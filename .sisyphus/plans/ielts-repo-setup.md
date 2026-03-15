# IELTS Training Repository Setup - 4-Week Intensive Sprint

## TL;DR

> **Quick Summary**: 建立结构化的IELTS训练仓库，支持4周高强度冲刺（5.0→7.0），重点Reading/Writing/Grammar，Listening/Speaking使用外部app，从电子书实时提取练习材料。

> **Deliverables**:
> - 完整的目录结构（reference/practice/notes/stats）
> - 4周详细任务安排（200+个带时间戳的任务单元）
> - Material extraction规范和示例
> - 复习策略（艾宾浩斯遗忘曲线）
> - README文档和入门指南

> **Estimated Effort**: Medium
> **Parallel Execution**: YES - 3 waves (Structure → Content → Validation)
> **Critical Path**: Directory setup → README → Skills definition → Task scheduling → Validation

---

## Context

### Original Request
用户想要将 `/mnt/d/MyDocs/IELTS_Practice` 目录作为日常雅思训练仓库，询问：
1. 如何设计仓库结构
2. 准备哪些适用于当前项目的skills

### Interview Summary

**Key Discussions**:
- **当前水平**: 初级 (5.0-6.0)，需要全面提升基础
- **目标分数**: 6.5-7.0，满足大多数研究生课程要求
- **时间限制**: 1个月冲刺（2025年2月6日 - 3月6日），每周25+小时
- **任务单元**: 25分钟练习 + 5分钟休息 = 30分钟/单元
- **模块分工**:
  - Reading (35%): 仓库重点，从reference电子书提取+轻量生成
  - Writing (35%): 仓库重点，从reference电子书提取+轻量生成
  - Listening (15%): 外部app（每日听力），仅任务指令
  - Speaking (10%): 外部app（每日听力），仅任务指令
  - Grammar (5%): 仓库记录笔记
  - Vocabulary (0%): 用户词汇较好，无需重点
- **Reference材料**: 用户上传电子书（转换为MD/TXT），实时提取+轻量生成（够用即可）
- **文件格式支持**: .md, .txt优先，.pdf可支持

**Research Findings**:
- IELTS考试结构: Listening (30min), Reading (60min), Writing (60min), Speaking (11-14min)
- 推荐学习时间: 初级到中级通常4-6个月，用户压缩到1个月需要高强度
- 核心策略: 诊断测试 → 针对练习 → 模考评估
- 复习策略: R1(1天), R2(3天), R3(7天), R4(14天)

### Metis Review

**Identified Gaps (addressed in this plan)**:
- ✅ Added concrete acceptance criteria for all deliverables
- ✅ Added verification commands for repository structure
- ✅ Added validation for material extraction time (<2 minutes)
- ✅ Added guardrails for timeboxing (25+5 strict enforcement)
- ✅ Added guardrails for material sourcing (P1→P2→P3)
- ✅ Added edge case handling (missing reference files, app unavailable)
- ✅ Added user onboarding acceptance criteria
- ✅ Added validation commands for skills

---

## Work Objectives

### Core Objective
建立一个高效的IELTS训练仓库，支持4周高强度冲刺计划，从用户上传的电子书中实时提取Reading/Writing/Grammar练习材料，Listening/Speaking使用外部app，实现5.0→7.0的目标分数提升。

### Concrete Deliverables
1. **Repository Structure**: 完整的目录结构（reference/practice/notes/stats）
2. **Documentation**: README.md（入门指南、使用说明）
3. **Task Schedule**: 4周详细任务安排（Week 1-4，200+个任务单元）
4. **Material Extraction Standards**: Reference材料提取/生成规范文档
5. **Review Strategy**: 艾宾浩斯复习策略实现
6. **Progress Tracking**: 进度追踪模板（weekly-reports, stats）

### Definition of Done
- [x] Repository structure created with all required directories
- [x] README.md created with complete onboarding guide
- [x] 4-week task schedule generated with timestamps
- [x] Material extraction standards documented
- [x] Reference directory populated with example structure (placeholder files)
- [x] All acceptance criteria verified via commands

### Must Have
- 4-week intensive sprint plan (Feb 6 - Mar 6, 100-120 hours)
- Reading/Writing focus (70% of time)
- Listening/Speaking via external app (instructions only)
- Grammar notes system
- Material extraction from reference ebooks (<2 min)
- Timebox enforcement (25+5 minute units)
- Review schedule (Ebbinghaus curve: 1d, 3d, 7d, 14d)
- Timestamps for all tasks

### Must NOT Have (Guardrails)

