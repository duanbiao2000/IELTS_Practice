# IELTS Collocation Annotator - 零依赖，纯提示词引擎

## 🎉 完成！工具已创建

**版本**: 3.0 - 纯提示词和分析工具

**核心特点**:
- ✅ **零外部依赖** - 只用Python标准库（`re`, `typing`）
- ✅ **纯提示词引擎** - 只负责生成提示词和解析结果
- ✅ **Agent CLI原生** - 与任何Agent CLI框架完美集成
- ✅ **通用接口** - 适配OpenAI、Anthropic、本地模型等

---

## 📦 项目结构

```
.skills/ielts-collocation-annotator/
├── ielts_collocation_annotator.py    # 核心模块（纯Python，无依赖）
├── __init__.py                         # 包导出
├── README.md                          # 使用文档
├── EXAMPLES.md                        # 完整集成示例
├── skill.json                         # Skill元数据
└── AGENT_CLI_INTEGRATION.md         # Agent CLI集成指南
```

---

## 🚀 在Agent CLI中使用（3秒上手）

### 最简单的方式

```python
# 1. 导入工具函数
from ielts_collocation_annotator import create_ielts_analysis_messages

# 2. 创建LLM消息
messages = create_ielts_analysis_messages(
    text=passage_text,
    title="Andrea Palladio"
)

# 3. 调用您的Agent CLI的LLM接口
response = your_agent.llm_call(messages)

# 4. （可选）解析结果
from ielts_collocation_annotator import parse_ielts_analysis
result = parse_ielts_analysis(response)
print(f"找到 {len(result['fixed_expressions'])} 个固定表达")
```

### 完整示例

```python
# 导入所有需要的函数
from ielts_collocation_annotator import (
    create_ielts_analysis_messages,
    parse_ielts_analysis,
    extract_vocab_from_analysis,
    create_vocab_list
)

# 读取IELTS文件
with open("ielts-reading-1.md", 'r') as f:
    content = f.read()

# 提取标题和正文
from ielts_collocation_annotator import IELTSCollocationAnnotator
title = IELTSCollocationAnnotator.extract_title(content)
passage = IELTSCollocationAnnotator.extract_reading_passage(content)

# 创建LLM消息
messages = create_ielts_analysis_messages(passage, title)

# 调用LLM
response = your_agent.llm_call(messages)

# 解析结果
result = parse_ielts_analysis(response)

# 创建词汇学习列表
vocab_list = create_vocab_list(response)

# 保存
with open("vocab-list.md", 'w') as f:
    f.write(vocab_list)

print("✅ 完成！")
```

---

## 📊 API参考

### 便捷函数（推荐使用）

| 函数 | 说明 | 返回 |
|------|------|------|
| `create_ielts_analysis_messages(text, title)` | 创建LLM消息 | `List[Dict]` |
| `parse_ielts_analysis(analysis)` | 解析分析结果 | `Dict[str, Any]` |
| `extract_vocab_from_analysis(analysis)` | 提取词汇列表 | `Dict[str, List[str]]` |
| `create_vocab_list(analysis)` | 创建词汇表 | `str` (Markdown) |
| `process_ielts_file(file_path)` | 处理文件 | `(title, passage_text)` |

### 静态方法（IELTSCollocationAnnotator类）

| 方法 | 说明 | 用途 |
|------|------|------|
| `create_messages(text, title)` | 创建消息列表 | LLM调用 |
| `extract_title(content)` | 提取标题 | 文件处理 |
| `extract_reading_passage(content)` | 提取正文 | 文件处理 |
| `parse_analysis(analysis)` | 解析结果 | 后续处理 |
| `extract_phrases_by_category(analysis)` | 按类别提取 | 词汇学习 |
| `create_vocab_list(analysis)` | 创建词汇表 | 生成材料 |

---

## 🎯 完整使用场景

### 场景1：分析单个文本

```python
from ielts_collocation_annotator import create_ielts_analysis_messages

# 您的文本
text = """
Vicenza is a pleasant, prosperous city in the Veneto, 60km west of Venice.
Its grand families settled and farmed the area from the 16th century.
But its principal claim to fame is Andrea Palladio...
"""

# 创建消息
messages = create_ielts_analysis_messages(text, "Andrea Palladio")

# 调用LLM
response = your_agent.llm_call(messages)

print(response)
```

### 场景2：处理IELTS文件

```python
from ielts_collocation_annotator import process_ielts_file, create_vocab_list

# 处理文件
title, passage = process_ielts_file("practice/reading/ielts-reading-1.md")

# 分析
from ielts_collocation_annotator import create_ielts_analysis_messages
messages = create_ielts_analysis_messages(passage, title)
response = your_agent.llm_call(messages)

# 创建词汇表
vocab = create_vocab_list(response)
print(vocab)
```

### 场景3：批量处理多个文件

