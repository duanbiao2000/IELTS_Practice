# Draft: IELTS Practice Repository Design

## User Intent
用户想要将 /mnt/d/MyDocs/IELTS_Practice 目录作为日常雅思训练仓库，询问：
1. 如何设计仓库结构
2. 准备哪些适用于当前项目的skills

## Context from Research
IELTS考试包含四个主要部分：
- Listening (听力)
- Reading (阅读)
- Writing (写作) - Task 1 & Task 2
- Speaking (口语)

## User Requirements (Confirmed)

### 当前水平
- **初级 (5.0-6.0)**: 需要全面提升基础

### 目标分数
- **6.5-7.0**: 满足大多数研究生课程要求

### 重点模块
- **Listening (听力)**: 需要练习听力理解和笔记记录
- **Reading (阅读)**: 需要提升阅读速度和理解能力
- **Writing (写作)**: 需要练习Task 1图表描述和Task 2议论文写作
- **Speaking (口语)**: 需要练习Part 1-3口语表达

### 仓库用途
- ✅ **练习记录和答案**: 记录做过的真题和模拟题
- ✅ **进度追踪和统计**: 追踪每周/每日的练习进度和成绩变化
- ✅ **学习笔记和词汇**: 整理词汇、语法、写作模板等学习笔记
- ✅ **策略和技巧总结**: 记录考试策略、解题技巧等
- ✅ **参考资料库**: 保存用户上传的学习资料，后续出题测验的素材来源

## Additional Requirements (Confirmed)
- **reference目录**: 用户会上传参考资料，用于后续出题测验的素材来源
- **文件格式支持**: 需要明确LLM支持的素材格式（txt, md, pdf等） - 这是关键信息，需要在设计文档中明确说明
- **材料优先级**: 练习材料优先级必须明确指定 - reference优先于LLM生成和网络查找
- **自动转换需求**: 用户上传的epub和PDF文件需要自动转换为md/txt格式

## Research Findings

### IELTS考试结构参考
- **Listening**: 30分钟, 4个部分, 40题
- **Reading**: 60分钟, 3篇文章, 40题
- **Writing**: 60分钟, Task 1 (图表描述) + Task 2 (议论文, 250词以上)
- **Speaking**: 11-14分钟, 3个部分 (Part 1: 简单问题, Part 2: Cue Card, Part 3: 讨论)

### 学习资源参考
- 研究发现语言学习项目通常采用：模块化结构 + 进度追踪 + 笔记词汇管理
- 标准推荐：初级到中级（5.0→7.0）需要4-6个月，每周15-20小时
- 核心策略：诊断测试 → 针对练习 → 模考评估

### 特殊调整（用户要求）
- **时间压缩**：1个月冲刺（2月6日 - 3月6日）
- **高强度练习**：每周25+小时，总计100-120小时
- **任务单元**：25分钟练习 + 5分钟休息 = 30分钟/单元
- **复习策略**：基于艾宾浩斯遗忘曲线安排复习
- **时间戳要求**：每个任务需要具体时间戳

## Proposed Solution

基于用户需求和研究成果，设计以下仓库结构和skills配置。

### Reference目录支持的素材格式

**推荐格式（优先级从高到低）**:

1. **.md (Markdown)** - 最推荐
   - 易于阅读和编辑
   - 支持格式化（标题、列表、代码块等）
   - LLM处理效果最佳

2. **.txt (纯文本)** - 推荐
   - 最通用的文本格式
   - 处理速度快
   - 适合简单的文章和笔记

3. **.epub (电子书)** - 需要自动转换
   - 适合保存完整教材
   - 需要自动转换为.md格式（pandoc）
   - 转换后自动标记为`.epub-converted.md`

4. **.pdf (PDF文档)** - 需要自动转换
   - 适合保存学术论文、书籍章节
   - 需要自动转换为.md或.txt格式（pandoc）
   - 转换后自动标记为`.pdf-converted.md`或`.pdf-converted.txt`
   - 注意：扫描版PDF效果较差

5. **.csv (CSV表格)** - 推荐（数据类素材）
   - 适合词汇表、统计数据
   - 可用于Reading部分的图表分析训练

