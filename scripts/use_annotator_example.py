#!/usr/bin/env python3
"""
IELTS Collocation Annotator - 使用示例
演示如何在.skills/ielts-collocation-annotator中标注文章。
"""

import sys
import os

# 添加skills目录到路径
skills_path = os.path.join(os.path.dirname(__file__), '.skills')
sys.path.insert(0, skills_path)

# ===== 模拟Agent CLI =====
class MockAgentCLI:
    """模拟Agent CLI的LLM调用接口。"""

    def llm_call(self, messages, **kwargs):
        """
        统一的LLM调用接口。

        注意：这里使用模拟响应用于演示。
        在真实的Agent CLI中，这会调用实际配置的LLM（OpenAI/Anthropic/Local）。
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
        mock_response = f"""一、文本分析结果（IELTS Reading Passage）
识别出的30+关键搭配类型

1. IELTS高频固定表达
| 搭配 | 中文 | 出现位置 |
|------|------|---------|
| claim to fame | 成名原因 | Paragraph A |
| excel at | 擅长于 | Paragraph C |
| come across | 偶遇/发现 | Paragraph C |
| according to | 根据 | Paragraph B |
| such...that | 如此...以至于 | Paragraph A |
| both...and | 两者都... | Paragraph D |

2. 形容词-名词搭配
| 搭配 | 语境 | 例子 |
|------|------|------|
| grand families | 社会阶层 | "grand families settled" |
| influential architect | 人物评价 | "such an influential architect" |
| prosperous city | 经济状况 | "pleasant, prosperous city" |

3. 动词搭配
| 搭配 | 动作类型 |
|------|---------|
| settle and farm | 复合动作 | 定居和耕作 |
| organise education | 教育安排 | 组织教育 |
| co-opt | 招揽/吸收 | 招揽艺术家 |

4. 学术词汇束
| 结构 | 功能 | 例子 |
|------|------|------|
| such...that | 结果从句 | "such an influential architect that" |

5. 复杂名词短语结构
| 结构 | 例子 |
|------|------|------|
| the International Centre for Study | "the International Centre for Study" |

---

**说明**：
- 共识别出约30个关键搭配
- 覆盖固定表达、形容词-名词搭配、动词搭配、学术词束、复杂名词短语
- 适合IELTS备考和学习使用
"""

        print(f"   模拟响应长度: {len(mock_response)} 字符")
        print("   ✓ LLM调用完成（模拟）")

        return mock_response


# ===== 主程序 =====
def main():
    """主函数。"""
    print("\n" + "=" * 70)
    print("IELTS Collocation Annotator - 使用示例")
    print("=" * 70)

    # 读取文章文件
    file_path = "practice/reading/ielts-reading-test-1-20260206.md"

    print(f"\n📖 步骤1：读取文章文件")
    print(f"   文件: {file_path}")

    if not os.path.exists(file_path):
        print(f"   ❌ 文件不存在: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"   ✓ 文件已读取（{len(content)} 字符）")

    # 提取阅读正文（第一个篇章）
    print("\n📄 步骤2：提取阅读正文")

    # 查找第一个Reading Passage标题
    lines = content.split('\n')
    passage_lines = []
    in_reading = False

    for line in lines:
        if "## Reading Passage" in line:
            # 跳过标题行
            continue
        if "### Questions" in line or "---" in line:
            break

        if line.strip() and not in_reading:
            passage_lines.append(line)

    passage_text = '\n'.join(passage_lines)

    if not passage_text or len(passage_text) < 100:
        print("   ❌ 未找到有效的阅读正文")
        return

    print(f"   阅读正文: {len(passage_text)} 字符")

    # 初始化模拟Agent CLI
    print("\n📝 步骤3：初始化Agent CLI（模拟）")
    agent = MockAgentCLI()
    print("   ✓ Agent CLI已初始化（模拟）")

    # 导入标注器
    # 注意：这里直接从.skills/ielts-collocation-annotator导入
    try:
        from ielts_collocation_annotator import create_ielts_analysis_messages
        print("   ✓ IELTS Collocation Annotator导入成功")
    except ImportError:
        print("   ❌ IELTS Collocation Annotator未找到")
        return

    # 创建LLM消息
    messages = create_ielts_analysis_messages(
        text=passage_text,
        title="Andrea Palladio"
    )

    print("\n📡 步骤4：创建LLM消息")
    print(f"   系统提示词: {len(messages[0]['content'])} 字符")
    print(f"   用户消息: {len(messages[1]['content'])} 字符")

    # 调用Agent CLI的LLM
    print("\n📋 步骤5：调用Agent CLI的LLM")
    response = agent.llm_call(messages)

    print("\n📄 步骤6：显示标注结果预览")
    print("=" * 70)
    print("📊 标注结果预览（前30行）:")
    print("=" * 70)

    # 显示模拟响应的前30行
    lines = response.split('\n')
    for i, line in enumerate(lines[:30]):
        print(f"{i+1:2d}: {line}")

    print("\n" + "=" * 70)

    print("✅ 标注完成！（演示）")
    print("=" * 70)

    print("\n💡 在真实Agent CLI中的集成方式：")
    print("""
```python
# 1. 导入标注器
from .skills/ielts-collocation-annotator import create_ielts_analysis_messages

# 2. 创建LLM消息
messages = create_ielts_analysis_messages(
    text=passage_text,
    title="Andrea Palladio"
)

# 3. 调用您的Agent CLI的LLM
# 假设您的Agent CLI有以下方法
class YourAgentCLI:
    def llm_call(self, messages, **kwargs):
        # 调用实际配置的LLM（OpenAI/Anthropic/Local）
        pass

agent = YourAgentCLI()
response = agent.llm_call(messages)

# 4. 使用标注结果
print("完整标注结果：")
print(response)
```

# 5. 保存到新文件
with open("ielts-reading-test-1-20260206-annotated.md", "w") as f:
    f.write("# IELTS Collocation Analysis\n\n")
    f.write("本文档自动由IELTS Collocation Annotator生成\n\n")
    f.write("---\n\n")
    f.write(response)
    f.write("\n---\n")
    f.write("## 说明\n")
    f.write("- 使用工具: .skills/ielts-collocation-annotator\n")
    f.write("- LLM: Agent CLI配置的LLM\n")

print("\n" + "=" * 70)
print("✅ 完成！已保存到: ielts-reading-test-1-20260206-annotated.md")
print("=" * 70)
