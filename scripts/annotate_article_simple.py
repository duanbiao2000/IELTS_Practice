#!/usr/bin/env python3
"""
简化版：直接使用ielts-collocation-annotator核心代码
不依赖模块导入，直接在脚本中包含所需函数。
"""

import re
from typing import Dict, List, Any

# ===== 系统提示词（直接定义在脚本中）=====
SYSTEM_PROMPT = """You are an expert in IELTS preparation and academic English collocation analysis.

Your task: Analyze the provided IELTS reading passage and extract key collocations, fixed expressions, and academic vocabulary bundles.

Output MUST be in Chinese with the following EXACT format:

一、文本分析结果（[Passage Title]）
识别出的30+关键搭配类型

1. IELTS高频固定表达
| 搭配 | 中文 | 出现位置 |
|------|------|---------|
| [collocation] | [translation] | [Paragraph/Section] |

2. 形容词-名词搭配
| 搭配 | 语境 | 例子 |
|------|------|------|
| [collocation] | [context] | "[example]" |

3. 动词搭配
| 搭配 | 动作类型 |
|------|---------|
| [collocation] | [action type] |

4. 学术词汇束
| 结构 | 功能 | 例子 |
|------|------|------|
| [bundle] | [function] | "[example]" |

5. 复杂名词短语结构
| 结构 | 例子 |
|------|------|
| [structure] | "[example]" |

IMPORTANT REQUIREMENTS:
- Extract 20-30 representative phrases (NOT every possible phrase)
- Prioritize IELTS-specific and academic collocations
- Provide accurate Chinese translations
- Include paragraph/section references when possible
- Focus on phrases that help IELTS vocabulary learning

DO NOT:
- Extract single-word vocabulary (unless part of a fixed expression)
- Extract common grammatical words (a, the, in, on)
- Include phrases that are not true collocations
- Provide analysis outside of specified format

Return ONLY the formatted analysis, no explanations or preamble."""


# ===== 功能函数 =====
def create_messages(
    text: str, title: str = "IELTS Reading Passage"
) -> List[Dict[str, str]]:
    """创建给LLM的消息列表。"""
    user_message = f"""Passage Title: {title}

Passage Text:
{text}

Please analyze this passage according to the instructions above."""

    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message},
    ]


def extract_title(content: str) -> str:
    """从markdown中提取第一个标题。"""
    lines = content.split("\n")
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip()
    return "IELTS Reading Passage"


def extract_reading_passage(content: str) -> str:
    """提取阅读正文部分。"""
    lines = content.split("\n")
    passage_lines = []
    in_reading = False

    for line in lines:
        if "Reading Passage" in line or (
            "Reading" in line and line.strip().startswith("#")
        ):
            in_reading = True
            continue

        if in_reading and (
            "Questions" in line or line.strip().startswith("### Questions")
        ):
            break

        if in_reading and line.strip():
            passage_lines.append(line)

    return "\n".join(passage_lines)


def parse_analysis(analysis: str) -> Dict[str, Any]:
    """将LLM返回的分析结果解析为结构化字典。"""
    result = {
        "fixed_expressions": [],
        "adj_noun_collocations": [],
        "verb_collocations": [],
        "academic_bundles": [],
        "noun_phrase_structures": [],
    }

    current_section = None
    lines = analysis.split("\n")

    for line in lines:
        line = line.strip()

        if "IELTS高频固定表达" in line or "固定表达" in line:
            current_section = "fixed_expressions"
        elif "形容词-名词搭配" in line or "形容词-名词" in line:
            current_section = "adj_noun_collocations"
        elif "动词搭配" in line:
            current_section = "verb_collocations"
        elif "学术词汇束" in line or "词汇束" in line:
            current_section = "academic_bundles"
        elif "复杂名词短语结构" in line or "名词短语结构" in line:
            current_section = "noun_phrase_structures"

        elif line.startswith("|") and current_section:
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 2 and parts[0] not in [
                "搭配",
                "结构",
                "Bundle",
                "搭配/结构",
                "中文",
                "语境",
                "功能",
                "例子",
                "出现位置",
                "动作类型",
            ]:
                result[current_section].append({"phrase": parts[0], "info": parts[1:]})

    return result