6. **.json / .xml** - 特殊用途
   - 适合结构化数据
   - 可用于词汇数据库、题库等

**建议的组织方式**:
```
reference/
├── listening/          # 听力素材
│   ├── transcripts/    # 听力原文（.txt/.md）
│   └── audio-notes/    # 听力笔记（.md）
├── reading/            # 阅读素材
│   ├── articles/       # 学术文章（.md/.pdf）
│   └── vocabulary/     # 词汇表（.csv/.md）
├── writing/            # 写作素材
│   ├── essays/         # 范文（.md）
│   └── templates/      # 模板（.md）
└── speaking/           # 口语素材
    ├── topics/         # 话题卡片（.md）
    └── scripts/        # 口语范文（.md）
```

**注意事项**:
- 优先使用.md和.txt格式，确保LLM能最佳处理
- PDF文件建议先转换为.txt或.md格式
- 音频/视频文件不直接支持，但可保存其transcripts（原文）
- 图片文件不推荐，如需图表描述应使用文字说明

## 4-Week Intensive Sprint Plan (1-Month 5.0→7.0)

### 总体规划
- **时间**: 2025年2月6日 - 2025年3月6日（28天）
- **总时长**: 100-120小时（每周25-30小时）
- **任务单元**: 30分钟（25分钟练习 + 5分钟休息）
- **每周单元数**: 50-60个单元
- **总计单元数**: 200-240个单元

### 时间分配策略（调整后）
| 模块 | 比例 | 每周单元数 | 4周总计 | 说明 |
|------|------|------------|---------|------|
| **Reading** | 35% | 18-21 | 72-84 | 仓库重点，从reference提取 |
| **Writing** | 35% | 18-21 | 72-84 | 仓库重点，从reference提取 |
| **Listening** | 15% | 8-9 | 32-36 | 外部app，仅任务指令 |
| **Speaking** | 10% | 5-6 | 20-24 | 外部app，仅任务指令 |
| **Grammar** | 5% | 2-3 | 10-12 | 仓库记录笔记 |

### 复习策略（艾宾浩斯遗忘曲线）
| 轮次 | 时间间隔 | 复习内容 | 目的 |
|------|----------|----------|------|
| R1 | 1天后 | 当日Reading题型和Writing模板 | 短期记忆巩固 |
| R2 | 3天后 | 重点语法点和写作技巧 | 中期记忆强化 |
| R3 | 7天后 | Reading错误分析和Writing范文复习 | 长期记忆形成 |
| R4 | 14天后 | 综合模考和语法笔记回顾 | 知识整合 |

---

## Material Sourcing Priority & Standards

### 🎯 核心原则
**Reading和Writing使用reference电子书提取练习；Listening/Speating使用外部app；记录语法笔记**

### 📊 模块分工

| 模块 | 方式 | 资料来源 | LLM职责 | 时间占比 |
|------|------|----------|---------|----------|
| **Reading** | ✅ 仓库重点 | Reference电子书 | 提取+轻量生成 | 35% |
| **Writing** | ✅ 仓库重点 | Reference电子书 | 提取+轻量生成 | 35% |
| **Listening** | 外部app | 每日听力app | 仅给出任务指令 | 15% |
| **Speaking** | 外部app | 每日听力app | 仅给出任务指令 | 10% |
| **Grammar** | ✅ 仓库重点 | Reference/练习总结 | 记录笔记 | 5% |
| **Vocabulary** | 用户较好 | 无需重点 | 偶尔记录 | 0% |

### 📊 材料优先级层级（严格顺序）

| 优先级 | 来源 | 使用条件 | 生成策略 |
|--------|------|----------|----------|
| **P1 (首要)** | `reference/` 电子书文件 | **始终优先** | 提取+轻量生成 |
| **P2 (补充)** | LLM基于P1的变体生成 | 仅当需要不同题型时 | 基于P1扩写 |
| **P3 (备用)** | 网络查找 | 仅当P1/P2完全无法满足 | 最后手段 |

### ✅ P1: 从电子书中提取/生成练习材料

#### Reference目录组织（简化）

