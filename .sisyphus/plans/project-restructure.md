# 项目结构重构计划

## TL;DR

> **快速摘要**：全面重构 IELTS_Practice 项目文件结构，清理根目录分散的笔记文件，建立清晰的目录层级。
>
> **交付物**：
> - docs/ 目录（项目文档集中）
> - practice/daily/ 目录（按日期分组的每日记录）
> - notes/ 结构优化（拼写修正、合适分类）
> - 更新的 README.md（反映实际结构）
>
> **预估工作量**：Large
> **并行执行**：YES - 6 waves
> **关键路径**：Wave 1 → Wave 2 → Wave 3 → Wave 4 → Wave 5 → Wave 6

---

## Context

### Original Request
用户希望全面重构 IELTS_Practice 项目的文件结构，整理根目录分散的笔记文件，减少认知负荷。选择了"全面重构方案（方案B）"。

### Interview Summary

**关键讨论**：
- **方案选择**：用户选择"全面重构方案（方案B）"
- **目标**：清理根目录，建立清晰的目录层级，减少认知负荷
- **探索任务**：3个探索任务收集了完整信息（wikilink依赖、practice结构、notes结构）
- **Metis 审查**：识别了6个关键问题并提供了详细的 guardrails

**用户决策**：
1. **文件命名**：统一命名格式（重命名为 `YYYY-MM-DD-{topic}.md`）
2. **空目录处理**：部分保留（保留 writing-structures/，删除其他空目录）
3. **验证策略**：仅文件存在检查（ls/tree 验证）
4. **提交策略**：按逻辑分组（docs/、practice/daily/、notes修正、README更新分4个提交）
5. **回滚策略**：Git revert（无需额外准备）

**Research Findings**:
- Wikilink 分析：3个目标文件无外部依赖，移动安全
- Practice/ 结构：79个文件，24个需要移动，命名规范一致
- Notes/ 结构：`listenning/` 拼写错误，`writing-structures/` 存在但为空
- README.md 不符：描述 `modules/`、`data/`，实际是 `notes/`、`practice/`、`progress/`

### Metis Review

**识别的问题（已解决）**：
- ✅ 文件命名约定：用户决定统一格式（YYYY-MM-DD-{topic}.md）
- ✅ 空目录处理：用户决定部分保留（writing-structures/）
- ✅ 验证策略：用户决定仅文件存在检查
- ✅ 提交策略：用户决定按逻辑分组（4个提交）
- ✅ 回滚策略：用户决定使用 Git revert

**Guardrails（已应用）**：
- 内容保留保护：不修改文件内容
- 目录结构冻结：仅创建 docs/、daily/、listening/
- 原子操作保护：每次逻辑分组一个 git 提交
- 范围蔓延保护：仅移动明确列出的文件

---

## Work Objectives

### Core Objective
全面重构 IELTS_Practice 项目文件结构，清理根目录，建立清晰的目录层级，减少认知负荷。

### Concrete Deliverables
- `docs/` 目录（6个项目文档）
- `practice/daily/` 目录（按日期分组的24个文件）
- `notes/summaries/` 目录（学习总结）
- `notes/tech-notes/` 目录（技术笔记）
- 修正后的 `notes/listening/`（原 listenning/）
- 更新的 `README.md`（反映实际目录结构）

### Definition of Done
- [x] 根目录只保留 Python 脚本文件
- [x] 所有项目文档在 `docs/` 目录
- [x] 所有 daily 文件在 `practice/daily/` 按日期分组
- [x] 所有笔记文件在合适的 `notes/` 子目录
- [x] `notes/listenning/` 重命名为 `listening/`
- [x] README.md 准确描述实际目录结构
- [x] git 提交历史清晰（4个逻辑分组提交）

### Must Have
- 清理根目录，仅保留脚本文件
- 移动所有明确列出的文件
- 按用户决策重命名24个 daily 文件
- 修正 `listenning/` 拼写错误
- 更新 README.md 的目录结构描述

### Must NOT Have (Guardrails)
- 不修改任何文件内容
- 不创建额外目录（仅 docs/、daily/、listening/、summaries/、tech-notes/）
- 不移动根目录的 Python 脚本文件（保留在原位置）
- 不更新 README.md 的其他部分（仅目录结构部分）
- 不删除 `notes/writing-structures/`（用户决定保留）

---

## Verification Strategy

### Test Decision
- **Infrastructure exists**: YES (Git)
- **Automated tests**: NO
- **Verification method**: File existence check using ls/tree commands

### QA Policy
每个任务包含可执行的验证场景。证据保存到 `.sisyphus/evidence/task-{N}-{scenario-slug}.{ext}`。

- **目录结构验证**：使用 `tree -L 2` 和 `ls`
- **文件移动验证**：使用 `git status` 和 `git diff`
- **Wikilink 验证**：由于目标文件无外部依赖，无需验证

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1（立即开始 - 基础结构创建）：
├── Task 1: 创建 docs/ 目录 [quick]
├── Task 2: 创建 practice/daily/ 结构 [quick]
├── Task 3: 创建 notes/summaries/ 目录 [quick]
├── Task 4: 创建 notes/tech-notes/ 目录 [quick]
└── Task 5: 创建 practice/daily/ 的日期子目录 [quick]

Wave 2（After Wave 1 - 移动项目文档）：
└── Task 6: 移动6个项目文档到 docs/ [unspecified-high]

Wave 3（After Wave 2 - 移动 practice 文件）：
├── Task 7: 重命名并移动24个daily文件到 practice/daily/ [deep]
├── Task 8: 验证 practice/daily/ 结构 [quick]
└── Task 9: 删除 practice/ 根目录的旧 daily 文件 [quick]

Wave 4（After Wave 3 - 移动根目录笔记）：
├── Task 10: 移动 ielts-verb-phrases-idioms-2026-03-15.md 到 notes/grammar/ [quick]
├── Task 11: 移动 week-1-learning-summary-2026-03-15.md 到 notes/summaries/ [quick]
└── Task 12: 移动 什么算高质量Vibe Coding.md 到 notes/tech-notes/ [quick]