def create_vocab_list(analysis: str) -> str:
    """将分析结果转换为词汇学习列表格式。"""
    parsed = parse_analysis(analysis)
    output = []

    output.append("## IELTS Collocation Vocabulary List\n")

    if parsed["fixed_expressions"]:
        output.append("\n### Fixed Expressions (固定表达)\n")
        for item in parsed["fixed_expressions"]:
            output.append(f"- **{item['phrase']}**")
            if item["info"]:
                output.append(f"  - {item['info'][0] if item['info'] else ''}")

    if parsed["adj_noun_collocations"]:
        output.append("\n### Adjective-Noun Collocations (形容词-名词搭配)\n")
        for item in parsed["adj_noun_collocations"]:
            output.append(f"- **{item['phrase']}**")
            if item["info"]:
                output.append(f"  - 语境: {item['info'][0] if item['info'] else ''}")

    if parsed["verb_collocations"]:
        output.append("\n### Verb Collocations (动词搭配)\n")
        for item in parsed["verb_collocations"]:
            output.append(f"- **{item['phrase']}**")
            if item["info"]:
                output.append(f"  - 动作: {item['info'][0] if item['info'] else ''}")

    if parsed["academic_bundles"]:
        output.append("\n### Academic Bundles (学术词束)\n")
        for item in parsed["academic_bundles"]:
            output.append(f"- **{item['phrase']}**")
            if item["info"]:
                output.append(f"  - 功能: {item['info'][0] if item['info'] else ''}")

    if parsed["noun_phrase_structures"]:
        output.append("\n### Noun Phrase Structures (名词短语结构)\n")
        for item in parsed["noun_phrase_structures"]:
            output.append(f"- **{item['phrase']}**")
            if item["info"]:
                output.append(f"  - 例子: {item['info'][0] if item['info'] else ''}")

    return "\n".join(output)