```
reference/
├── reading-book.md                # 阅读教材电子书
├── writing-book.md                # 写作教材电子书
├── grammar-book.md                # 语法教材电子书
├── essays-collection.md           # 范文集电子书
└── cambridge-tests.md             # 剑桥真题集（Reading/Writing部分）
```

#### 仓库结构（调整后）

```
IELTS_Practice/
├── README.md
├── reference/                    # 📚 电子书（重点）
│   ├── reading-book.md            # 阅读教材
│   ├── writing-book.md            # 写作教材
│   ├── grammar-book.md            # 语法教材
│   ├── essays-collection.md       # 范文集
│   └── cambridge-tests.md         # 真题集
│
├── practice/                     # ✏️ 练习记录
│   ├── reading/
│   │   └── practice-YYYY-MM-DD.md
│   ├── writing/
│   │   ├── task1/
│   │   │   └── essay-YYYY-MM-DD.md
│   │   └── task2/
│   │       └── essay-YYYY-MM-DD.md
│   └── grammar/
│       └── notes-YYYY-MM-DD.md
│
├── notes/                       # 📝 学习笔记
│   ├── grammar/                  # 语法笔记（重点）
│   ├── reading-techniques/       # 阅读技巧
│   └── writing-structures/       # 写作结构
│
└── progress/                     # 📊 进度追踪
    ├── weekly-reports/
    └── stats/
```

#### 提取/生成原则（关键！）
```
✅ DO（必须）:
- 从电子书中提取当日训练所需内容
- 按需生成练习材料（够用即可）
- 生成时间控制在任务总时间的5-10%以内
- 优先提取现成内容（如词汇表、范文、例题）

❌ DON'T（禁止）:
- 提前生成大量练习材料
- 生成超过当日训练需要的内容
- 在生成上花费过多时间
- 生成复杂材料（如完整模拟试卷）
```

#### 提取/生成工作流（按需执行）

```
FOR EACH TASK (即时执行):

Step 1: 确定任务需求
  - 示例: "需要5个environment主题词汇 + 1篇相关文章"

Step 2: 搜索电子书
  - Glob("reference/*.md")
  - 识别相关书籍文件

Step 3: 提取现有内容（优先）
  - Read文件，搜索关键词
  - 提取现成的词汇表、例句、范文
  - 示例: 从vocabulary-book.md提取environment词汇

Step 4: 轻量生成（仅当不够时）
  - 基于提取的内容生成练习题
  - 生成简单题型（填空、选择、短答）
  - 示例: 基于词汇生成配对练习题

Step 5: 验证数量
  - 确保生成量=当日训练需求
  - 不多生成，不少生成

Step 6: 记录来源
  - 记录使用的电子书文件
  - 记录提取/生成的内容范围
```

#### 各模块提取/生成策略

| 模块 | 提取内容 | 生成策略 | 生成上限 |
|------|----------|----------|----------|
| **Reading** | 学术文章段落、题型说明 | 提取段落，生成3-4个简单题目 | 1篇文章+3-4题 |
| **Writing** | 范文、模板、句型 | 提取模板/范文片段，生成1个练习提示 | 1个模板+1个提示 |
| **Grammar** | 语法点、例句 | 提取语法规则，记录到笔记 | 1个语法点+例句 |
| **Listening** | ❌ 不需要提取 | ✅ 外部app完成任务 | 仅任务指令 |
| **Speaking** | ❌ 不需要提取 | ✅ 外部app完成任务 | 仅任务指令 |
| **Vocabulary** | 偶尔提取（用户词汇好） | 仅记录生词 | 偶尔记录 |

#### 提取/生成时间控制

```
任务总时长: 25分钟
生成/提取时间: ≤2分钟 (8%)
实际练习时间: ≥23分钟 (92%)

如果预计生成时间超过2分钟:
→ 简化生成策略（只提取，不复杂生成）
→ 或者使用更简单的题型
→ 绝不延长生成时间
```

#### 轻量生成示例（实际执行时）