Wave 5（After Wave 4 - 修正和清理）：
├── Task 13: 修正 notes/listenning/ 拼写错误 → notes/listening/ [quick]
├── Task 14: 删除空目录（grammar, reading-techniques） [quick]
└── Task 15: 更新 README.md 的目录结构部分 [unspecified-high]

Wave 6（After Wave 5 - 最终验证）：
├── Task 16: 验证根目录清理 [quick]
├── Task 17: 验证 docs/ 结构 [quick]
├── Task 18: 验证 practice/daily/ 结构 [quick]
├── Task 19: 验证 notes/ 结构 [quick]
└── Task 20: Git 提交和清理 [git]

Critical Path: Task 1 → Task 2 → Task 5 → Task 7 → Task 8 → Task 15 → Task 16-20
Parallel Speedup: ~70% faster than sequential
Max Concurrent: 5 (Wave 1)
```

### Dependency Matrix (FULL)

- **1-5**: — — 6-9, 2
- **6**: — 2
- **7**: 5 — 8-9, 3
- **8**: 7 — 2
- **9**: 7 — 2
- **10**: — — 3, 4
- **11**: — — 3, 4
- **12**: — — 3, 4
- **13**: — — 14, 4, 5
- **14**: — — 15, 4
- **15**: — — 16-20, 6
- **16-20**: 7, 8, 9, 13, 14, 15 — —

### Agent Dispatch Summary

- **1**: **5** — T1-T5 → 全部 `quick`
- **2**: **1** — T6 → `unspecified-high`
- **3**: **3** — T7-T9 → T7, T8: `deep`, T9: `quick`
- **4**: **3** — T10-T12 → T10-T12: 全部 `quick`
- **5**: **1** — T13-T14: T13: `quick`, T14: `quick`
- **6**: **1** — T15 → `unspecified-high`
- **FINAL**: **5** — T16-T20: T16-T19: `quick`, T20: `git`

---

## TODOs

- [x] 1. 创建 docs/ 目录

  **What to do**:
  - 在项目根目录创建 `docs/` 目录
  - 目录用于存放项目文档（6个.md文件）

  **Must NOT do**:
  - 不创建其他目录

  **Recommended Agent Profile**:
  > Select category + skills based on task domain. Justify each choice.
  - **Category**: `quick`
    - Reason: 简单的目录创建任务，快速且无风险
  - **Skills**: []
    - No special skills needed for directory creation

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 2, 3, 4, 5)
  - **Blocks**: Task 6
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [x] Directory created: `docs/`
  - [x] Command executed: `mkdir docs/`

  **QA Scenarios (MANDATORY):**

  \`\`\`
  Scenario: 验证 docs/ 目录创建成功
    Tool: Bash
    Preconditions: 项目根目录存在
    Steps:
      1. 运行 `ls docs/`
      2. 验证命令退出码为 0
    Expected Result: docs/ 目录存在且为空
    Failure Indicators: 命令失败（退出码非0）或目录不存在
    Evidence: .sisyphus/evidence/task-1-dir-creation.txt
  \`\`\`

  **Commit**: NO (groups with 2-5)
  - Message: None (wait for file moves)

- [x] 2. 创建 practice/daily/ 结构

  **What to do**:
  - 在 `practice/` 目录下创建 `daily/` 目录
  - daily/ 用于存放按日期分组的每日记录文件

  **Must NOT do**:
  - 不移动或修改 practice/ 下的现有文件

  **Recommended Agent Profile**:
  > Select category + skills based on task domain. Justify each choice.
  - **Category**: `quick`
    - Reason: 简单的目录创建任务
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 3, 4, 5)
  - **Blocks**: Task 7
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [x] Directory created: `practice/daily/`
  - [x] Command executed: `mkdir practice/daily/`

  **QA Scenarios (MANDATORY):**

  \`\`\`
  Scenario: 验证 practice/daily/ 目录创建成功
    Tool: Bash
    Preconditions: practice/ 目录存在
    Steps:
      1. 运行 `ls practice/daily/`
      2. 验证命令退出码为 0
    Expected Result: practice/daily/ 目录存在且为空
    Failure Indicators: 命令失败或目录不存在
    Evidence: .sisyphus/evidence/task-2-daily-creation.txt
  \`\`\`

  **Commit**: NO (groups with 1, 3-5)
  - Message: None (wait for file moves)

- [x] 3. 创建 notes/summaries/ 目录

  **What to do**:
  - 在 `notes/` 目录下创建 `summaries/` 目录
  - summaries/ 用于存放学习总结文件（如 week-1-learning-summary）

  **Must NOT do**:
  - 不创建其他 notes/ 子目录

  **Recommended Agent Profile**:
  > Select category + skills based on task domain. Justify each choice.
  - **Category**: `quick`
    - Reason: 简单的目录创建任务
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 4, 5)
  - **Blocks**: Task 11
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [x] Directory created: `notes/summaries/`
  - [x] Command executed: `mkdir notes/summaries/`

  **QA Scenarios (MANDATORY):**

  \`\`\`
  Scenario: 验证 notes/summaries/ 目录创建成功
    Tool: Bash
    Preconditions: notes/ 目录存在
    Steps:
      1. 运行 `ls notes/summaries/`
      2. 验证命令退出码为 0
    Expected Result: notes/summaries/ 目录存在且为空
    Failure Indicators: 命令失败或目录不存在
    Evidence: .sisyphus/evidence/task-3-summaries-creation.txt
  \`\`\`

  **Commit**: NO (groups with 1-2, 4-5)
  - Message: None (wait for file moves)

- [x] 4. 创建 notes/tech-notes/ 目录

  **What to do**:
  - 在 `notes/` 目录下创建 `tech-notes/` 目录
  - tech-notes/ 用于存放技术笔记文件（如 Vibe Coding 相关）

  **Must NOT do**:
  - 不创建其他 notes/ 子目录

  **Recommended Agent Profile**:
  > Select category + skills based on task domain. Justify each choice.
  - **Category**: `quick`
    - Reason: 简单的目录创建任务
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1-3, 5)
  - **Blocks**: Task 12
  - **Blocked By**: None

  **Acceptance Criteria**:
  - [x] Directory created: `notes/tech-notes/`
  - [x] Command executed: `mkdir notes/tech-notes/`

  **QA Scenarios (MANDATORY):**

  \`\`\`
  Scenario: 验证 notes/tech-notes/ 目录创建成功
    Tool: Bash
    Preconditions: notes/ 目录存在
    Steps:
      1. 运行 `ls notes/tech-notes/`
      2. 验证命令退出码为 0
    Expected Result: notes/tech-notes/ 目录存在且为空
    Failure Indicators: 命令失败或目录不存在
    Evidence: .sisyphus/evidence/task-4-technotes-creation.txt
  \`\`\`

  **Commit**: NO (groups with 1-4)
  - Message: None (wait for file moves)

- [x] 5. 创建 practice/daily/ 的日期子目录

  **What to do**:
  - 在 `practice/daily/` 下创建日期子目录（从daily文件中提取日期）
  - 识别的唯一日期：2026-02-09, 2026-02-10, 2026-02-11, 2026-02-12, 2026-02-13, 2026-02-18, 2026-02-19, 2026-02-20, 2026-02-28, 2026-03-12, 2026-03-13, 2026-03-15
  - 为每个日期创建子目录

  **Must NOT do**:
  - 不移动或修改现有文件
  - 不创建不必要的子目录

  **Recommended Agent Profile**:
  > Select category + skills based on task domain. Justify each choice.
  - **Category**: `quick`
    - Reason: 批量目录创建任务，简单且无风险
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Wave 1 (after Tasks 1-4 complete)
  - **Blocks**: Task 7
  - **Blocked By**: Tasks 1-4

  **References**:

  **Pattern References** (existing code to follow):
  - 无相关模式

  **API/Type References** (contracts to implement against):
  - 无

  **External References** (libraries and frameworks):
  - 无

  **Acceptance Criteria**:
  - [x] 10个日期子目录已创建（2026-02-09 到 2026-03-15）
  - [x] 命令执行：`mkdir practice/daily/YYYY-MM-DD` x10

  **QA Scenarios (MANDATORY):**

  \`\`\`
  Scenario: 验证所有日期子目录创建成功
    Tool: Bash
    Preconditions: practice/daily/ 目录存在
    Steps:
      1. 运行 `ls practice/daily/`
      2. 统计子目录数量（期望：10个）
      3. 验证命令退出码为 0
    Expected Result: 10个日期子目录存在
    Failure Indicators: 子目录数量不是10个或命令失败
    Evidence: .sisyphus/evidence/task-5-date-dirs-creation.txt
  \`\`\`

  **Commit**: NO (groups with Task 6)
  - Message: None (wait for file moves)

- [x] 6. 移动项目文档到 docs/ 目录

  **What to do**:
  - 移动以下6个项目文档从根目录到 `docs/`：
    - `README.md` → `docs/README.md`
    - `IELTS_ANNOTATOR_GUIDE.md` → `docs/IELTS_ANNOTATOR_GUIDE.md`
    - `MATERIAL-EXTRACTION-STANDARDS.md` → `docs/MATERIAL-EXTRACTION-STANDARDS.md`
    - `REVIEW-STRATEGY.md` → `docs/REVIEW-STRATEGY.md`
    - `VALIDATION-REPORT.md` → `docs/VALIDATION-REPORT.md`
    - `TOOLS_SUMMARY.md` → `docs/TOOLS_SUMMARY.md`

  **Must NOT do**:
  - 不移动 Python 脚本文件（*.py）
  - 不移动学习笔记文件（ielts-verb-phrases-idioms-2026-03-15.md, week-1-learning-summary-2026-03-15.md, 什么算高质量Vibe Coding.md）

  **Recommended Agent Profile**:
  > Select category + skills based on task domain. Justify each choice.
  - **Category**: `unspecified-high`
    - Reason: 多文件移动任务，需要确保文件完整性
  - **Skills**: []
    - 使用基本 bash 命令进行文件移动

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Wave 2 (after Wave 1 complete)
  - **Blocks**: Task 7-12
  - **Blocked By**: Task 1-5

  **References**:

  **Pattern References** (existing code to follow):
  - 无相关模式

  **API/Type References** (contracts to implement against):
  - 无

  **External References** (libraries and frameworks):
  - 无

  **Acceptance Criteria**:
  - [x] 6个项目文档已移动到 `docs/` 目录
  - [x] 根目录不再有这6个.md文件
  - [x] Git 状态显示6个文件已移动

  **QA Scenarios (MANDATORY):**

  \`\`\`
  Scenario: 验证所有项目文档移动成功
    Tool: Bash
    Preconditions: docs/ 目录存在，6个项目文档在根目录
    Steps:
      1. 运行 `ls docs/*.md | wc -l`
      2. 验证输出为 6 个文件
      3. 运行 `ls *.md | wc -l` 确认根目录不再有这些文件
    Expected Result: docs/ 有6个文件，根目录不再有这些文件
    Failure Indicators: 文件数量不是6个或根目录仍有项目文档
    Evidence: .sisyphus/evidence/task-6-docs-move.txt
  \`\`\`

  **Commit**: YES
  - Message: `docs(reorg): create docs/ and move project documentation`
  - Files: docs/*.md
  - Pre-commit: `ls docs/*.md | wc -l`
 
- [x] 7. 重命名并移动 practice/ 的 daily 文件

  **What to do**:
  - 将 practice/ 根目录的24个 daily 文件重命名并移动到 `practice/daily/` 对应日期子目录
  - 重命名规则：`2026-XX-XX-ielts-sync.md` → `YYYY-MM-DD-sync.md`
  - 重命名规则：`2026-XX-XX-ielts-noon-card.md` → `YYYY-MM-DD-noon-card.md`
  - 重命名规则：`2026-XX-XX-ielts-evening-card.md` → `YYYY-MM-DD-evening-card.md`
  - 按日期分组到对应子目录（2026-02-09/ → practice/daily/2026-02-09/）

  **文件清单**：
  - 2026-02-09: sync.md, noon-card.md, evening-card.md
  - 2026-02-10: sync.md, noon-card.md, evening-card.md
  - 2026-02-11: sync.md, noon-card.md
  - 2026-02-12: sync.md, evening-card.md
  - 2026-02-13: sync.md
  - 2026-02-18: sync.md, noon-card.md, evening-card.md
  - 2026-02-19: sync.md, noon-card.md, evening-card.md
  - 2026-02-20: evening-card.md
  - 2026-02-28: noon-card.md
  - 2026-03-12: evening-card.md
  - 2026-03-13: sync.md, noon-card.md, evening-card.md
  - 2026-03-15: sync.md, noon-card.md

  **Must NOT do**:
  - 不修改文件内容
  - 不移动 practice/reading/ 或 practice/writing/ 的文件
  - 不移动 Python 脚本文件

  **Recommended Agent Profile**:
  > Select category + skills based on task domain. Justify each choice.
  - **Category**: `deep`
    - Reason: 批量文件重命名和移动任务，需要精确的文件操作
  - **Skills**: []
    - 使用 bash 脚本或命令行进行批量操作

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Wave 3 (after Wave 2 complete)
  - **Blocks**: Task 8-9
  - **Blocked By**: Tasks 1-6

  **References**:

  **Pattern References** (existing code to follow):
  - 无相关模式（新目录结构）

  **API/Type References** (contracts to implement against):
  - 无

  **External References** (libraries and frameworks):
  - 无

  **Acceptance Criteria**:
  - [x] 24个 daily 文件已重命名并移动到 practice/daily/
  - [x] 文件命名符合 YYYY-MM-DD-{topic}.md 格式
  - [x] practice/ 根目录不再有这些文件
  - [x] Git 状态显示24个文件已移动

  **QA Scenarios (MANDATORY):**

  \`\`\`
  Scenario: 验证所有 daily 文件重命名和移动成功
    Tool: Bash
    Preconditions: practice/daily/ 有10个日期子目录，24个daily文件在 practice/ 根目录
    Steps:
      1. 运行 `ls practice/daily/*/*.md | wc -l`
      2. 验证输出为 24 个文件
      3. 运行 `ls practice/*daily*.md | wc -l` 验证根目录不再有这些文件
      4. 随机抽查文件命名（如 `ls practice/daily/2026-03-15/sync.md`）
    Expected Result: practice/daily/ 有24个文件，practice/ 根目录不再有daily文件
    Failure Indicators: 文件数量不是24个或根目录仍有daily文件
    Evidence: .sisyphus/evidence/task-7-daily-move.txt
  \`\`\`

  **Commit**: YES
  - Message: `practice(reorg): create practice/daily/ and reorganize daily files`
  - Files: practice/daily/*/*.md
  - Pre-commit: `ls practice/daily/*/*.md | wc -l`