**Scope Boundaries (from Metis review)**:
- ❌ Do NOT generate listening audio files (use external app)
- ❌ Do NOT generate speaking scripts (app provides prompts)
- ❌ Do NOT create full Cambridge mock exams (too time-consuming)
- ❌ Do NOT build app integrations (instructions only)
- ❌ Do NOT generate vocabulary lists (user's vocab is good)
- ❌ Do NOT create visual progress charts (text-based only)
- ❌ Do NOT implement automatic scoring (manual grading only)
- ❌ Do NOT add flashcard systems (out of scope)
- ❌ Do NOT create mobile apps (desktop-only)
- ❌ Do NOT generate materials >2 minutes extraction time

**AI Slop Patterns to Avoid**:
- ❌ Generating excessive practice materials beyond daily needs
- ❌ Creating complex file structures beyond basic directories
- ❌ Adding unnecessary features (charts, dashboards, integrations)
- ❌ Spending time on non-essentials (backup systems, export formats)
- ❌ Generating complete IELTS exams (focus on targeted practice)
- ❌ Over-documenting with redundant information

---

## Verification Strategy (MANDATORY)

> **UNIVERSAL RULE: ZERO HUMAN INTERVENTION**
>
> ALL tasks in this plan MUST be verifiable WITHOUT any human action.
> This is NOT conditional — it applies to EVERY task, regardless of test strategy.
>
> **FORBIDDEN** — acceptance criteria that require:
> - "User manually tests..." / "用户手动测试..."
> - "User visually confirms..." / "用户目视确认..."
> - "User interacts with..." / "用户交互..."
> - "Ask user to verify..." / "要求用户验证..."
> - ANY step where a human must perform an action
>
> **ALL verification is executed by the agent** using tools (Read, Glob, Bash). No exceptions.

### Test Decision
- **Infrastructure exists**: N/A (Not a coding project)
- **Automated tests**: N/A (Content creation, not code)
- **Framework**: N/A

### Agent-Executed QA Scenarios (MANDATORY — ALL tasks)

**Verification Tool**: Bash (commands) + Read (file content verification)

---

## Execution Strategy

### Parallel Execution Waves

> Maximize throughput by grouping independent tasks into parallel waves.
> Each wave completes before the next begins.

```
Wave 0 (Start Immediately):
└── Task 0: Setup Auto-Conversion for EPUB/PDF (pandoc)

Wave 1 (After Wave 0):
├── Task 1: Create repository structure (directories)
└── Task 2: Create README.md (core documentation)

Wave 2 (After Wave 1):
├── Task 3: Create placeholder reference files
├── Task 4: Create Material Extraction Standards doc
└── Task 5: Create Review Strategy doc

Wave 3 (After Wave 2):
├── Task 6: Generate 4-week task schedule (Week 1)
├── Task 7: Generate 4-week task schedule (Week 2)
├── Task 8: Generate 4-week task schedule (Week 3)
└── Task 9: Generate 4-week task schedule (Week 4)

Wave 4 (After Wave 3):
└── Task 10: Validate all deliverables and verify structure
```

### Dependency Matrix

| Task | Depends On | Blocks | Can Parallelize With |
|------|------------|--------|---------------------|
| 0 | None | 1-5 | None |
| 1 | 0 | 2, 3, 4, 5 | None |
| 2 | 0, 1 | 6-9 | 3, 4, 5 |
| 3 | 0, 1 | 6-9 | 2, 4, 5 |
| 4 | 0, 1 | 6-9 | 2, 3, 5 |
| 5 | 0, 1 | 6-9 | 2, 3, 4 |
| 6 | 2, 3, 4, 5 | 10 | 7, 8, 9 |
| 7 | 2, 3, 4, 5 | 10 | 6, 8, 9 |
| 8 | 2, 3, 4, 5 | 10 | 6, 7, 9 |
| 9 | 2, 3, 4, 5 | 10 | 6, 7, 8 |
| 10 | 6, 7, 8, 9 | None | None (final) |

### Agent Dispatch Summary

| Wave | Tasks | Recommended Agents |
|------|-------|-------------------|
| 0 | 0 | delegate_task(category="quick", load_skills=["git-master"]) |
| 1 | 1, 2 | dispatch parallel after Wave 0 completes |
| 2 | 3, 4, 5 | dispatch parallel after Wave 1 completes |
| 3 | 6, 7, 8, 9 | dispatch parallel after Wave 2 completes |
| 4 | 10 | final validation task |

---

## TODOs

> Implementation + Documentation = ONE Task. Never separate.
> EVERY task MUST have: Recommended Agent Profile + Parallelization info.

- [x] 0. Setup Auto-Conversion for EPUB/PDF (pandoc)

  **What to do**:
  - Create scripts/auto-convert.sh with pandoc conversion logic
  - Create scripts/ directory if not exists
  - Script must handle .epub → .md conversion
  - Script must handle .pdf → .md conversion (fallback to .txt)
  - Create reference/conversion-log.md for tracking
  - Create reference/conversion-status.md for status
  - Include pandoc installation instructions in README

  **Must NOT do**:
  - Do NOT delete original .epub/.pdf files
  - Do NOT create complex UI tools (script only)
  - Do NOT integrate with external services (local conversion only)

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Simple script creation with pandoc commands
  - **Skills**: [`git-master`]
    - `git-master`: For version control of scripts

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Wave 0 (solo task)
  - **Blocks**: Tasks 1-5 (directory structure depends on pandoc setup)
  - **Blocked By**: None (can start immediately)

  **References** (CRITICAL - Be Exhaustive):

  **Documentation References**:
  - `.sisyphus/drafts/ielts-repo-design.md:617-790` - Complete Auto-Conversion Feature specification
  - `.sisyphus/drafts/ielts-repo-design.md:64-108` - File format requirements

  **External References**:
  - Pandoc documentation: https://pandoc.org/MANUAL.html

  **WHY Each Reference Matters**:
  - Draft file contains complete pandoc conversion requirements
  - File format requirements specify .epub/.pdf → .md conversion needs
  - Pandoc docs provide command syntax

  **Acceptance Criteria**:

  > **AGENT-EXECUTABLE VERIFICATION ONLY**

  - [ ] scripts/auto-convert.sh created
  - [ ] Script handles .epub → .md conversion
  - [ ] Script handles .pdf → .md conversion
  - [ ] Script has fallback .pdf → .txt conversion
  - [ ] reference/conversion-log.md created
  - [ ] reference/conversion-status.md created
  - [ ] README.md includes pandoc installation instructions
  - [ ] Script is executable (chmod +x)

  **Agent-Executed QA Scenarios (MANDATORY — per-scenario, ultra-detailed):**

  \`\`\`
  Scenario: Verify auto-conversion script exists and has correct structure
    Tool: Read
    Preconditions: scripts/ directory exists
    Steps:
      1. Read "scripts/auto-convert.sh"
      2. bash -c "grep -c 'pandoc' scripts/auto-convert.sh"
      3. Assert: Count >= 2 (at least 2 pandoc commands)
      4. bash -c "grep -c 'for epub in \*.epub' scripts/auto-convert.sh"
      5. Assert: Count >= 1 (epub loop exists)
      6. bash -c "grep -c 'for pdf in \*.pdf' scripts/auto-convert.sh"
      7. Assert: Count >= 1 (pdf loop exists)
      8. bash -c "grep -c 'fallback' scripts/auto-convert.sh"
      9. Assert: Count >= 1 (fallback logic exists)
    Expected Result: Script handles both .epub and .pdf with fallback
    Evidence: Script content verified
  \`\`\`

  \`\`\`
  Scenario: Verify conversion log and status files are created
    Tool: Bash
    Preconditions: reference/ directory exists
    Steps:
      1. bash -c "ls scripts/"
      2. Assert: Output contains auto-convert.sh
      3. bash -c "ls reference/ | grep -E '(conversion-log|conversion-status)'"
      4. Assert: Both conversion-log.md and conversion-status.md exist
      5. Read "reference/conversion-status.md"
      6. Assert: Contains table structure (Original File | Converted File | Status)
      7. Read "scripts/auto-convert.sh"
      8. bash -c "grep -c '#!/bin/bash' scripts/auto-convert.sh"
      9. Assert: Script has shebang (is executable)
    Expected Result: Script and log files created, script is executable
    Evidence: Command outputs and script content
  \`\`\`

  **Evidence to Capture**:
  - [ ] scripts/auto-convert.sh content
  - [ ] reference/conversion-log.md content
  - [ ] reference/conversion-status.md content

  **Commit**: YES (groups with Tasks 1-5)
  - Message: `feat: add pandoc auto-conversion for epub/pdf files`
  - Files: scripts/auto-convert.sh, reference/conversion-log.md, reference/conversion-status.md
  - Pre-commit: N/A

---

- [x] 1. Create Repository Structure

  **What to do**:
  - Create directory structure: reference/, practice/, notes/, progress/
  - Create subdirectories for each skill
  - Create placeholder README in each major directory

  **Must NOT do**:
  - Do NOT create any non-.md files (prometheus-md-only hook will block)
  - Do NOT create backup systems or export functionality
  - Do NOT add any additional directories beyond specified

  **Recommended Agent Profile**:
  > Select category + skills based on task domain. Justify each choice.
  - **Category**: `quick`
    - Reason: Simple directory creation, file operations, straightforward
  - **Skills**: [`git-master`]
    - `git-master`: Needed for creating file structure and git operations if needed

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Wave 1 (with Task 2)
  - **Blocks**: Tasks 3-9 (all depend on directory structure)
  - **Blocked By**: None (can start immediately)

  **References** (CRITICAL - Be Exhaustive):

  **Pattern References** (none - greenfield project):
  - No existing patterns to follow

  **Documentation References**:
  - `.sisyphus/drafts/ielts-repo-design.md:118-139` - Overall time allocation and 4-week plan structure
  - `.sisyphus/drafts/ielts-repo-design.md:191-211` - Repository structure design

  **WHY Each Reference Matters**:
  - Draft file contains the complete agreed-upon directory structure
  - Time allocation strategy informs the task distribution across 4 weeks
  - Reference directory structure must match user requirements

  **Acceptance Criteria**:

  > **AGENT-EXECUTABLE VERIFICATION ONLY** — No human action permitted.
  > Every criterion MUST be verifiable by running a command or using a tool.

  - [ ] All directories exist: reference/, practice/, notes/, progress/
  - [ ] All subdirectories exist: reference/, practice/reading/, practice/writing/, practice/grammar/, notes/grammar/, notes/reading-techniques/, notes/writing-structures/, progress/weekly-reports/, progress/stats/
  - [ ] README.md exists in root directory
  - [ ] README.md contains onboarding guide and usage instructions

  **Agent-Executed QA Scenarios (MANDATORY — per-scenario, ultra-detailed):**

  \`\`\`
  Scenario: Verify directory structure is complete
    Tool: Bash
    Preconditions: Working directory is /mnt/d/MyDocs/IELTS_Practice
    Steps:
      1. bash -c "ls -la | grep -E '^(reference|practice|notes|progress)'"
      2. Assert: Output contains reference, practice, notes, progress
      3. bash -c "ls reference/ && ls practice/ && ls notes/ && ls progress/"
      4. Assert: All directories are accessible
      5. bash -c "find . -type d -name 'reading' -o -name 'writing' -o -name 'grammar'"
      6. Assert: Output shows reading, writing, grammar subdirectories
    Expected Result: All required directories exist and are accessible
    Evidence: Command output captured
  \`\`\`

  \`\`\`
  Scenario: Verify README.md exists and contains required sections
    Tool: Read
    Preconditions: README.md file exists in root directory
    Steps:
      1. Read "README.md"
      2. Assert: File contains "# IELTS Practice Repository"
      3. Assert: File contains "## Repository Structure"
      4. Assert: File contains "## How to Use"
      5. Assert: File contains "## Task Schedule"
      6. Assert: File contains "## Progress Tracking"
    Expected Result: README.md is complete with all required sections
    Evidence: README.md content verified
  \`\`\`

  **Evidence to Capture**:
  - [ ] Directory listing output
  - [ ] README.md content verification

  **Commit**: YES (groups with Task 2)
  - Message: `feat: create repository structure and core documentation`
  - Files: README.md, placeholder files
  - Pre-commit: N/A

---

- [x] 2. Create README.md (Core Documentation)

  **What to do**:
  - Create comprehensive README.md with onboarding guide
  - Include repository structure explanation
  - Include usage instructions for each module
  - Include 4-week task schedule overview
  - Include progress tracking guide

  **Must NOT do**:
  - Do NOT add visual charts or diagrams (text-based only)
  - Do NOT add app integration instructions beyond what's required
  - Do NOT create multiple README files (single README.md only)

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Documentation creation, straightforward
  - **Skills**: [`git-master`]
    - `git-master`: For version control of documentation

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Task 1)
  - **Blocks**: Tasks 3-9 (content generation depends on README structure)
  - **Blocked By**: None (can start immediately)

  **References** (CRITICAL - Be Exhaustive):

  **Documentation References**:
  - `.sisyphus/drafts/ielts-repo-design.md:15-39` - User requirements and module explanations
  - `.sisyphus/drafts/ielts-repo-design.md:64-108` - Reference file format support and organization
  - `.sisyphus/drafts/ielts-repo-design.md:260-280` - Task execution workflows

  **External References**:
  - GitHub Docs: https://docs.github.com/en/repositories/managing-your-repositorys-files/working-with-readme - README best practices

  **WHY Each Reference Matters**:
  - User requirements must be reflected in README
  - Reference file formats need to be documented for user understanding
  - Task execution workflows guide users on how to use the system

  **Acceptance Criteria**:

  > **AGENT-EXECUTABLE VERIFICATION ONLY**

  - [ ] README.md created in root directory
  - [ ] Contains "# IELTS Practice Repository"
  - [ ] Contains "## Repository Structure" with directory tree
  - [ ] Contains "## Module Guide" explaining Reading/Writing/Grammar/Listening/Speaking
  - [ ] Contains "## How to Use" with step-by-step instructions
  - [ ] Contains "## 4-Week Task Schedule" with overview
  - [ ] Contains "## Progress Tracking" with instructions
  - [ ] Contains "## Reference Materials" with format requirements

  **Agent-Executed QA Scenarios (MANDATORY — per-scenario, ultra-detailed):**

  \`\`\`
  Scenario: Verify README.md contains all required sections
    Tool: Read
    Preconditions: README.md exists in root directory
    Steps:
      1. Read "README.md"
      2. bash -c "grep -c '# IELTS Practice Repository' README.md"
      3. Assert: Count equals 1 (header exists)
      4. bash -c "grep -c '## Repository Structure' README.md"
      5. Assert: Count >= 1 (section exists)
      6. bash -c "grep -c '## Module Guide' README.md"
      7. Assert: Count >= 1 (section exists)
      8. bash -c "grep -c '## How to Use' README.md"
      9. Assert: Count >= 1 (section exists)
      10. bash -c "grep -c '## 4-Week Task Schedule' README.md"
      11. Assert: Count >= 1 (section exists)
      12. bash -c "grep -c '## Progress Tracking' README.md"
      13. Assert: Count >= 1 (section exists)
    Expected Result: All required sections present in README.md
    Evidence: README.md grep output
  \`\`\`

  **Evidence to Capture**:
  - [ ] README.md content
  - [ ] Grep output for required sections

  **Commit**: YES (groups with Task 1)
  - Message: `feat: create repository structure and core documentation`
  - Files: README.md, placeholder files
  - Pre-commit: N/A

---

- [x] 3. Create Placeholder Reference Files

  **What to do**:
  - Create placeholder reference files with structure templates
  - reference/reading-book.md with placeholder content
  - reference/writing-book.md with placeholder content
  - reference/grammar-book.md with placeholder content
  - reference/essays-collection.md with placeholder content
  - reference/cambridge-tests.md with placeholder content
  - Each file should include metadata header template

  **Must NOT do**:
  - Do NOT create any actual practice content (placeholders only)
  - Do NOT generate vocabulary lists (user's vocab is good)
  - Do NOT create listening transcripts (use external app)
  - Do NOT create speaking scripts (use external app)

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Simple file creation with template content
  - **Skills**: [`git-master`]
    - `git-master`: For version control

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 4, 5)
  - **Blocks**: Tasks 6-9 (task scheduling needs reference structure)
  - **Blocked By**: Tasks 1, 2 (directory structure and README must exist)

  **References** (CRITICAL - Be Exhaustive):

  **Documentation References**:
  - `.sisyphus/drafts/ielts-repo-design.md:191-211` - Reference directory structure
  - `.sisyphus/drafts/ielts-repo-design.md:64-108` - Reference file format requirements

  **WHY Each Reference Matters**:
  - Directory structure must match design
  - File format requirements need to be included as templates

  **Acceptance Criteria**:

  > **AGENT-EXECUTABLE VERIFICATION ONLY**

  - [ ] All 5 reference files created: reading-book.md, writing-book.md, grammar-book.md, essays-collection.md, cambridge-tests.md
  - [ ] Each file has metadata header template (Book, Category, Level, Source, Format)
  - [ ] Each file has placeholder content indicating user should upload actual ebooks
  - [ ] Files are in .md format (not .txt or other formats)

  **Agent-Executed QA Scenarios (MANDATORY — per-scenario, ultra-detailed):**

  \`\`\`
  Scenario: Verify all reference files exist with correct format
    Tool: Bash
    Preconditions: reference/ directory exists
    Steps:
      1. bash -c "ls reference/"
      2. Assert: Output contains reading-book.md, writing-book.md, grammar-book.md, essays-collection.md, cambridge-tests.md
      3. bash -c "for file in reference/*.md; do head -10 $file | grep -E '(Book:|Category:|Level:)'; done"
      4. Assert: All files contain metadata header fields
      5. bash -c "for file in reference/*.md; do wc -l $file; done"
      6. Assert: All files have content (line count > 0)
    Expected Result: All 5 reference files exist with metadata headers
    Evidence: Command output captured
  \`\`\`

  \`\`\`
  Scenario: Verify reference file format is .md
    Tool: Bash
    Preconditions: reference/ directory exists
    Steps:
      1. bash -c "find reference/ -type f -name '*.md'"
      2. Assert: Output shows 5 .md files
      3. bash -c "find reference/ -type f ! -name '*.md'"
      4. Assert: Output is empty (no non-md files)
    Expected Result: All reference files are in .md format
    Evidence: Command output
  \`\`\`

  **Evidence to Capture**:
  - [ ] Directory listing of reference/
  - [ ] Metadata header verification output
  - [ ] File format verification output

  **Commit**: NO (groups with Tasks 4, 5)
  - Message: N/A
  - Files: N/A
  - Pre-commit: N/A

---

- [x] 4. Create Material Extraction Standards Document

  **What to do**:
  - Create MATERIAL-EXTRACTION-STANDARDS.md in docs/ or root
  - Document P1→P2→P3 material sourcing priority
  - Document extraction workflow (Read → Extract → Generate)
  - Document time limits (<2 minutes)
  - Include examples for Reading/Writing/Grammar
  - Include Listening/Speaking task instruction examples
  - Document guardrails and constraints

  **Must NOT do**:
  - Do NOT create complex extraction tools (documentation only)
  - Do NOT include code examples (not a coding project)
  - Do NOT add features beyond extraction standards

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Technical documentation creation
  - **Skills**: [`writing-clearly-and-concisely`]
    - `writing-clearly-and-concisely`: For clear, concise documentation

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 3, 5)
  - **Blocks**: Tasks 6-9 (task scheduling follows these standards)
  - **Blocked By**: Tasks 1, 2 (repository structure needed)

  **References** (CRITICAL - Be Exhaustive):

  **Documentation References**:
  - `.sisyphus/drafts/ielts-repo-design.md:143-490` - Complete Material Sourcing Priority & Standards section
  - `.sisyphus/drafts/ielts-repo-design.md:260-280` - Extraction workflows
  - `.sisyphus/drafts/ielts-repo-design.md:284-332` - Lightweight generation examples

  **WHY Each Reference Matters**:
  - Complete sourcing standards must be documented
  - Extraction workflows guide material usage
  - Examples provide concrete usage patterns

  **Acceptance Criteria**:

  > **AGENT-EXECUTABLE VERIFICATION ONLY**

  - [ ] MATERIAL-EXTRACTION-STANDARDS.md created
  - [ ] Contains "## Material Sourcing Priority (P1→P2→P3)"
  - [ ] Contains "## Extraction Workflow" with 6 steps
  - [ ] Contains "## Time Limits" (<2 minutes)
  - [ ] Contains "## Reading Task Examples"
  - [ ] Contains "## Writing Task Examples"
  - [ ] Contains "## Grammar Task Examples"
  - [ ] Contains "## Listening/Speaking Task Instructions"
  - [ ] Contains "## Guardrails and Constraints"
  - [ ] Contains "## Examples" for at least 3 scenarios

  **Agent-Executed QA Scenarios (MANDATORY — per-scenario, ultra-detailed):**

  \`\`\`
  Scenario: Verify Material Extraction Standards document is complete
    Tool: Read
    Preconditions: MATERIAL-EXTRACTION-STANDARDS.md exists
    Steps:
      1. Read "MATERIAL-EXTRACTION-STANDARDS.md"
      2. bash -c "grep -c '## Material Sourcing Priority' MATERIAL-EXTRACTION-STANDARDS.md"
      3. Assert: Count >= 1 (section exists)
      4. bash -c "grep -c 'P1\|P2\|P3' MATERIAL-EXTRACTION-STANDARDS.md"
      5. Assert: Count >= 3 (priority levels documented)
      6. bash -c "grep -c '<2 minutes\|≤2 minutes' MATERIAL-EXTRACTION-STANDARDS.md"
      7. Assert: Count >= 1 (time limit documented)
      8. bash -c "grep -c '## Reading' MATERIAL-EXTRACTION-STANDARDS.md"
      9. Assert: Count >= 1 (Reading section exists)
      10. bash -c "grep -c '## Writing' MATERIAL-EXTRACTION-STANDARDS.md"
      11. Assert: Count >= 1 (Writing section exists)
      12. bash -c "grep -c '## Grammar' MATERIAL-EXTRACTION-STANDARDS.md"
      13. Assert: Count >= 1 (Grammar section exists)
    Expected Result: All required sections present
    Evidence: Grep output captured
  \`\`\`

  **Evidence to Capture**:
  - [ ] MATERIAL-EXTRACTION-STANDARDS.md content
  - [ ] Grep output for required sections

  **Commit**: NO (groups with Tasks 3, 5)
  - Message: N/A
  - Files: N/A
  - Pre-commit: N/A

---

- [x] 5. Create Review Strategy Document

  **What to do**:
  - Create REVIEW-STRATEGY.md in docs/ or root
  - Document Ebbinghaus forgetting curve (R1: 1d, R2: 3d, R3: 7d, R4: 14d)
  - Document review content for each round
  - Document how to track reviews in the system
  - Include review schedule template
  - Include examples of review entries

  **Must NOT do**:
  - Do NOT create automated review systems (manual tracking only)
  - Do NOT add flashcard integration (out of scope)
  - Do NOT create reminder systems (manual scheduling only)

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Documentation creation
  - **Skills**: [`writing-clearly-and-concisely`]
    - `writing-clearly-and-concisely`: For clear documentation

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 3, 4)
  - **Blocks**: Tasks 6-9 (task scheduling incorporates review strategy)
  - **Blocked By**: Tasks 1, 2 (repository structure needed)

  **References** (CRITICAL - Be Exhaustive):

  **Documentation References**:
  - `.sisyphus/drafts/ielts-repo-design.md:133-139` - Ebbinghaus review strategy table
  - `.sisyphus/drafts/ielts-repo-design.md:133-139` - Review intervals and content

  **WHY Each Reference Matters**:
  - Ebbinghaus curve must be accurately documented
  - Review intervals and content need to be clearly defined

  **Acceptance Criteria**:

  > **AGENT-EXECUTABLE VERIFICATION ONLY**

  - [ ] REVIEW-STRATEGY.md created
  - [ ] Contains "## Ebbinghaus Forgetting Curve" with R1-R4 intervals
  - [ ] Contains "## Review Content" for each round
  - [ ] Contains "## How to Track Reviews"
  - [ ] Contains "## Review Schedule Template"
  - [ ] Contains "## Review Entry Examples"

  **Agent-Executed QA Scenarios (MANDATORY — per-scenario, ultra-detailed):**

  \`\`\`
  Scenario: Verify Review Strategy document is complete
    Tool: Read
    Preconditions: REVIEW-STRATEGY.md exists
    Steps:
      1. Read "REVIEW-STRATEGY.md"
      2. bash -c "grep -c '## Ebbinghaus' REVIEW-STRATEGY.md"
      3. Assert: Count >= 1 (section exists)
      4. bash -c "grep -c 'R1\|R2\|R3\|R4' REVIEW-STRATEGY.md"
      5. Assert: Count >= 4 (all review rounds documented)
      6. bash -c "grep -c '1 day\|3 days\|7 days\|14 days' REVIEW-STRATEGY.md"
      7. Assert: Count >= 4 (all intervals documented)
      8. bash -c "grep -c '## Review Content' REVIEW-STRATEGY.md"
      9. Assert: Count >= 1 (review content section exists)
    Expected Result: All required sections and intervals documented
    Evidence: Grep output captured
  \`\`\`

  **Evidence to Capture**:
  - [ ] REVIEW-STRATEGY.md content
  - [ ] Grep output for required sections

  **Commit**: YES (groups with Tasks 3, 4)
  - Message: `docs: add material extraction standards and review strategy`
  - Files: MATERIAL-EXTRACTION-STANDARDS.md, REVIEW-STRATEGY.md
  - Pre-commit: N/A

---

- [x] 6. Generate Week 1 Task Schedule

  **What to do**:
  - Create WEEK-1-SCHEDULE.md in schedules/ or progress/
  - Generate detailed daily tasks for Feb 6-12 (7 days)
  - Each task must have:
    - Task number (Task-XX)
    - Timestamp (HH:MM-HH:MM)
    - Module (Reading/Writing/Grammar/Listening/Speaking)
    - Task description
    - Material source (reference/ or external app)
    - Review tag (if applicable: R1/R2/R3/R4)
  - Total: ~50-60 task units (8-9 per day)
  - Include diagnostic test on Day 1 (Feb 6)
  - Include mock test on Day 7 (Feb 12)

  **Must NOT do**:
  - Do NOT generate actual practice content (scheduling only)
  - Do NOT create tasks beyond 30-minute units
  - Do NOT schedule any tasks without timestamps
  - Do NOT generate listening/speaking materials (external app instructions only)

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Creating structured schedule documentation
  - **Skills**: [`writing-clearly-and-concisely`]
    - `writing-clearly-and-concisely`: For clear, organized schedule

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Tasks 7, 8, 9)
  - **Blocks**: Task 10 (final validation)
  - **Blocked By**: Tasks 1-5 (all documentation must exist)

  **References** (CRITICAL - Be Exhaustive):

  **Documentation References**:
  - `.sisyphus/drafts/ielts-repo-design.md:117-139` - Overall time allocation and 4-week plan
  - `.sisyphus/drafts/ielts-repo-design.md:133-139` - Review strategy (R1-R4)
  - `.sisyphus/drafts/ielts-repo-design.md:124-131` - Module time allocation

  **External References**:
  - IELTS structure: Research findings showing Listening(30m), Reading(60m), Writing(60m), Speaking(11-14m)

  **WHY Each Reference Matters**:
  - Time allocation ensures balanced skill coverage
  - Review strategy must be incorporated into schedule
  - Module proportions (35/35/15/10/5/0) must be followed

  **Acceptance Criteria**:

  > **AGENT-EXECUTABLE VERIFICATION ONLY**

  - [ ] WEEK-1-SCHEDULE.md created
  - [ ] Contains 7 days (Feb 6-12)
  - [ ] Each day contains 8-9 task units (25+5 min)
  - [ ] Day 1 (Feb 6) contains diagnostic test tasks
  - [ ] Day 7 (Feb 12) contains mock test tasks
  - [ ] Total task count ~50-60 for the week
  - [ ] All tasks have timestamps (HH:MM-HH:MM format)
  - [ ] All tasks have module labels (Reading/Writing/Grammar/Listening/Speaking)
  - [ ] Review tasks are tagged with R1/R2/R3/R4
  - [ ] Module distribution approximates: Reading(35%), Writing(35%), Grammar(5%), Listening(15%), Speaking(10%)

  **Agent-Executed QA Scenarios (MANDATORY — per-scenario, ultra-detailed):**

  \`\`\`
  Scenario: Verify Week 1 schedule is complete and follows time allocation
    Tool: Read + Bash
    Preconditions: WEEK-1-SCHEDULE.md exists
    Steps:
      1. Read "WEEK-1-SCHEDULE.md"
      2. bash -c "grep -c '## Day' WEEK-1-SCHEDULE.md"
      3. Assert: Count equals 7 (7 days in Week 1)
      4. bash -c "grep -c 'Task-' WEEK-1-SCHEDULE.md"
      5. Assert: Count >= 50 (at least 50 tasks)
      6. bash -c "grep -c 'Task-01.*Diagnostic' WEEK-1-SCHEDULE.md"
      7. Assert: Count >= 1 (diagnostic test exists)
      8. bash -c "grep -c '\[19:00-\|09:00-\|14:00-' WEEK-1-SCHEDULE.md"
      9. Assert: Count >= 40 (timestamps present)
      10. bash -c "grep -E '(Reading|Writing|Grammar|Listening|Speaking)' WEEK-1-SCHEDULE.md | wc -l"
      11. Assert: Count >= 40 (module labels present)
      12. bash -c "grep -c 'R1\|R2\|R3\|R4' WEEK-1-SCHEDULE.md"
      13. Assert: Count >= 5 (review tasks present)
    Expected Result: Week 1 schedule complete with 7 days, ~50+ tasks, timestamps, modules, and reviews
    Evidence: Grep output captured
  \`\`\`

  **Evidence to Capture**:
  - [ ] WEEK-1-SCHEDULE.md content (first 100 lines)
  - [ ] Grep output for structure verification
  - [ ] Module distribution statistics

  **Commit**: NO (groups with Tasks 7, 8, 9)
  - Message: N/A
  - Files: N/A
  - Pre-commit: N/A

---

- [x] 7. Generate Week 2 Task Schedule

  **What to do**:
  - Create WEEK-2-SCHEDULE.md in schedules/ or progress/
  - Generate detailed daily tasks for Feb 13-19 (7 days)
  - Follow same format as Week 1
  - Include R1 reviews from Week 1 tasks
  - Include mock test on Day 14 (Feb 19)
  - Focus on intensive training (no more diagnostics)

  **Must NOT do**:
  - Do NOT generate actual practice content
  - Do NOT schedule tasks beyond 30-minute units
  - Do NOT create tasks without timestamps

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Schedule documentation creation
  - **Skills**: [`writing-clearly-and-concisely`]
    - `writing-clearly-and-concisely`: For clear organization

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Tasks 6, 8, 9)
  - **Blocks**: Task 10 (final validation)
  - **Blocked By**: Tasks 1-5 (documentation must exist)

  **References** (CRITICAL - Be Exhaustive):

  **Documentation References**:
  - `.sisyphus/drafts/ielts-repo-design.md:117-139` - Overall time allocation
  - `.sisyphus/drafts/ielts-repo-design.md:133-139` - Review strategy

  **WHY Each Reference Matters**:
  - Must maintain consistent format with Week 1
  - Review schedule must continue from Week 1

  **Acceptance Criteria**:

  > **AGENT-EXECUTABLE VERIFICATION ONLY**

  - [ ] WEEK-2-SCHEDULE.md created
  - [ ] Contains 7 days (Feb 13-19)
  - [ ] Each day contains 8-9 task units
  - [ ] Day 14 (Feb 19) contains mock test tasks
  - [ ] Review tasks tagged with R1/R2 (from Week 1)
  - [ ] All tasks have timestamps and module labels
  - [ ] Module distribution follows 35/35/15/10/5/0 proportion

  **Agent-Executed QA Scenarios (MANDATORY — per-scenario, ultra-detailed):**

  \`\`\`
  Scenario: Verify Week 2 schedule format and structure
    Tool: Read + Bash
    Preconditions: WEEK-2-SCHEDULE.md exists
    Steps:
      1. Read "WEEK-2-SCHEDULE.md"
      2. bash -c "grep -c '## Day' WEEK-2-SCHEDULE.md"
      3. Assert: Count equals 7 (7 days)
      4. bash -c "grep -c 'Task-' WEEK-2-SCHEDULE.md"
      5. Assert: Count >= 50 (at least 50 tasks)
      6. bash -c "grep -c '\[19:00-\|09:00-\|14:00-' WEEK-2-SCHEDULE.md"
      7. Assert: Count >= 40 (timestamps present)
      8. bash -c "grep -c 'R1\|R2' WEEK-2-SCHEDULE.md"
      9. Assert: Count >= 10 (review tasks from Week 1)
    Expected Result: Week 2 schedule complete with 7 days, ~50+ tasks, timestamps, reviews
    Evidence: Grep output captured
  \`\`\`

  **Evidence to Capture**:
  - [ ] WEEK-2-SCHEDULE.md content
  - [ ] Grep output for verification

  **Commit**: NO (groups with Tasks 6, 8, 9)
  - Message: N/A
  - Files: N/A
  - Pre-commit: N/A

---

- [x] 8. Generate Week 3 Task Schedule

  **What to do**:
  - Create WEEK-3-SCHEDULE.md in schedules/ or progress/
  - Generate detailed daily tasks for Feb 20-26 (7 days)
  - Include R2 reviews from Week 1 tasks
  - Include R1 reviews from Week 2 tasks
  - Include mock test on Day 21 (Feb 26)

  **Must NOT do**:
  - Do NOT generate actual practice content
  - Do NOT schedule tasks beyond 30-minute units

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Schedule documentation
  - **Skills**: [`writing-clearly-and-concisely`]
    - `writing-clearly-and-concisely`: For clear organization

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Tasks 6, 7, 9)
  - **Blocks**: Task 10 (final validation)
  - **Blocked By**: Tasks 1-5 (documentation must exist)

  **References** (CRITICAL - Be Exhaustive):

  **Documentation References**:
  - `.sisyphus/drafts/ielts-repo-design.md:117-139` - Time allocation
  - `.sisyphus/drafts/ielts-repo-design.md:133-139` - Review strategy

  **WHY Each Reference Matters**:
  - Maintains consistency with Weeks 1-2
  - Review schedule continues from previous weeks

  **Acceptance Criteria**:

  > **AGENT-EXECUTABLE VERIFICATION ONLY**

  - [ ] WEEK-3-SCHEDULE.md created
  - [ ] Contains 7 days (Feb 20-26)
  - [ ] Each day contains 8-9 task units
  - [ ] Day 21 (Feb 26) contains mock test
  - [ ] Review tasks tagged with R1, R2
  - [ ] All tasks have timestamps and module labels

  **Agent-Executed QA Scenarios (MANDATORY — per-scenario, ultra-detailed):**

  \`\`\`
  Scenario: Verify Week 3 schedule structure
    Tool: Read + Bash
    Preconditions: WEEK-3-SCHEDULE.md exists
    Steps:
      1. Read "WEEK-3-SCHEDULE.md"
      2. bash -c "grep -c '## Day' WEEK-3-SCHEDULE.md"
      3. Assert: Count equals 7
      4. bash -c "grep -c 'Task-' WEEK-3-SCHEDULE.md"
      5. Assert: Count >= 50
      6. bash -c "grep -c '\[19:00-\|09:00-\|14:00-' WEEK-3-SCHEDULE.md"
      7. Assert: Count >= 40
    Expected Result: Week 3 schedule complete with 7 days, ~50+ tasks
    Evidence: Grep output captured
  \`\`\`

  **Evidence to Capture**:
  - [ ] WEEK-3-SCHEDULE.md content
  - [ ] Grep output

  **Commit**: NO (groups with Tasks 6, 7, 9)
  - Message: N/A
  - Files: N/A
  - Pre-commit: N/A

---

- [x] 9. Generate Week 4 Task Schedule

  **What to do**:
  - Create WEEK-4-SCHEDULE.md in schedules/ or progress/
  - Generate detailed daily tasks for Feb 27 - Mar 5 (7 days)
  - Include R3 reviews from Week 1 tasks
  - Include R2 reviews from Week 2 tasks
  - Include R1 reviews from Week 3 tasks
  - Include final mock test on Day 28 (Mar 5)
  - Include overall progress summary tasks

  **Must NOT do**:
  - Do NOT generate actual practice content
  - Do NOT schedule tasks beyond 30-minute units

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: Final schedule documentation
  - **Skills**: [`writing-clearly-and-concisely`]
    - `writing-clearly-and-concisely`: For clear organization

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 3 (with Tasks 6, 7, 8)
  - **Blocks**: Task 10 (final validation)
  - **Blocked By**: Tasks 1-5 (documentation must exist)

  **References** (CRITICAL - Be Exhaustive):

  **Documentation References**:
  - `.sisyphus/drafts/ielts-repo-design.md:117-139` - Time allocation
  - `.sisyphus/drafts/ielts-repo-design.md:133-139` - Review strategy

  **WHY Each Reference Matters**:
  - Maintains consistency with Weeks 1-3
  - Final week includes all review rounds

  **Acceptance Criteria**:

  > **AGENT-EXECUTABLE VERIFICATION ONLY**

  - [ ] WEEK-4-SCHEDULE.md created
  - [ ] Contains 7 days (Feb 27 - Mar 5)
  - [ ] Each day contains 8-9 task units
  - [ ] Day 28 (Mar 5) contains final mock test
  - [ ] Review tasks tagged with R1, R2, R3
  - [ ] All tasks have timestamps and module labels
  - [ ] Includes overall progress summary

  **Agent-Executed QA Scenarios (MANDATORY — per-scenario, ultra-detailed):**

  \`\`\`
  Scenario: Verify Week 4 schedule structure and completeness
    Tool: Read + Bash
    Preconditions: WEEK-4-SCHEDULE.md exists
    Steps:
      1. Read "WEEK-4-SCHEDULE.md"
      2. bash -c "grep -c '## Day' WEEK-4-SCHEDULE.md"
      3. Assert: Count equals 7
      4. bash -c "grep -c 'Task-' WEEK-4-SCHEDULE.md"
      5. Assert: Count >= 50
      6. bash -c "grep -c 'Final Mock Test' WEEK-4-SCHEDULE.md"
      7. Assert: Count >= 1 (final test exists)
      8. bash -c "grep -c 'Progress Summary' WEEK-4-SCHEDULE.md"
      9. Assert: Count >= 1 (summary included)
    Expected Result: Week 4 schedule complete with 7 days, ~50+ tasks, final test, summary
    Evidence: Grep output captured
  \`\`\`

  **Evidence to Capture**:
  - [ ] WEEK-4-SCHEDULE.md content
  - [ ] Grep output

  **Commit**: YES (groups with Tasks 6, 7, 8)
  - Message: `docs: add 4-week task schedules with timestamps and reviews`
  - Files: WEEK-1-SCHEDULE.md, WEEK-2-SCHEDULE.md, WEEK-3-SCHEDULE.md, WEEK-4-SCHEDULE.md
  - Pre-commit: N/A

---

- [x] 10. Final Validation and Documentation

  **What to do**:
  - Run all validation commands from previous tasks
  - Verify repository structure is complete
  - Verify all documentation files exist
  - Verify all 4-week schedules are generated
  - Create VALIDATION-REPORT.md with:
    - Directory structure verification
    - File existence verification
    - Acceptance criteria checklist
    - Any issues found and resolved

  **Must NOT do**:
  - Do NOT add any new features or files
  - Do NOT modify existing content beyond validation

  **Recommended Agent Profile**:
  - **Category**: `unspecified-low`
    - Reason: Validation and reporting
  - **Skills**: [`git-master`]
    - `git-master`: For git status check if needed

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Sequential (final task)
  - **Blocks**: None (final task)
  - **Blocked By**: Tasks 6-9 (all schedules must exist)

  **References** (CRITICAL - Be Exhaustive):

  **Documentation References**:
  - All previous tasks' acceptance criteria
  - `.sisyphus/drafts/ielts-repo-design.md` - Overall design requirements

  **WHY Each Reference Matters**:
  - Must verify all deliverables meet acceptance criteria
  - Must ensure project completion

  **Acceptance Criteria**:

  > **AGENT-EXECUTABLE VERIFICATION ONLY**

  - [ ] VALIDATION-REPORT.md created
  - [ ] Report includes directory structure verification
  - [ ] Report includes file existence verification (README, reference files, schedules, standards docs)
  - [ ] Report includes acceptance criteria checklist for all 10 tasks
  - [ ] All validation commands executed successfully
  - [ ] No critical issues found (or issues resolved)

  **Agent-Executed QA Scenarios (MANDATORY — per-scenario, ultra-detailed):**

  \`\`\`
  Scenario: Final validation of all deliverables
    Tool: Bash + Read
    Preconditions: All previous tasks completed
    Steps:
      1. bash -c "ls -la | grep -E '(reference|practice|notes|progress)'"
      2. Assert: Output shows all 4 directories
      3. bash -c "ls reference/ | wc -l"
      4. Assert: Count equals 5 (5 reference files)
      5. bash -c "ls WEEK-*.md 2>/dev/null | wc -l"
      6. Assert: Count equals 4 (4 weekly schedules)
      7. Read "README.md"
      8. Assert: Contains all required sections
      9. Read "VALIDATION-REPORT.md"
      10. Assert: Contains validation results and checklist
    Expected Result: All deliverables verified, validation report created
    Evidence: Command outputs and file contents
  \`\`\`

  **Evidence to Capture**:
  - [ ] Directory listing outputs
  - [ ] File count outputs
  - [ ] VALIDATION-REPORT.md content
  - [ ] Overall validation status

  **Commit**: YES
  - Message: `chore: complete IELTS repository setup with validation report`
  - Files: VALIDATION-REPORT.md
  - Pre-commit: All previous validation commands pass

---

## Commit Strategy

| After Task | Message | Files | Verification |
|------------|---------|-------|--------------|
| 0 | `feat: add pandoc auto-conversion for epub/pdf files` | scripts/auto-convert.sh, reference/conversion-log.md, reference/conversion-status.md | Script handles .epub and .pdf conversion |
| 1+2 | `feat: create repository structure and core documentation` | README.md, directories | README.md exists |
| 3+4+5 | `docs: add material extraction standards and review strategy` | MATERIAL-EXTRACTION-STANDARDS.md, REVIEW-STRATEGY.md, reference/* | All docs contain required sections |
| 6+7+8+9 | `docs: add 4-week task schedules with timestamps and reviews` | WEEK-*-SCHEDULE.md | All schedules have ~50+ tasks |
| 10 | `chore: complete IELTS repository setup with validation report` | VALIDATION-REPORT.md | All validation commands pass |

---

## Success Criteria

### Verification Commands

```bash
# Directory structure verification (including scripts/)
bash -c "ls -la | grep -E '(scripts|reference|practice|notes|progress)'"
# Expected: scripts, reference, practice, notes, progress

# Auto-conversion script verification
bash -c "test -f scripts/auto-convert.sh && echo 'Script exists' || echo 'Script missing'"
# Expected: Script exists

# Reference files verification
bash -c "ls reference/*.md | wc -l"
# Expected: 5 files (including conversion log/status)

# Weekly schedules verification
bash -c "ls WEEK-*-SCHEDULE.md | wc -l"
# Expected: 4 files

# README verification
bash -c "grep -c '## Repository Structure\|## Module Guide\|## How to Use\|## Pandoc Installation' README.md"
# Expected: All sections present including pandoc installation

# Task count verification
bash -c "grep -c 'Task-' WEEK-*-SCHEDULE.md"
# Expected: Total >= 200 tasks
```

### Final Checklist

- [x] Auto-conversion script created (scripts/auto-convert.sh)
- [x] Conversion log files created (reference/conversion-log.md, conversion-status.md)
- [x] Repository structure created (reference, practice, notes, progress)
- [x] README.md with complete onboarding guide (includes pandoc installation instructions)
- [x] 5 reference placeholder files created
- [x] MATERIAL-EXTRACTION-STANDARDS.md created
- [x] REVIEW-STRATEGY.md created
- [x] 4 weekly schedules created (Week 1-4)
- [x] Each week has ~50-60 task units
- [x] All tasks have timestamps (HH:MM-HH:MM)
- [x] All tasks have module labels
- [x] Review tasks tagged with R1/R2/R3/R4
- [x] VALIDATION-REPORT.md created
- [x] All acceptance criteria verified

---

## Post-Implementation Notes

### For User

After completing this plan, your IELTS training repository will be ready for 4-week intensive sprint:

1. **Upload your reference ebooks** to `reference/` directory (支持 .epub 和 .pdf 格式)
2. **Run auto-conversion script** to convert .epub/.pdf to .md format:
   ```bash
   bash scripts/auto-convert.sh
   ```
3. **Start with Day 1 tasks** in WEEK-1-SCHEDULE.md
4. **Follow the 25+5 minute timebox** for each task unit
5. **Track progress** in `progress/weekly-reports/`
6. **Follow review schedule** (R1: 1d, R2: 3d, R3: 7d, R4: 14d)

### Next Steps

This plan creates the foundation. Future phases could include:
- Automated progress tracking
- Visual charts and dashboards
- Flashcard integration (Anki)
- Mobile app support
- AI-powered feedback

(These are intentionally out of scope for this initial setup phase)