**场景1: Reading文章练习**
```
需求: 1篇600词文章 + 3个题目

提取（1.5分钟）:
1. Read(reference/reading-book.md)
2. 搜索适合长度（约600词）的段落
3. 提取段落内容

生成（0.5分钟）:
4. 基于段落生成简单T/F题目
  - 只需要3题，不需要复杂题型

结果: 1篇文章 + 3个T/F题，时间2分钟
```

**场景2: Writing模板练习**
```
需求: 1个Task 2模板 + 练习提示

提取（1分钟）:
1. Read(reference/writing-book.md)
2. 搜索 "template" 或 "structure"
3. 提取现成的模板句型

生成（1分钟）:
4. 生成1个与模板匹配的题目提示
  - 简单的一句话题目即可

结果: 1个模板 + 1个题目，时间2分钟
```

**场景3: Grammar笔记**
```
需求: 1个语法点 + 例句

提取（1.5分钟）:
1. Read(reference/grammar-book.md)
2. 搜索主题（如"passive voice"）
3. 提取语法规则和例句

生成（0.5分钟）:
4. 无需生成，直接记录到notes/grammar/

结果: 1个语法点 + 例句，时间2分钟
```

#### 提取/生成质量标准

```
提取内容标准:
✅ 来自电子书的原文内容（准确）
✅ 符合当前学习水平（初级5.0-6.0）
✅ 与当日训练主题相关

生成内容标准（Reading/Writing）:
✅ 简单、直接、不复杂
✅ 基于提取的内容（不凭空创造）
✅ 易于完成（1篇文章+3-4题 / 1个模板+1个提示）
❌ 不生成长篇阅读材料
❌ 不生成复杂题型（如雅思完整试卷）
❌ 不生成本未学习的语法练习

Listening/Speaking:
✅ 仅给出任务指令，不生成材料
✅ 任务明确指向外部app的具体功能
```

### ✅ P2: 基于P1的变体生成（谨慎使用）

#### 使用条件
- 当P1提取的内容需要不同题型练习时
- 示例: 同一篇文章，今天用T/F题，明天用选择题

#### P2生成约束
```
必须:
- 基于已经提取的内容
- 生成简单变体题型
- 时间控制在1分钟内

禁止:
- 基于电子书其他部分生成（只用已提取部分）
- 生成复杂变体
- 生成过多内容
```

#### P2生成示例
```
场景: 昨天用了1篇environment文章做T/F题
需求: 今天用同样文章做选择题

生成（1分钟）:
1. 使用昨天的文章内容
2. 生成3-4个简单选择题
3. 不需要阅读电子书的其他部分

结果: 1篇文章 + 3选择题，时间1分钟
```

### ✅ P3: 网络查找（最后手段）

#### 使用条件
- 电子书中完全没有相关内容
- 示例: 需要最新的考试趋势信息

#### P3查找约束
```
必须:
- 仅在P1/P2完全无法满足时使用
- 使用官方来源（ielts.org, British Council）
- 快速验证并提取

禁止:
- 替代电子书内容
- 使用非官方来源
- 花费时间过长
```

### 📊 Reference使用统计（轻量级）

每个任务后，简单记录在日志中：
```
Task: [任务名称]
Source: reference/vocabulary-book.md (P1)
Extracted: 10 words from Section 3
Generated: 10 matching questions
Generation Time: 2 min
```

### 🎯 实际执行时的Material Extraction流程

```
FOR EACH TASK (即时执行):

IF task is Reading/Writing/Grammar:

1. [IDENTIFY NEED]
   确定需要什么内容（1篇文章？1个模板？1个语法点？）

2. [SEARCH EBOOK]
   Glob("reference/*.md")
   → 找到相关电子书

3. [EXTRACT CONTENT]
   Read文件 → 搜索关键词 → 提取内容
   → 优先提取现成内容（范文、模板、段落）

4. [GENERATE IF NEEDED]
   IF 提取内容不足:
     生成简单练习（基于提取内容）
     时间控制在1-2分钟

5. [VALIDATE AMOUNT]
   确保生成量=训练需求（不多不少）

6. [RECORD]
   记录来源和提取/生成内容

ELIF task is Listening/Speaking:

1. [IDENTIFY NEED]
   确定训练目标（听力Section 1？口语Part 1？）

2. [GENERATE TASK INSTRUCTION]
   生成明确的任务指令指向外部app

3. [NO EXTRACTION NEEDED]
   无需从reference提取材料

4. [RECORD]
   记录任务指令
```