```python
import glob
from ielts_collocation_annotator import process_ielts_file, create_vocab_list

# 批量处理
files = glob.glob("practice/reading/*.md")
for file_path in files:
    title, passage = process_ielts_file(file_path)

    # 分析
    from ielts_collocation_annotator import create_ielts_analysis_messages
    messages = create_ielts_analysis_messages(passage, title)
    response = your_agent.llm_call(messages)

    # 保存
    vocab = create_vocab_list(response)
    output_path = file_path.replace(".md", "-vocab.md")
    with open(output_path, 'w') as f:
        f.write(vocab)
    print(f"✅ {file_path}")
```

### 场景4：只提取特定类别

```python
from ielts_collocation_annotator import extract_vocab_from_analysis

# 分析
messages = create_ielts_analysis_messages(text, title)
response = your_agent.llm_call(messages)

# 只提取固定表达
vocab = extract_vocab_from_analysis(response)
fixed_expressions = vocab["fixed_expressions"]

print("学习这些固定表达：")
for phrase in fixed_expressions:
    print(f"  - {phrase}")
```

---

## 📝 输出格式

### LLM消息格式（传递给Agent CLI）

```python
[
    {
        "role": "system",
        "content": "You are an expert in IELTS preparation..."  # 系统提示词
    },
    {
        "role": "user",
        "content": "Passage Title: Andrea Palladio\n\nPassage Text: ..."  # 用户消息
    }
]
```

### 分析结果格式（LLM返回）

完全匹配您的示例格式：

```markdown
一、文本分析结果（Andrea Palladio：Italian architect）
识别出的30+关键搭配类型

1. IELTS高频固定表达
| 搭配 | 中文 | 出现位置 |
|------|------|---------|
| claim to fame | 成名原因 | Paragraph A |
| world renowned | 世界闻名的 | Paragraph C |

2. 形容词-名词搭配
| 搭配 | 语境 | 例子 |
|------|------|------|
| grand families | 社会阶层 | "grand families settled" |
| influential architect | 人物评价 | "such an influential architect" |

3. 动词搭配
| 搭配 | 动作类型 |
|------|---------|
| settle and farm | 复合动作 |
| come across | 偶遇/发现 |

4. 学术词汇束
| 结构 | 功能 | 例子 |
|------|------|------|
| such...that | 结果从句 | "such an influential architect that" |

5. 复杂名词短语结构
| 结构 | 例子 |
|------|------|
| Det + Adj + Noun + of-phrase | "the International Centre for Study" |
```

---

## 🔧 测试验证

### 运行测试脚本

```bash
# 在项目目录下运行
python test_annotator.py
```

预期输出：

```
✅ IELTS Collocation Annotator v3.0
======================================================================

📊 核心功能:
  ✓ 消息创建 (create_messages)
  ✓ 结果解析 (parse_analysis)
  ✓ 文件处理 (extract_title, extract_reading_passage)
  ✓ 词汇提取 (extract_phrases_by_category)
  ✓ 列表生成 (create_vocab_list)

======================================================================
✅ 所有功能正常！

💡 使用方式:
  from ielts_collocation_annotator import create_ielts_analysis_messages
  messages = create_ielts_analysis_messages(text, title)
  response = your_agent.llm_call(messages)
======================================================================
```

---

## 🎯 总结

### 核心优势

| 特点 | 说明 |
|------|------|
| ✅ **零依赖** | 只用`re`和`typing`两个标准库 |
| ✅ **纯提示词** | 专注消息生成和结果解析 |
| ✅ **Agent CLI原生** | 完美适配任何Agent框架 |
| ✅ **通用接口** | 支持OpenAI、Anthropic、Local LLM |
| ✅ **灵活扩展** | 轻松自定义提示词和解析逻辑 |
| ✅ **易于集成** | 只需导入函数，无需复杂配置 |

### 使用流程

```
1. Agent CLI配置LLM（您的事）
       ↓
2. 用户请求分析IELTS阅读
       ↓
3. Agent调用工具函数创建LLM消息
       ↓
4. Agent调用自身LLM接口
       ↓
5. LLM返回分析结果
       ↓
6. Agent使用工具函数解析结果
       ↓
7. 输出格式化的搭配分析
```

### 关键代码模式

```python
# 模式1：基础使用
from ielts_collocation_annotator import create_ielts_analysis_messages
messages = create_ielts_analysis_messages(text, title)
response = your_agent.llm_call(messages)

# 模式2：解析结果
from ielts_collocation_annotator import parse_ielts_analysis
result = parse_ielts_analysis(response)

# 模式3：处理文件
from ielts_collocation_annotator import process_ielts_file
title, passage = process_ielts_file("file.md")
```

---

## 📚 详细文档

- **使用指南**: `.skills/ielts-collocation-annotator/README.md`
- **完整示例**: `.skills/ielts-collocation-annotator/EXAMPLES.md`
- **Agent CLI集成**: `.skills/ielts-collocation-annotator/AGENT_CLI_INTEGRATION.md`

---

## 🎯 开始使用

### 在您的Agent CLI中集成

```python
# 添加skills目录到Python路径
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.skills'))

# 导入工具
from ielts_collocation_annotator import create_ielts_analysis_messages

# 创建消息
messages = create_ielts_analysis_messages(text, title)

# 调用LLM
response = your_agent.llm_call(messages)
```

就这么简单！🎉
