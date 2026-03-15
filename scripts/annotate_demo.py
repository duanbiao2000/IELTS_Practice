#!/usr/bin/env python3
"""演示脚本：直接使用ielts-collocation-annotator核心功能"""
import sys, os

# 直接定义所需函数（避免模块导入问题）

def create_messages(text, title="IELTS Reading Passage"):
    user_message = f"""Passage Title: {title}

Passage Text:
{text}

Please analyze this passage according to the instructions in the system prompt."""
    return [
        {"role": "system", "content": """You are an expert in IELTS preparation..."""},
        {"role": "user", "content": user_message}
    ]

def extract_title(content):
    lines = content.split('\n')
    for line in lines:
        if line.strip().startswith('#'):
            return line.strip('#').strip()
    return "IELTS Reading Passage"

def extract_reading_passage(content):
    lines = content.split('\n')
    passage_lines = []
    in_reading = False
    for line in lines:
        if "Reading Passage" in line:
            in_reading = True
        if in_reading and ("Questions" in line or line.strip().startswith("### Questions")):
            break
        if in_reading and line.strip():
            passage_lines.append(line)
    return '\n'.join(passage_lines)

# 模拟Agent CLI
class MockAgent:
    def llm_call(self, messages, **kwargs):
        print("\n📡 调用LLM（模拟）")
        # 返回模拟响应
        return """一、文本分析结果（IELTS Reading Passage）
识别出的30+关键搭配类型

1. IELTS高频固定表达
| 搭配 | 中文 | 出现位置 |
|------|------|---------|
| claim to fame | 成名原因 | Paragraph A |
| principal claim to | 主要声称 | Paragraph A |
| excel at | 擅长于 | Paragraph C |
| come across | 偶遇/发现 | Paragraph C |

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
| one of | 部分指代 | "one of his finest buildings" |

5. 复杂名词短语结构
| 结构 | 例子 |
|------|------|
| Determiner + Adj + Noun + of-phrase | "the International Centre for Study" |
| Possessive + Adj + Noun | "Palladio's design" |

---

说明：
- 识别出约30个关键搭配
- 适合IELTS备考和学习使用
"""

# 主程序
def main():
    print("="*70)
    print("IELTS Collocation Annotator - 演示")
    print("="*70)
    
    # 读取文件
    file_path = "practice/reading/ielts-reading-test-1-20260206.md"
    print(f"\n📖 读取: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取
    title = extract_title(content)
    passage = extract_reading_passage(content)
    
    print(f"标题: {title}")
    print(f"正文: {len(passage)} 字符")
    
    # 创建消息并调用LLM
    messages = create_messages(passage, title)
    response = MockAgent().llm_call(messages)
    
    # 输出结果
    print(f"\n\n{response}")
    
    # 保存到文件
    output_path = file_path.replace('.md', '-demo-annotated.md')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# IELTS Collocation Analysis\n\n")
        f.write("本文档由IELTS Collocation Annotator生成\n\n")
        f.write(f"## {title}\n\n")
        f.write(response)
    
    print(f"\n✅ 已保存: {output_path}")

if __name__ == "__main__":
    main()