### 📝 Reference文件格式建议

#### 电子书头部元数据（可选，如果已包含则保留）
```markdown
---
Book: [书名]
Category: [Reading/Writing/Grammar]
Level: [初级/中级]
Source: [原始来源]
Format: [Ebook converted to Markdown]
---
```

### 🎤 Listening/Speaking任务指令示例

#### Listening任务指令（无需材料提取）

```
Task: Listening Practice - Section 1
Source: External App (每日听力)
Instruction:
1. Open 每日听力app
2. Navigate to IELTS Listening → Section 1
3. Select a practice set (conversation)
4. Listen without transcript first
5. Answer all 10 questions
6. Review with transcript
7. Note any unfamiliar vocabulary in notes/ folder
Duration: 25 minutes
```

```
Task: Listening Practice - Section 4
Source: External App (每日听力)
Instruction:
1. Open 每日听力app
2. Navigate to IELTS Listening → Section 4
3. Select an academic lecture topic
4. Practice note-taking while listening
5. Answer all 10 questions
6. Review transcript and compare notes
7. Summarize key points in notes/listening/
Duration: 25 minutes
```

#### Speaking任务指令（无需材料提取）

```
Task: Speaking Practice - Part 1
Source: External App (每日听力)
Instruction:
1. Open 每日听力app
2. Navigate to IELTS Speaking → Part 1
3. Select 5 common topics (family, work, hobbies)
4. Record your answers (use app's recording feature)
5. Listen to your recordings
6. Note improvements needed
7. Re-record at least 2 answers
Duration: 25 minutes
```

```
Task: Speaking Practice - Part 2
Source: External App (每日听力)
Instruction:
1. Open 每日听力app
2. Navigate to IELTS Speaking → Part 2
3. Select a cue card topic
4. Prepare for 1 minute
5. Record 2-minute response
6. Listen and analyze:
   - Fluency
   - Vocabulary range
   - Grammar accuracy
7. Re-record with improvements
Duration: 25 minutes
```

### 📚 Reading/Writing任务示例（需要材料提取）

#### Reading任务示例

```
Task: Reading Practice - True/False/Not Given
Source: reference/reading-book.md (P1)
Instruction:
1. Extract a 600-word passage from reading-book.md
   Search for topic: "environment" or "technology"
2. Generate 3 T/F/NG questions based on passage
   Questions should be simple and direct
3. Read passage (10 minutes)
4. Answer questions (5 minutes)
5. Check answers (5 minutes)
6. Note mistakes in practice/reading/
7. Extract 5 key vocabulary from passage
Duration: 25 minutes
Extraction Time: ≤2 minutes
```

#### Writing任务示例

```
Task: Writing Practice - Task 2 Introduction
Source: reference/writing-book.md (P1)
Instruction:
1. Extract a Task 2 template from writing-book.md
   Search: "introduction" or "opinion essay structure"
2. Generate 1 practice topic based on template
3. Write introduction only (10 minutes)
   Use extracted template structure
4. Self-review (5 minutes)
   Check: thesis statement, paraphrasing
5. Compare with model intro (if available)
6. Save to practice/writing/task2/
Duration: 25 minutes
Extraction Time: ≤2 minutes
```

#### Grammar任务示例

```
Task: Grammar Note - Passive Voice
Source: reference/grammar-book.md (P1)
Instruction:
1. Extract passive voice rules from grammar-book.md
   Search: "passive voice" or "be + past participle"
2. Extract 3-5 example sentences
3. Write brief explanation in own words
4. Note common exceptions
5. Save to notes/grammar/passive-voice-YYYY-MM-DD.md
6. Create 3 practice sentences (if time permits)
Duration: 25 minutes
Extraction Time: ≤2 minutes
```

#### 电子书内容组织（保持原结构）
```markdown
# 第一章: 听力基础

## Section 1: 对话练习

### Example 1
[对话内容...]

### Vocabulary
[词汇表...]

---
[按原书章节继续...]
```