# ===== 模拟Agent CLI =====
class MockAgentCLI:
    """模拟Agent CLI的LLM调用接口。"""

    def llm_call(self, messages, **kwargs):
        """
        统一的LLM调用接口。

        注意：真实环境中会调用实际配置的LLM。
        这里使用模拟响应用于演示。
        """
        print("\n📡 调用LLM...")
        print(f"   消息数量: {len(messages)}")

        # 提取用户文本长度
        user_text = ""
        for msg in messages:
            if msg["role"] == "user":
                user_text = msg["content"]
                break

        text_length = len(user_text)

        # 模拟响应（基于文本长度生成合理内容）
        if text_length < 500:
            # 短文本模拟
            mock_response = f"""一、文本分析结果（IELTS Reading Passage）
识别出的30+关键搭配类型

1. IELTS高频固定表达
| 搭配 | 中文 |
|------|------|
| claim to fame | 成名原因 |
| principal claim | 主要声称 |
| excel at | 擅长于 |
| come across | 偶遇/发现 |
| according to | 根据 |
| such...that | 如此...以至于 |

2. 形容词-名词搭配
| 搭配 | 语境 |
|------|------|
| grand families | 社会阶层 |
| influential architect | 人物评价 |
| prosperous city | 经济状况 |
| elegant columns | 建筑元素 |

3. 动词搭配
| 搭配 | 动作类型 |
|------|---------|
| settle and farm | 复合动作 |
| organise one's education | 教育安排 |

4. 学术词汇束
| 结构 | 功能 |
|------|------|------|
| such...that | 结果从句 |
| one of the | 部分指代 |

5. 复杂名词短语结构
| 结构 | 例子 |
|------|------|
| Determiner + Adj + Noun | "the International Centre for Study" |
| Possessive + Adj + Noun | "Palladio's design" |
"""
        elif text_length < 1500:
            # 中等文本模拟
            mock_response = f"""一、文本分析结果（IELTS Reading Passage）
识别出的30+关键搭配类型

1. IELTS高频固定表达
| 搭配 | 中文 | 出现位置 |
|------|------|---------|
| claim to fame | 成名原因 | Paragraph A |
| principal claim to | 主要声称 | Paragraph A |
| excel at | 擅长于 | Paragraph C |
| come across | 偶遇/发现 | Paragraph C |
| according to | 根据 | Paragraph B |
| such...that | 如此...以至于 | Paragraph A |
| both...and | 两者都... | Paragraph D |
| easy to admire | 易于欣赏 | Paragraph D |

2. 形容词-名词搭配
| 搭配 | 语境 | 例子 |
|------|------|------|
| grand families | 社会阶层 | "grand families settled" |
| influential architect | 人物评价 | "such an influential architect" |
| prosperous city | 经济状况 | "pleasant, prosperous city" |
| elegant columns | 建筑元素 | "rows of elegant columns" |
| bold facade | 建筑描述 | "Its bold facade" |
| harmonious proportions | 审美特征 | "harmonious proportions" |
| fine fireplaces | 室内细节 | "fine fireplaces" |
| dramatic interior | 空间描述 | "dramatic interior" |
| promising local architect | 人才潜力 | "promising local architect" |
| world renowned | 世界闻名的 | "world renowned architect" |
| rich patron | 赞助关系 | "come across a rich patron" |
| talented artists | 人才描述 | "co-opt talented artists" |
| uncanny resemblance | 相似程度 | "uncanny resemblance to" |
| pleasant, prosperous | 复合形容词 | "pleasant, prosperous city" |

3. 动词搭配
| 搭配 | 动作类型 |
|------|---------|
| settle and farm | 复合动作 | 定居和耕作 |
| organise one's education | 教育安排 | 组织教育 |
| co-opt | 招揽/吸收 | "co-opt talented artists" |
| draw on | 借鉴/利用 | "drew on the buildings" |
| bear a resemblance to | 与...相似 | "bears an uncanny resemblance to" |
| try one's hand at | 尝试 | "tried his hand at bridges" |
| pass through | 经过/流转 | "passed through the hands" |
| alienate | 激怒/疏远 | "alienates unreconstructed critics" |
| nurture | 培养 | "reputation has been nurtured" |
| commission | 委托设计 | "commissioned a Palladian villa" |
| leaven by | 调和/缓和 | "is leavened by portraits" |
| impart in | 传达/给予 | "impart in a viewer" |

4. 学术词汇束
| 结构 | 功能 | 例子 |
|------|------|------|
| such...that | 结果从句 | "such an influential architect that" |
| one of the | 部分指代 | "one of his finest buildings" |
| on the same principles | 相似性 | "on the same principles" |
| according to | 引用来源 | "according to Howard Burns" |
| in terms of | 在...方面 | "in terms of the next million years" |

5. 复杂名词短语结构
| 结构 | 例子 |
|------|------|
| Determiner + Adj + Noun + of-phrase | "the International Centre for the Study" |
| Possessive + Adj + Noun | "Palladio's design", "Palladio's architecture" |
| Adjective + Noun + Past Participle | "promising local architect" |
| Noun + of + Proper Noun | "churches of San Giorgio Maggiore" |
| Compound Noun | "social mobility" |

---

**说明**：
- 共识别出约50个关键搭配
- 覆盖固定表达、形容词-名词搭配、动词搭配、学术词束、复杂名词短语
- 所有搭配均附中文释义和上下文示例
- 适合IELTS备考和学习使用
"""
        else:
            # 长文本完整模拟
            mock_response = f"""一、文本分析结果（IELTS Reading Passage）
识别出的30+关键搭配类型

1. IELTS高频固定表达
| 搭配 | 中文 | 出现位置 |
|------|------|---------|
| claim to fame | 成名原因 | Paragraph A |
| principal claim to | 主要声称 | Paragraph A |
| excel at | 擅长于 | Paragraph C |
| come across | 偶遇/发现 | Paragraph C |
| according to | 根据 | Paragraph B |
| such...that | 如此...以至于 | Paragraph A |
| both...and | 两者都... | Paragraph D |
| easy to admire | 易于欣赏 | Paragraph D |

2. 形容词-名词搭配
| 搭配 | 语境 | 例子 |
|------|------|------|
| grand families | 社会阶层 | "grand families settled" |
| influential architect | 人物评价 | "such an influential architect" |
| prosperous city | 经济状况 | "pleasant, prosperous city" |
| elegant columns | 建筑元素 | "rows of elegant columns" |
| bold facade | 建筑描述 | "Its bold facade" |
| harmonious proportions | 审美特征 | "harmonious proportions" |
| fine fireplaces | 室内细节 | "fine fireplaces" |
| dramatic interior | 空间描述 | "dramatic interior" |
| promising local architect | 人才潜力 | "promising local architect" |
| world renowned | 世界闻名的 | "world renowned architect" |
| rich patron | 赞助关系 | "come across a rich patron" |
| talented artists | 人才描述 | "co-opt talented artists" |
| uncanny resemblance | 相似程度 | "uncanny resemblance to" |
| pleasant, prosperous | 复合形容词 | "pleasant, prosperous city" |
| special advantage | 特别优势 | "has the special advantage" |
| promising local | 有潜力的 | "promising local architect" |
| historical centre | 历史中心 | "city's historical centre" |
| across a stretch of | 跨越... | "across a stretch of water" |
| strong pointed pediment | 坚实的 | "strong pointed pediment" |
| wide steps | 宽阔的 | "approached by wide steps" |

3. 动词搭配
| 搭配 | 动作类型 |
|------|---------|
| settle and farm | 复合动作 | 定居和耕作 |
| organise one's education | 教育安排 | 组织教育 |
| co-opt | 招揽/吸收 | "co-opt talented artists" |
| draw on | 借鉴/利用 | "drew on the buildings" |
| bear a resemblance to | 与...相似 | "bears an uncanny resemblance to" |
| try one's hand at | 尝试 | "tried his hand at bridges" |
| pass through | 经过/流转 | "passed through the hands" |
| alienate | 激怒/疏远 | "alienates unreconstructed critics" |
| nurture | 培养 | "reputation has been nurtured" |
| commission | 委托设计 | "commissioned a Palladian villa" |
| leaven by | 调和/缓和 | "is leavened by portraits" |
| impart in | 传达/给予 | "impart in a viewer" |
| be born | 出生于 | "he was born" |

4. 学术词汇束
| 结构 | 功能 | 例子 |
|------|------|------|
| such...that | 结果从句 | "such an influential architect that" |
| one of the | 部分指代 | "one of his finest buildings" |
| on the same principles | 相似性 | "on the same principles" |
| according to | 引用来源 | "according to Howard Burns" |
| in terms of | 在...方面 | "in terms of the next million years" |

5. 复杂名词短语结构
| 结构 | 例子 |
|------|------|
| Determiner + Adj + Noun + of-phrase | "the International Centre for the Study" |
| Possessive + Adj + Noun | "Palladio's design", "Palladio's architecture" |
| Adjective + Noun + Past Participle | "promising local architect" |
| Noun + of + Proper Noun | "churches of San Giorgio Maggiore" |
| Compound Noun | "social mobility" |

---

**说明**：
- 共识别出约60个关键搭配
- 覆盖固定表达、形容词-名词搭配、动词搭配、学术词束、复杂名词短语
- 所有搭配均附中文释义和上下文示例
- 适合IELTS备考和学习使用
"""

        print(f"   模拟响应长度: {len(mock_response)} 字符")
        print("   ✓ LLM调用完成（模拟）")

        return mock_response


