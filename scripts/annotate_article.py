#!/usr/bin/env python3
"""
示例：使用IELTS Collocation Annotator技能标注文章

演示如何在Agent CLI环境中集成使用ielts-collocation-annotator。
"""

import sys
import os

# 添加skills目录到路径
skills_dir = os.path.join(os.path.dirname(__file__), ".skills")
sys.path.insert(0, skills_dir)

from ielts_collocation_annotator import (
    create_ielts_analysis_messages,
    parse_ielts_analysis,
    extract_vocab_from_analysis,
    create_vocab_list,
    process_ielts_file,
)


# ===== 模拟Agent CLI的LLM调用接口 =====
class MockAgentCLI:
    """
    模拟的Agent CLI LLM接口。

    在真实的Agent CLI中，这会调用实际配置的LLM（OpenAI/Anthropic/Local）。
    """

    def llm_call(self, messages, **kwargs):
        """
        统一的LLM调用接口。

        Args:
            messages: 消息列表 [{"role": "system", "content": "..."}]
            **kwargs: 额外参数

        Returns:
            LLM响应文本

        注意：这里使用模拟响应，真实环境中会调用实际LLM。
        """
        print("\n📡 调用LLM...")
        print(f"   消息数量: {len(messages)}")

        # 提取用户文本长度
        user_text = ""
        for msg in messages:
            if msg["role"] == "user":
                user_text = msg["content"]
                break

        # 基于文本长度生成模拟响应
        text_length = len(user_text)

        # 对于真实的Agent CLI，这里是调用实际LLM的地方
        # 例如：
        # import openai
        # client = openai.OpenAI(api_key="your-key")
        # response = client.chat.completions.create(...)
        # return response.choices[0].message.content

        # 模拟响应（用于演示）
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
| as a result of | 因果关系 | (可能出现在文中） |
| in terms of | 在...方面 | (学术表达） |

5. 复杂名词短语结构
| 结构 | 例子 |
|------|------|
| Determiner + Adjective + Noun + of-phrase | "the International Centre for the Study" |
| Possessive + Adjective + Noun | "Palladio's design", "Palladio's architecture" |
| Adjective + Noun + Past Participle | "promising local architect" |
| Noun + of + Proper Noun | "churches of San Giorgio Maggiore" |
| Compound Noun | "social mobility" |
| Noun + with + Noun Phrase | "pediment decorated with columns" |

---

**说明**：
- 共识别出约60个关键搭配
- 覆盖固定表达、形容词-名词搭配、动词搭配、学术词束、复杂名词短语
- 所有搭配均附中文释义和上下文示例
- 适合IELTS备考和学习使用

**使用提示**：
- 重点关注IELTS高频固定表达，这些在考试中经常出现
- 形容词-名词搭配是雅思写作和阅读的重点词汇类型
- 动词搭配帮助理解文章的逻辑关系
- 学术词汇束提升学术写作的连贯性
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

    # 1. 初始化模拟Agent CLI
    print("\n📝 步骤1：初始化Agent CLI（模拟）")
    agent = MockAgentCLI()
    print("   ✓ Agent CLI已初始化")

    # 2. 读取文章文件
    file_path = "practice/reading/ielts-reading-test-1-20260206.md"

    print(f"\n📖 步骤2：读取文章文件")
    print(f"   文件: {file_path}")

    if not os.path.exists(file_path):
        print(f"   ❌ 文件不存在: {file_path}")
        return

    # 读取完整文件
    with open(file_path, "r", encoding="utf-8") as f:
        full_content = f.read()

    print(f"   ✓ 文件已读取（{len(full_content)} 字符）")

    # 3. 提取两个阅读篇章
    print("\n📄 步骤3：提取阅读篇章")

    passages = []

    # 方法1：按标题分割
    sections = full_content.split("## Reading Passage")

    for i, section in enumerate(sections[1:], 1):  # 跳过空第一部分
        lines = section.strip().split("\n")
        if not lines[0].strip():
            continue

        title = lines[0].strip()

        # 提取正文（到Questions之前）
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

        if len(passage_text) > 100:  # 只处理有足够内容的篇章
            passages.append({"title": title, "content": passage_text})
            print(f"   ✓ 篇章 {i}: {title} ({len(passage_text)} 字符）")

    if not passages:
        print("   ❌ 未找到有效的阅读篇章")
        return

    print(f"\n   共找到 {len(passages)} 个阅读篇章")

    # 4. 对每个篇章进行标注
    print("\n📡 步骤4：对每个篇章进行搭配标注")

    all_results = []

    for i, passage in enumerate(passages, 1):
        print(f"\n{'=' * 60}")
        print(f"正在处理篇章 {i}/{len(passages)}: {passage['title']}")
        print("=" * 60)

        # 创建LLM消息
        messages = create_ielts_analysis_messages(
            text=passage["content"], title=passage["title"]
        )

        # 调用Agent CLI的LLM
        response = agent.llm_call(messages)

        # 解析结果
        result = parse_ielts_analysis(response)

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
# 1. 导入工具
from ielts_collocation_annotator import (
    create_ielts_analysis_messages,
    parse_ielts_analysis
)

# 2. 定义您的LLM调用函数（替换MockAgentCLI）
class YourAgentCLI:
    def llm_call(self, messages, **kwargs):
        # 调用实际配置的LLM
        # import openai  # 或 anthropic, 或本地模型
        # client = openai.OpenAI(api_key=your_key)
        # response = client.chat.completions.create(...)
        # return response.choices[0].message.content
        pass

# 3. 使用
agent = YourAgentCLI()

# 创建消息
messages = create_ielts_analysis_messages(passage_text, title)

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

    print("\n" + "=" * 70)
    print("🎯 关键功能：")
    print("=" * 70)
    print("""
1. ✅ 零依赖 - 只用Python标准库
2. ✅ Agent CLI原生 - 完美适配您的LLM接口
3. ✅ 纯提示词引擎 - 只负责提示词和解析
4. ✅ 批量处理 - 自动处理多个篇章
5. ✅ 格式化输出 - 生成Markdown格式的词汇学习材料
6. ✅ 结构化数据 - 解析为字典便于后续处理
""")


if __name__ == "__main__":
    main()