Step 2: 按文件名/标签匹配主题
  - 优先使用与当前练习主题最相关的文件

Step 3: 读取文件内容（Read工具）
  - 提取练习所需内容
  - 记录来源文件名

Step 4: 标注来源
  - 在任务描述中注明: "Source: reference/reading/articles/topic-climate-change.md"
```

#### Reference材料使用率目标
| 技能模块 | Reference使用率目标 | 最低要求 |
|----------|-------------------|----------|
| Listening | 100% | 必须100%来自reference |
| Reading | 100% | 必须100%来自reference |
| Writing | 90% | ≥90%范文/模板来自reference |
| Speaking | 100% | 必须100%话题来自reference |
| Vocabulary | 100% | 必须100%来自reference |

### ✅ P2: LLM生成规范

#### 使用条件（仅满足以下条件之一时使用）
1. **Reference材料不足**: `reference/`目录中相关文件数量 < 3
2. **需要变体练习**: Reference材料已经使用过，需要同主题的变体练习
3. **格式转换**: 需要将reference材料转换为其他格式（如文章→题目）

#### LLM生成约束
- **必须基于reference**: 使用`reference/`中相关材料作为上下文
- **标注基础**: 必须标注"Based on: reference/xxx"
- **风格一致**: 生成的练习风格应与reference材料保持一致
- **避免幻觉**: 不得编造reference中没有的知识点

#### LLM生成示例
```
Task: Generate a new IELTS Reading passage
Constraints:
  - MUST use reference/reading/articles/urbanization.md as base
  - Similar difficulty level
  - Same topic (urbanization)
  - Similar structure (3 paragraphs, 600-700 words)
Output: Generate passage + questions
Note: "Generated based on reference/reading/articles/urbanization.md"
```

### ✅ P3: 网络查找规范

#### 使用条件（仅满足以下条件之一时使用）
1. **Reference完全缺失**: `reference/`目录中无任何相关文件
2. **特定格式需求**: 需要reference中没有的特殊格式（如特定图表类型）
3. **最新趋势**: 需要reference中没有的考试趋势信息

#### 网络查找约束
- **最后手段**: 必须先尝试P1和P2
- **权威来源**: 仅使用官方或知名教育网站（ielts.org, British Council, IDP等）
- **标注来源**: 必须标注网络来源URL
- **质量验证**: 必须验证内容准确性

#### 网络查找示例
```
Task: Find IELTS Listening Section 4 example
Constraints:
  - Check reference/listening/transcripts/ first (EMPTY)
  - Try LLM generation based on academic topics (NOT SUITABLE)
  - Web search from ielts.org ONLY
  - Validate: official Cambridge material
Output: Download + verify + record source
Note: "Source: https://ielts.org/listening-sample"
```

### 🔍 材料来源验证机制

#### 每个任务必须包含的元数据
```markdown
## Material Source Verification
- **Source Type**: [P1/P2/P3]
- **Source File/URL**: [文件路径或URL]
- **Last Used**: [上次使用日期]
- **Usage Count**: [使用次数]
- **Validity**: [有效/过期]
```

#### Reference材料索引
在`reference/`目录下创建索引文件:
```markdown
# Reference Material Index

## Listening
- `transcripts/cambridge-16-test1.md` - Academic lecture, Section 4, 40 questions
- `transcripts/cambridge-16-test2.md` - Campus dialogue, Section 3, 40 questions

## Reading
- `articles/technology-impact.md` - 700 words, Topic: Technology & Society
- `articles/environmental-issues.md` - 650 words, Topic: Environment

## Writing
- `essays/task2-opinion-sample1.md` - Band 8.5, Topic: Education
- `templates/task1-graph-template.md` - Graph description structure
```

### ❌ 禁止行为

1. **禁止跳过P1**: 在有reference材料时直接使用LLM生成
2. **禁止优先P3**: 网络查找不是首选，是最后选项
3. **禁止混合来源**: 同一个练习任务不应混用P1/P2/P3材料
4. **禁止未标注**: 所有材料必须标注来源（P1文件名/P2基础/P3 URL）
5. **禁止低质量**: 即使网络查找的材料，也必须经过质量验证

### 📈 Reference材料使用统计

每次执行任务后，更新`reference/usage-stats.md`:
```markdown
## Reference Usage Statistics