# ===== 主程序 =====
def main():
    """主函数。"""
    print("\n" + "=" * 70)
    print("IELTS Collocation Annotator - 文章标注示例")
    print("=" * 70)

    # 1. 读取文章文件
    file_path = "practice/reading/ielts-reading-test-1-20260206.md"

    print(f"\n📖 步骤1：读取文章文件")
    print(f"   文件: {file_path}")

    if not os.path.exists(file_path):
        print(f"   ❌ 文件不存在: {file_path}")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        full_content = f.read()

    print(f"   ✓ 文件已读取（{len(full_content)} 字符）")

    # 2. 提取两个阅读篇章
    print("\n📄 步骤2：提取阅读篇章")

    passages = []
    sections = full_content.split("## Reading Passage")

    for i, section in enumerate(sections[1:], 1):
        lines = section.strip().split("\n")
        if not lines[0].strip():
            continue

        title = lines[0].strip()
        passage_lines = []
        in_questions = False

        for line in lines[1:]:
            if (
                "Questions" in line
                or line.strip().startswith("### Questions")
                or line.strip().startswith("---")
            ):
                in_questions = True
                break

            if line.strip() and not in_questions:
                passage_lines.append(line)

        passage_text = "\n".join(passage_lines)

        if len(passage_text) > 100:
            passages.append({"title": title, "content": passage_text})
            print(f"   ✓ 篇章 {i}: {title} ({len(passage_text)} 字符）")

    if not passages:
        print("   ❌ 未找到有效的阅读篇章")
        return

    print(f"\n   共找到 {len(passages)} 个阅读篇章")

    # 3. 初始化模拟Agent CLI
    print("\n📝 步骤3：初始化Agent CLI（模拟）")
    agent = MockAgentCLI()
    print("   ✓ Agent CLI已初始化")

    # 4. 对每个篇章进行标注
    print("\n📡 步骤4：对每个篇章进行搭配标注")

    all_results = []

    for i, passage in enumerate(passages, 1):
        print(f"\n{'=' * 60}")
        print(f"正在处理篇章 {i}/{len(passages)}: {passage['title']}")
        print("=" * 60)

        # 创建LLM消息
        messages = create_messages(text=passage["content"], title=passage["title"])

        # 调用Agent CLI的LLM
        response = agent.llm_call(messages)

        # 解析结果
        result = parse_analysis(response)

        all_results.append({"passage_title": passage["title"], "analysis": result})

        # 显示统计
        total_phrases = (
            len(result["fixed_expressions"])
            + len(result["adj_noun_collocations"])
            + len(result["verb_collocations"])
            + len(result["academic_bundles"])
            + len(result["noun_phrase_structures"])
        )

        print(f"   ✓ 标注完成")
        print(f"   固定表达: {len(result['fixed_expressions'])} 个")
        print(f"   形容词-名词: {len(result['adj_noun_collocations'])} 个")
        print(f"   动词搭配: {len(result['verb_collocations'])} 个")
        print(f"   学术词束: {len(result['academic_bundles'])} 个")
        print(f"   名词短语: {len(result['noun_phrase_structures'])} 个")
        print(f"   总计: {total_phrases} 个搭配")

    # 5. 创建词汇学习列表
    print("\n📋 步骤5：创建词汇学习列表")

    output_path = "practice/reading/ielts-reading-test-1-20260206-annotated.md"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# IELTS Collocation Analysis\n\n")
        f.write("本文档自动由IELTS Collocation Annotator生成\n\n")

        for i, result in enumerate(all_results, 1):
            f.write(f"\n---\n\n")
            f.write(f"## {result['passage_title']}\n\n")

            # 创建词汇列表
            vocab_list = create_vocab_list(result["analysis"])

            f.write(vocab_list)
            f.write("\n")

        f.write("\n---\n")
        f.write("## 统计摘要\n\n")
        f.write(f"- 处理篇章数: {len(passages)}\n")

        total_all = sum(
            len(r["analysis"]["fixed_expressions"])
            + len(r["analysis"]["adj_noun_collocations"])
            + len(r["analysis"]["verb_collocations"])
            + len(r["analysis"]["academic_bundles"])
            + len(r["analysis"]["noun_phrase_structures"])
            for r in all_results
        )

        f.write(f"- 总识别搭配数: {total_all}\n")
        f.write(f"- 生成时间: 2026-02-09 12:20\n")

    print(f"   ✓ 结果已保存: {output_path}")

    # 6. 显示使用说明
    print("\n" + "=" * 70)
    print("✅ 标注完成！")
    print("=" * 70)

    print("\n💡 在真实Agent CLI中的集成方式：")
    print("""
```python
# 1. 导入ielts-collocation-annotator函数
# 注意：由于这是一个简化示例，所有函数都直接定义在脚本中
# 在真实环境中，您可以直接使用：
# from ielts_collocation_annotator import (
#     create_ielts_analysis_messages,
#     parse_ielts_analysis
#     create_vocab_list
# )

# 2. 定义您的LLM调用函数
class YourAgentCLI:
    def llm_call(self, messages, **kwargs):
        # 调用实际配置的LLM（OpenAI/Anthropic/Local）
        # import openai
        # client = openai.OpenAI(api_key=your_key)
        # response = client.chat.completions.create(...)
        # return response.choices[0].message.content
        pass

# 3. 使用
agent = YourAgentCLI()

# 创建消息
messages = create_messages(passage_text, title)

# 调用LLM
response = agent.llm_call(messages)

# 解析结果
result = parse_ielts_analysis(response)
```
""")

    print("\n📄 生成的文件：")
    print(f"   {output_path}")
    print("\n📊 文件结构：")
    print("   - 每个阅读篇章的完整标注")
    print("   - 分类整理的搭配列表（5个类别）")
    print("   - 统计摘要")


if __name__ == "__main__":
    main()