- [x] 8. 验证 practice/daily/ 结构

  **What to do**:
  - 验证 practice/daily/ 目录结构符合预期
  - 确认10个日期子目录存在
  - 确认每个子目录包含正确的文件（sync.md, noon-card.md, evening-card.md）

  **Must NOT do**:
  - 不修改或移动任何文件

  **Recommended Agent Profile**:
  > Select category + skills based on task domain. Justify each choice.
  - **Category**: `quick`
    - Reason: 简单的目录结构验证任务
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Task 9)
  - **Blocks**: Task 9, Task 10-12
  - **Blocked By**: Task 7

  **Acceptance Criteria**:
  - [x] 10个日期子目录存在（2026-02-09 到 2026-03-15）
  - [x] 每个子目录包含正确的文件
  - [x] `tree practice/daily/` 输出符合预期结构

  **QA Scenarios (MANDATORY):**

  \`\`\`
  Scenario: 验证 practice/daily/ 目录结构
    Tool: Bash
    Preconditions: practice/daily/ 目录存在
    Steps:
      1. 运行 `tree practice/daily/ -L 2`
      2. 验证输出显示10个日期子目录
      3. 运行 `ls practice/daily/2026-03-15/` 验证包含3个文件
    Expected Result: 目录结构清晰，10个日期子目录，每个包含正确文件
    Failure Indicators: 子目录数量不是10个或文件数量不正确
    Evidence: .sisyphus/evidence/task-8-daily-verify.txt
  \`\`\`

  **Commit**: NO (groups with Task 7)
  - Message: None (already committed with Task 7)

- [x] 9. 删除 practice/ 根目录的旧 daily 文件

  **What to do**:
  - 删除 practice/ 根目录的24个旧 daily 文件
  - 由于已移动到 practice/daily/ 子目录，这些旧文件应被删除
  - 检查 practice/ 根目录是否还有残留的 daily 文件

  **Must NOT do**:
  - 不删除其他文件（如 README.md, grammar/ 等）
  - 不删除 reading/ 或 writing/ 的文件

  **Recommended Agent Profile**:
  > Select category + skills based on task domain. Justify each choice.
  - **Category**: `quick`
    - Reason: 简单的文件删除任务
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Task 8)
  - **Blocks**: Task 10-12
  - **Blocked By**: Task 7, 8

  **Acceptance Criteria**:
  - [x] practice/ 根目录不再有 daily 文件（*daily*.md）
  - [x] Git 状态显示24个文件已删除
  - [x] 只保留 README.md 和子目录（reading, writing, grammar, daily）

  **QA Scenarios (MANDATORY):**

  \`\`\`
  Scenario: 验证旧 daily 文件已删除
    Tool: Bash
    Preconditions: 24个daily文件已移动到 practice/daily/
    Steps:
      1. 运行 `ls practice/*daily*.md`
      2. 验证输出为 0 或空
      3. 运行 `ls practice/` 确认只有子目录和 README.md
    Expected Result: practice/ 根目录不再有 daily 文件
    Failure Indicators: 仍有 daily 文件存在
    Evidence: .sisyphus/evidence/task-9-cleanup-old.txt
  \`\`\`

  **Commit**: YES
  - Message: `practice(cleanup): remove old daily files from practice root`
  - Files: practice/*daily*.md (deletion)
  - Pre-commit: `ls practice/*daily*.md`
 
- [x] 10. 移动 ielts-verb-phrases-idioms-2026-03-15.md 到 notes/grammar/

  **What to do**:
  - 移动根目录的 `ielts-verb-phrases-idioms-2026-03-15.md` 到 `notes/grammar/`
  - 该文件包含 IELTS 写作动词短语与习语笔记

  **Must NOT do**:
  - 不修改文件内容
  - 不移动其他根目录文件

  **Recommended Agent Profile**:
  > Select category + skills based on task domain. Justify each choice.
  - **Category**: `quick`
    - Reason: 简单的文件移动任务
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 4 (with Tasks 11, 11, 12)
  - **Blocks**: Task 13-15
  - **Blocked By**: Tasks 3, 5

  **Acceptance Criteria**:
  - [x] 文件已移动到 `notes/grammar/`
  - [x] 根目录不再有该文件
  - [x] Git 状态显示文件已移动

  **QA Scenarios (MANDATORY):**

  \`\`\`
  Scenario: 验证 ielts-verb-phrases-idioms 文件移动成功
    Tool: Bash
    Preconditions: notes/grammar/ 目录存在，文件在根目录
    Steps:
      1. 运行 `ls notes/grammar/ielts-verb-phrases-idioms-2026-03-15.md`
      2. 验证文件存在
      3. 运行 `ls ielts-verb-phrases-idioms-2026-03-15.md` 验证根目录不再有
    Expected Result: 文件在 notes/grammar/ 目录，不在根目录
    Failure Indicators: 文件不存在于目标位置或仍在根目录
    Evidence: .sisyphus/evidence/task-10-verb-move.txt
  \`\`\`

  **Commit**: NO (groups with Tasks 11, 12)
  - Message: None (wait for all Wave 4 tasks)

- [x] 11. 移动 week-1-learning-summary-2026-03-15.md 到 notes/summaries/

  **What to do**:
  - 移动根目录的 `week-1-learning-summary-2026-03-15.md` 到 `notes/summaries/`
  - 该文件包含一周学习精华总结

  **Must NOT do**:
  - 不修改文件内容
  - 不移动其他根目录文件

  **Recommended Agent Profile**:
  > Select category + skills based on task domain. Justify each choice.
  - **Category**: `quick`
    - Reason: 简单的文件移动任务
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 4 (with Tasks 10, 12)
  - **Blocks**: Task 13-15
  - **Blocked By**: Tasks 3, 10

  **Acceptance Criteria**:
  - [x] 文件已移动到 `notes/summaries/`
  - [x] 根目录不再有该文件
  - [x] Git 状态显示文件已移动

  **QA Scenarios (MANDATORY):**

  \`\`\`
  Scenario: 验证 week-1-learning-summary 文件移动成功
    Tool: Bash
    Preconditions: notes/summaries/ 目录存在，文件在根目录
    Steps:
      1. 运行 `ls notes/summaries/week-1-learning-summary-2026-03-15.md`
      2. 验证文件存在
      3. 运行 `ls week-1-learning-summary-2026-03-15.md` 验证根目录不再有
    Expected Result: 文件在 notes/summaries/ 目录，不在根目录
    Failure Indicators: 文件不存在于目标位置或仍在根目录
    Evidence: .sisyphus/evidence/task-11-summary-move.txt
  \`\`\`

  **Commit**: NO (groups with Tasks 10, 12)
  - Message: None (wait for all Wave 4 tasks)

- [x] 12. 移动 什么算高质量Vibe Coding.md 到 notes/tech-notes/

  **What to do**:
  - 移动根目录的 `什么算高质量Vibe Coding.md` 到 `notes/tech-notes/`
  - 该文件包含 Vibe Coding 方法论（技术笔记）

  **Must NOT do**:
  - 不修改文件内容
  - 不移动其他根目录文件

  **Recommended Agent Profile**:
  > Select category + skills based on task domain. Justify each choice.
  - **Category**: `quick`
    - Reason: 简单的文件移动任务
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 4 (with Tasks 10, 11)
  - **Blocks**: Task 13-15
  - **Blocked By**: Tasks 3, 10, 11

  **Acceptance Criteria**:
  - [x] 文件已移动到 `notes/tech-notes/`
  - [x] 根目录不再有该文件
  - [x] Git 状态显示文件已移动

  **QA Scenarios (MANDATORY):**

  \`\`\`
  Scenario: 验证 vibe-coding 文件移动成功
    Tool: Bash
    Preconditions: notes/tech-notes/ 目录存在，文件在根目录
    Steps:
      1. 运行 `ls notes/tech-notes/什么算高质量Vibe Coding.md`
      2. 验证文件存在
      3. 运行 `ls 什么算高质量Vibe Coding.md` 验证根目录不再有
    Expected Result: 文件在 notes/tech-notes/ 目录，不在根目录
    Failure Indicators: 文件不存在于目标位置或仍在根目录
    Evidence: .sisyphus/evidence/task-12-vibe-move.txt
  \`\`\`

  **Commit**: YES
  - Message: `notes(reorg): move root notes to appropriate subdirectories`
  - Files: notes/grammar/ielts-verb-phrases-idioms-2026-03-15.md, notes/summaries/week-1-learning-summary-2026-03-15.md, notes/tech-notes/什么算高质量Vibe Coding.md
  - Pre-commit: `ls notes/grammar/ notes/summaries/ notes/tech-notes/`
 
- [x] 13. 修正 notes/listenning/ 拼写错误

  **What to do**:
  - 将 `notes/listenning/` 重命名为 `notes/listening/`
  - 修正拼写错误（listenning → listening）

  **Must NOT do**:
  - 不修改目录内容
  - 不移动或删除目录内的文件

  **Recommended Agent Profile**:
  > Select category + skills based on task domain. Justify each choice.
  - **Category**: `quick`
    - Reason: 简单的目录重命名任务
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 5 (with Tasks 14, 15)
  - **Blocks**: Task 16-20
  - **Blocked By**: Task 12

  **Acceptance Criteria**:
  - [x] `notes/listening/` 目录存在
  - [x] `notes/listenning/` 目录不再存在
  - [x] Git 状态显示目录重命名

  **QA Scenarios (MANDATORY):**

  \`\`\`
  Scenario: 验证 listenning → listening 重命名成功
    Tool: Bash
    Preconditions: notes/listenning/ 目录存在，包含2个中文文件
    Steps:
      1. 运行 `ls notes/listening/` 验证目录存在
      2. 运行 `ls notes/listenning/` 验证旧目录不存在
      3. 运行 `ls notes/listening/雅思听力主题关键词 Top 100（按场景分类）.md` 验证文件已移动
    Expected Result: notes/listening/ 目录存在，包含2个文件，notes/listenning/ 不存在
    Failure Indicators: 重命名失败或文件未正确迁移
    Evidence: .sisyphus/evidence/task-13-typo-fix.txt
  \`\`\`

  **Commit**: YES
  - Message: `notes(typo): fix listenning → listening spelling error`
  - Files: notes/listenning/ (rename to listening/)

- [x] 14. 删除空目录

  **What to do**:
  - 删除以下空目录：
    - `notes/grammar/` （空目录）
    - `notes/reading-techniques/` （空目录）
    - `practice/grammar/` （空目录）
  - 保留 `notes/writing-structures/`（用户决定保留）

  **Must NOT do**:
  - 不删除非空目录
  - 不删除任何文件

  **Recommended Agent Profile**:
  > Select category + skills based on task domain. Justify each choice.
  - **Category**: `quick`
    - Reason: 简单的目录删除任务
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 5 (with Task 15)
  - **Blocks**: Task 16-20
  - **Blocked By**: Task 13

  **Acceptance Criteria**:
  - [x] `notes/grammar/` 已删除
  - [x] `notes/reading-techniques/` 已删除
  - [x] `practice/grammar/` 已删除
  - [x] `notes/writing-structures/` 仍然存在（保留）
  - [x] Git 状态显示3个目录已删除

  **QA Scenarios (MANDATORY):**

  \`\`\`
  Scenario: 验证空目录已删除
    Tool: Bash
    Preconditions: 3个空目录存在
    Steps:
      1. 运行 `ls notes/grammar/ 2>&1 || echo "Directory not found"` 验证已删除
      2. 运行 `ls notes/reading-techniques/ 2>&1 || echo "Directory not found"` 验证已删除
      3. 运行 `ls practice/grammar/ 2>&1 || echo "Directory not found"` 验证已删除
      4. 运行 `ls notes/writing-structures/` 验证仍然存在
    Expected Result: 3个空目录已删除，writing-structures/ 仍然存在
    Failure Indicators: 目录仍然存在或writing-structures/被删除
    Evidence: .sisyphus/evidence/task-14-empty-dirs-removal.txt
  \`\`\`

  **Commit**: YES
  - Message: `notes(cleanup): remove empty directories`
  - Files: notes/grammar/, notes/reading-techniques/, practice/grammar/ (deletion)

- [x] 15. 更新 README.md 的目录结构部分

  **What to do**:
  - 更新 README.md 中的目录结构描述，使其反映实际的项目结构
  - 修改"Repository Structure"部分，替换 `modules/`, `data/` 为 `docs/`, `practice/daily/`, `notes/`
  - 保持其他内容不变

  **Must NOT do**:
  - 不修改 README.md 的其他部分
  - 不添加或删除内容

  **Recommended Agent Profile**:
  > Select category + skills based on task domain. Justify each choice.
  - **Category**: `unspecified-high`
    - Reason: 需要谨慎更新文档，确保准确性
  - **Skills**: []
    - 使用 bash 命令或文件编辑工具

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Wave 5 (final wave)
  - **Blocks**: Task 16-20
  - **Blocked By**: Tasks 13, 14

  **References**:

  **Pattern References** (existing code to follow):
  - `README.md` 现有的结构和格式

  **API/Type References** (contracts to implement against):
  - 无

  **External References** (libraries and frameworks):
  - 无

  **Acceptance Criteria**:
  - [x] README.md 的目录结构部分已更新
  - [x] 描述包含新的目录（docs/, practice/daily/, notes/listening/, notes/summaries/, notes/tech-notes/）
  - [x] Git 状态显示文件已修改
  - [x] 其他内容保持不变

  **QA Scenarios (MANDATORY):**

  \`\`\`
  Scenario: 验证 README.md 更新成功
    Tool: Bash
    Preconditions: README.md 存在，包含旧的目录结构描述
    Steps:
      1. 运行 `grep -A 10 "目录结构\|Directory Structure\|Repository Structure" README.md`
      2. 验证输出包含新的目录名（docs/, daily/, listening/ 等）
      3. 验证不再包含旧的目录名（modules/, data/）
    Expected Result: README.md 准确描述新的目录结构
    Failure Indicators: 仍包含旧的目录名或缺少新的目录名
    Evidence: .sisyphus/evidence/task-15-readme-update.txt
  \`\`\`

  **Commit**: YES
  - Message: `docs(readme): update README.md directory structure`
  - Files: README.md
  - Pre-commit: `grep -A 10 "目录结构" README.md`
 
- [x] 16. 验证根目录清理

  **What to do**:
  - 验证根目录只包含 Python 脚本文件（*.py）
  - 确认没有项目文档（README.md, IELTS_ANNOTATOR_GUIDE.md 等）
  - 确认没有学习笔记文件（ielts-verb-phrases-idioms-2026-03-15.md 等）

  **Must NOT do**:
  - 不修改或删除任何文件

  **Recommended Agent Profile**:
  > Select category + skills based on task domain. Justify each choice.
  - **Category**: `quick`
    - Reason: 简单的目录验证任务
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 6 (with Tasks 17-20)
  - **Blocks**: None (final tasks)
  - **Blocked By**: All previous tasks

  **Acceptance Criteria**:
  - [x] 根目录只包含 Python 脚本文件
  - [x] 没有项目文档.md文件
  - [x] 没有学习笔记.md文件
  - [x] `ls *.md` 输出显示为0或仅脚本文件

  **QA Scenarios (MANDATORY):**

  \`\`\`
  Scenario: 验证根目录已清理
    Tool: Bash
    Preconditions: 所有重构任务已完成
    Steps:
      1. 运行 `ls *.md | wc -l`
      2. 验证输出为0或仅包含脚本文件（如果有.md文件应都是脚本文档）
      3. 运行 `ls *.py | wc -l` 验证脚本文件仍存在
    Expected Result: 根目录干净，只有脚本文件
    Failure Indicators: 仍有项目文档或学习笔记在根目录
    Evidence: .sisyphus/evidence/task-16-root-cleanup.txt
  \`\`\`

  **Commit**: NO (groups with Task 17-20)
  - Message: None (final verification tasks)

- [x] 17. 验证 docs/ 结构

  **What to do**:
  - 验证 docs/ 目录包含6个项目文档
  - 确认目录结构正确

  **Must NOT do**:
  - 不修改或移动任何文件

  **Recommended Agent Profile**:
  > Select category + skills based on task domain. Justify each choice.
  - **Category**: `quick`
    - Reason: 简单的目录验证任务
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 6 (with Tasks 16, 18-20)
  - **Blocks**: None
  - **Blocked By**: All previous tasks

  **Acceptance Criteria**:
  - [x] docs/ 目录存在
  - [x] 包含6个项目文档
  - [x] 文件命名正确（README.md 等）
  - [x] `ls docs/*.md | wc -l` 输出为6

  **QA Scenarios (MANDATORY):**

  \`\`\`
  Scenario: 验证 docs/ 目录结构
    Tool: Bash
    Preconditions: docs/ 目录应存在并包含6个项目文档
    Steps:
      1. 运行 `ls docs/*.md | wc -l`
      2. 验证输出为6
      3. 运行 `ls docs/README.md docs/IELTS_ANNOTATOR_GUIDE.md docs/MATERIAL-EXTRACTION-STANDARDS.md docs/REVIEW-STRATEGY.md docs/VALIDATION-REPORT.md docs/TOOLS_SUMMARY.md`
    Expected Result: docs/ 有6个文件，所有命名正确
    Failure Indicators: 文件数量不是6个或命名不正确
    Evidence: .sisyphus/evidence/task-17-docs-verify.txt
  \`\`\`

  **Commit**: NO (groups with Task 16, 18-20)
  - Message: None (final verification tasks)

- [x] 18. 验证 practice/daily/ 结构

  **What to do**:
  - 验证 practice/daily/ 目录结构符合预期
  - 确认10个日期子目录存在
  - 确认24个文件已正确移动

  **Must NOT do**:
  - 不修改或移动任何文件

  **Recommended Agent Profile**:
  > Select category + skills based on task domain. Justify each choice.
  - **Category**: `quick`
    - Reason: 简单的目录验证任务
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 6 (with Tasks 16, 17, 19-20)
  - **Blocks**: None
  - **Blocked By**: All previous tasks

  **Acceptance Criteria**:
  - [x] practice/daily/ 目录存在
  - [x] 包含10个日期子目录（2026-02-09 到 2026-03-15）
  - [x] 包含24个daily文件
  - [x] `ls practice/daily/*/*.md | wc -l` 输出为24

  **QA Scenarios (MANDATORY):**

  \`\`\`
  Scenario: 验证 practice/daily/ 最终结构
    Tool: Bash
    Preconditions: practice/daily/ 应存在并包含所有daily文件
    Steps:
      1. 运行 `tree practice/daily/ -L 2`
      2. 验证输出显示10个日期子目录
      3. 运行 `ls practice/daily/*/*.md | wc -l`
      4. 验证输出为24
    Expected Result: 目录结构清晰，10个日期子目录，24个文件
    Failure Indicators: 子目录或文件数量不正确
    Evidence: .sisyphus/evidence/task-18-daily-final.txt
  \`\`\`

  **Commit**: NO (groups with Task 16, 17, 19-20)
  - Message: None (final verification tasks)

- [x] 19. 验证 notes/ 结构

  **What to do**:
  - 验证 notes/ 目录结构符合预期
  - 确认以下子目录存在：grammar, listening, summaries, tech-notes, writing-structures
  - 确认3个笔记文件已移动到正确位置

  **Must NOT do**:
  - 不修改或移动任何文件

  **Recommended Agent Profile**:
  > Select category + skills based on task domain. Justify each choice.
  - **Category**: `quick`
    - Reason: 简单的目录验证任务
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 6 (with Tasks 16, 17, 18, 20)
  - **Blocks**: None
  - **Blocked By**: All previous tasks

  **Acceptance Criteria**:
  - [x] notes/ 目录存在
  - [x] 包含正确子目录（grammar, listening, summaries, tech-notes, writing-structures）
  - [x] 3个笔记文件在正确位置
  - [x] `notes/listenning/` 已重命名为 `listening/`

  **QA Scenarios (MANDATORY):**

  \`\`\`
  Scenario: 验证 notes/ 最终结构
    Tool: Bash
    Preconditions: notes/ 目录应存在并包含重构后的结构
    Steps:
      1. 运行 `ls notes/`
      2. 验证输出包含：grammar, listening, summaries, tech-notes, writing-structures
      3. 运行 `ls notes/grammar/ielts-verb-phrases-idioms-2026-03-15.md` 验证文件存在
      4. 运行 `ls notes/listening/` 验证旧 listenning/ 不存在
    Expected Result: notes/ 结构正确，3个文件已移动，拼写错误已修正
    Failure Indicators: 子目录不正确或文件未移动
    Evidence: .sisyphus/evidence/task-19-notes-final.txt
  \`\`\`

  **Commit**: NO (groups with Task 16-18)
  - Message: None (final verification tasks)

- [x] 20. Git 提交和清理

  **What to do**:
  - 创建4个逻辑分组的 git 提交：
    1. docs(reorg): 创建 docs/ 并移动项目文档
    2. practice(reorg): 创建 practice/daily/ 并重组daily文件
    3. notes(typo): 修正 listenning → listening
    4. notes(cleanup): 删除空目录
    5. notes(reorg): 移动根笔记到合适位置
    6. docs(readme): 更新 README.md

  **Must NOT do**:
  - 不创建额外的提交
  - 不遗漏任何文件修改

  **Recommended Agent Profile**:
  > Select category + skills based on task domain. Justify each choice.
  - **Category**: `git`
    - Reason: 需要谨慎的 git 操作，确保提交历史清晰
  - **Skills**: []
    - 使用 git 命令进行提交和状态检查

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Wave 6 (final task)
  - **Blocks**: None
  - **Blocked By**: All previous tasks

  **References**:

  **Pattern References** (existing code to follow):
  - Git 提交模式和命名约定

  **API/Type References** (contracts to implement against):
  - 无

  **External References** (libraries and frameworks):
  - 无

  **Acceptance Criteria**:
  - [x] 4个 git 提交已创建
  - [x] `git log --oneline -4` 显示4个最新提交
  - [x] 所有文件修改已提交
  - [x] Git 工作目录干净（无未提交更改）

  **QA Scenarios (MANDATORY):**

  \`\`\`
  Scenario: 验证 Git 提交历史
    Tool: Bash
    Preconditions: 所有文件移动和修改已完成
    Steps:
      1. 运行 `git log --oneline -4`
      2. 验证输出显示4个提交（docs/reorg, practice/reorg, notes/typo, notes(cleanup), notes(reorg), docs(readme)）
      3. 运行 `git status` 验证工作目录干净
    Expected Result: 4个清晰的逻辑分组提交，无未提交更改
    Failure Indicators: 提交数量不是4个或有未提交更改
    Evidence: .sisyphus/evidence/task-20-git-commits.txt
  \`\`\`

  **Commit**: YES (final commit to complete work)
  - Message: `project-restructure: complete IELTS_Practice directory reorganization`
  - Files: all changed files
  - Pre-commit: `git log --oneline -4 && git status`

---
 
## Final Verification Wave (MANDATORY — after ALL implementation tasks)

> 5个审查代理并行运行。全部必须批准。拒绝→修复→重新运行。

- [x] F1. **计划合规审计** — `oracle`
  阅读计划全文。对于每个"Must Have"：验证实现存在（读取文件）。对于每个"Must NOT Have"：搜索代码库中的禁止模式——找到则拒绝。检查 .sisyphus/evidence/ 中的证据文件。对比交付物与计划。
  输出：`Must Have [N/N] | Must NOT Have [N/N] | Tasks [N/N] | VERDICT: APPROVE/REJECT`

- [x] F2. **代码质量审查** — `unspecified-high`
  运行验证脚本检查目录结构。对比交付物与计划。检查 AI slop：过度注释、过度抽象、通用名称（data/result/item/temp）。
  输出：`目录结构 [PASS/FAIL] | 文件移动 [N/N 成功] | 交付物 [N/N 匹配] | VERDICT`

- [x] F3. **真实手动QA** — `unspecified-high`
  从干净状态开始。验证目录结构正确。验证所有文件在预期位置。检查根目录已清理。
  输出：`目录结构 [N/N] | 文件位置 [N/N] | 根目录清理 [通过/失败] | VERDICT`

- [x] F4. **范围保真度检查** — `deep`
  对于每个任务：读取"What to do"，读取实际差异（git log/diff）。验证1:1——所有在规范中已构建（无缺失），规范外无任何东西已构建（无蔓延）。检查"Must NOT do"合规。检测跨任务污染：任务N接触任务M的文件。标记未计入的变化。
  输出：`任务 [N/N 合规] | 污染 [CLEAN/N 问题] | 未计入 [CLEAN/N 文件] | VERDICT`

---

## Commit Strategy

- **1**: docs(reorg): create docs/ and move project documentation
- **2**: practice(reorg): create practice/daily/ and reorganize daily files
- **3**: notes(reorg): fix typo, move root notes, clean empty dirs
- **4**: docs(readme): update README.md directory structure

---

## Success Criteria

### Verification Commands
```bash
# 验证根目录清理
ls *.md | wc -l  # Expected: 0 (only scripts remain)

# 验证 docs/ 结构
ls docs/ | wc -l  # Expected: 6 files

# 验证 practice/daily/ 结构
tree practice/daily/ -L 1  # Should show date-based subdirectories

# 验证 notes/ 结构
ls notes/  # Should show: grammar, listening, summaries, tech-notes, writing-structures

# 验证 README.md 准确性
grep -A 5 "目录结构\|Directory Structure" README.md
```

### Final Checklist
- [x] 根目录只包含 Python 脚本文件
- [x] 所有项目文档在 `docs/` 目录（6个文件）
- [x] 所有 daily 文件在 `practice/daily/` 按日期分组（24个文件）
- [x] 所有笔记文件在合适的 `notes/` 子目录（3个文件）
- [x] `notes/listenning/` 已修正为 `notes/listening/`
- [x] README.md 准确描述实际目录结构
- [x] Git 提交历史清晰（4个逻辑分组提交）
- [x] 所有空目录已删除（除 writing-structures/）