### Week 1 (Feb 6-12)
- **Total Tasks**: 47
- **P1 Usage**: 45 (95.7%) ✅
- **P2 Usage**: 2 (4.3%) ✅
- **P3 Usage**: 0 (0%) ✅

### By Skill
- Listening: 15/15 P1 (100%)
- Reading: 15/15 P1 (100%)
- Writing: 12/12 P1 (100%)
- Speaking: 5/5 P1 (100%)

### Coverage
- reference/listening/transcripts/: 3 files used
- reference/reading/articles/: 5 files used
- reference/writing/essays/: 4 files used
```

### 🎯 执行时的Material Sourcing流程

当执行任何任务时，按以下顺序进行:

```
FOR EACH TASK:

1. [SEARCH P1]
   Glob("reference/{skill}/**/*.{md,txt,}")
   → IF found: SELECT most relevant file
   → IF not found: GOTO STEP 2

2. [VALIDATE P1]
   Read selected file
   → IF suitable: USE as material
   → IF insufficient for task: GOTO STEP 3

3. [GENERATE P2]
   Use P1 file as context
   LLM generate variation/complement
   → IF successful: USE with P1 attribution
   → IF not suitable: GOTO STEP 4

4. [FIND P3]
   Web search (official sources ONLY)
   → IF found: VALIDATE quality
   → IF valid: USE with URL attribution
   → IF invalid: REQUEST USER TO UPLOAD TO REFERENCE

5. [RECORD]
   Update reference/usage-stats.md
   Note source in task metadata
```

### 📝 用户上传Reference材料的规范

#### 推荐上传的材料类型
| 类别 | 格式 | 建议内容 | 文件数目标 |
|------|------|----------|------------|
| Listening | .txt/.md | 听力原文、对话脚本 | 5-10个 |
| Reading | .txt/.md | 学术文章、考试阅读材料 | 10-15个 |
| Writing | .txt/.md | 范文、写作模板、范文分析 | 10-15个 |
| Speaking | .txt/.md | 话题卡片、口语范文 | 8-12个 |
| Vocabulary | .csv/.md | 词汇表、学术词汇 | 5-10个 |

#### 文件命名规范
```
reference/{skill}/{category}/{topic}-{level}-{date}.md

示例:
reference/reading/articles/technology-impact-medium-20250206.md
reference/writing/essays/task2-environment-opinion-band8.5-20250206.md
reference/speaking/topics/travel-experience-cuecard-20250206.md
```

#### 文件内容规范（头部元数据）
```markdown
---
Topic: [主题]
Skill: [Listening/Reading/Writing/Speaking]
Level: [Easy/Medium/Hard]
Word Count: [字数]
Source: [原始来源, 如Cambridge 16 Test 1]
Uploaded: [YYYY-MM-DD]
Tags: [tag1, tag2, tag3]
---

[内容开始...]
```

---

## 🔄 Auto-Conversion Feature for EPUB/PDF Files

### 需求说明

**问题**: 用户上传的参考材料可能是`.epub`或`.pdf`格式，但系统需要`.md`或`.txt`格式才能最佳处理。

**解决方案**: 当用户将`.epub`或`.pdf`文件放入`reference/`目录时，自动转换为`.md`或`.txt`格式。

### 技术方案

**推荐工具**: `pandoc` - 通用文档转换器

**安装命令**:
```bash
# Ubuntu/Debian
sudo apt install pandoc

# macOS
brew install pandoc

# Windows (via Chocolatey)
choco install pandoc
```

**转换规则**:
1. **自动转换**: 检测到`.epub`或`.pdf`文件后，自动转换为`.md`格式
2. **输出命名**:
   - `reading-book.epub` → `reading-book.epub-converted.md`
   - `writing-book.pdf` → `writing-book.pdf-converted.md`
3. **原文件保留**: 转换后保留原始文件（不删除）
4. **Fallback机制**: 如果`.md`转换失败，尝试转换为`.txt`
5. **错误记录**: 转换失败时记录到`reference/conversion-log.md`

**转换命令**:
```bash
# EPUB → Markdown
pandoc "reference/file.epub" -o "reference/file.epub-converted.md"

# PDF → Markdown
pandoc "reference/file.pdf" -o "reference/file.pdf-converted.md"

# PDF → Plain Text (if MD fails)
pandoc "reference/file.pdf" -o "reference/file.pdf-converted.txt" -t plain
```

### 自动化脚本示例

创建`scripts/auto-convert.sh`:

```bash
#!/bin/bash
# auto-convert.sh - 自动转换reference/目录中的epub和pdf文件

cd /mnt/d/MyDocs/IELTS_Practice/reference

# 创建转换日志
echo "# Conversion Log - $(date '+%Y-%m-%d %H:%M:%S')" > conversion-log.md
echo "" >> conversion-log.md
echo "## Successes" >> conversion-log.md
echo "" >> conversion-log.md

# 转换所有.epub文件
for epub in *.epub; do
  if [ -f "$epub" ] && [ ! -f "${epub}.converted.md" ]; then
    echo "Converting $epub to Markdown..." | tee -a conversion-log.md
    pandoc "$epub" -o "${epub}.converted.md"
    if [ $? -eq 0 ]; then
      echo "✅ $epub → ${epub}.converted.md" | tee -a conversion-log.md
    else
      echo "❌ Failed to convert $epub" | tee -a conversion-log.md
    fi
  fi
done

# 转换所有.pdf文件
for pdf in *.pdf; do
  if [ -f "$pdf" ] && [ ! -f "${pdf}.converted.md" ]; then
    echo "Converting $pdf to Markdown..." | tee -a conversion-log.md
    pandoc "$pdf" -o "${pdf}.converted.md"
    if [ $? -eq 0 ]; then
      echo "✅ $pdf → ${pdf}.converted.md" | tee -a conversion-log.md
    else
      # Fallback to plain text
      echo "Trying plain text conversion for $pdf..." | tee -a conversion-log.md
      pandoc "$pdf" -o "${pdf}.converted.txt" -t plain
      if [ $? -eq 0 ]; then
        echo "✅ $pdf → ${pdf}.converted.txt (plain text fallback)" | tee -a conversion-log.md
      else
        echo "❌ Failed to convert $pdf (both MD and TXT failed)" | tee -a conversion-log.md
      fi
    fi
  fi
done

echo "" >> conversion-log.md
echo "Conversion completed at $(date '+%Y-%m-%d %H:%M:%S')" >> conversion-log.md
```

### 使用方式

```bash
# 用户上传epub/pdf文件后，运行一次转换脚本
bash scripts/auto-convert.sh

# 查看转换日志
cat reference/conversion-log.md
```

### 转换状态追踪

创建`reference/conversion-status.md`:

```markdown
# Conversion Status

## 最近转换记录

| 原始文件 | 转换后文件 | 状态 | 转换时间 | 备注 |
|----------|------------|------|----------|------|
| reading-book.epub | reading-book.epub-converted.md | ✅ 成功 | 2025-02-06 18:00 | - |
| writing-book.pdf | writing-book.pdf-converted.md | ✅ 成功 | 2025-02-06 18:01 | - |
| old-grammar.pdf | old-grammar.pdf-converted.txt | ⚠️ 仅TXT | 2025-02-06 18:02 | MD转换失败 |

## 转换错误

| 文件 | 错误时间 | 错误信息 | 处理方式 |
|------|----------|----------|----------|
| damaged.pdf | 2025-02-05 | Pandoc timeout (文件过大) | 建议手动转换 |
```

### 配置选项

**优先级顺序**:
1. 优先转换为`.md`格式
2. 如果MD转换失败，fallback到`.txt`格式
3. 只转换一次（避免重复转换，通过检查`.converted.md`是否存在）

**性能考虑**:
- 转换时间: 通常<1秒/文件（小文件），<30秒/文件（大书籍）
- 文件大小限制: 建议单个文件<50MB

**错误处理**:
- Pandoc未安装: 提示用户安装
- 转换超时: 记录日志，建议手动转换
- 文件损坏: 记录日志，跳过该文件
