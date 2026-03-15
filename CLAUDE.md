# IELTS Practice Project - AI Instructions

> Instructions for Claude Code assistants working on this project

---

## Memory Update Protocol

**CRITICAL**: When working on this project, update `memory/MEMORY.md` when ANY of the following occur:

### When to Update Memory

| Trigger | Action | Example |
|---------|--------|---------|
| **Major decision made** | Add to "Completed Work" section | Chose not to add audio links due to reliability concerns |
| **New pattern discovered** | Add to "File Format Conventions" | Task files use Hong Kong tutorial standard |
| **Project structure change** | Update "Project Overview" | Added new quick-reference file |
| **Git workflow decision** | Add to "Git Configuration" | Stopped tracking .sisyphus/ files |
| **User preference stated** | Add to "User Preferences" section | User prefers Chinese explanations |
| **Recurring issue solved** | Add to "Common Pitfalls" | CRLF warnings on Windows |

### Memory Update Format

When updating memory:
1. **Read existing memory first** - Avoid duplicates
2. **Update specific sections** - Don't rewrite entire file
3. **Keep it concise** - Under 200 lines total
4. **Link related info** - Cross-reference sections
5. **Date stamp updates** - Use `*Last Updated: YYYY-MM-DD*`

### Quick Memory Update Template

```markdown
## [Section Name]

**Update [Date]**: [Brief description of what changed and why]

[Rationale or context]
```

---

## Project Context

### What This Project Is

A **100-task IELTS Speaking practice system** organized into 4 weeks:
- Week 1 (1-25): Fluency Foundation
- Week 2 (26-50): Sentence Expansion
- Week 3 (51-75): Pronunciation + Mock Exams
- Week 4 (76-100): Final Sprint

### Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Task files follow Hong Kong tutorial standard | Pre-study → Practice → Answer → Notes |
| No specific audio/video URLs | Links break; use general guidance |
| Unified PROGRESS-TRACKER.md | Easier than complex spreadsheets |
| Topic-based navigation (TOPIC-INDEX.md) | IELTS is topic-driven |
| Quick reference cards per week | Consolidated learning |

### File Naming Conventions

```
task-XXX-[topic].md          # Individual tasks (001-100)
quick-reference-[skill].md   # Reference cards
PROGRESS-TRACKER.md          # Master progress file
TOPIC-INDEX.md               # Topic navigation
```

---

## Git Workflow

### Files NOT to Track

```
.sisyphus/                   # Project notes (local only)
.claude/settings.local.json  # Local settings (not committed)
```

If a file was previously tracked and should be local:
```bash
git rm --cached [file]
```

### Commit Message Style

```
type(scope): brief description

Details if needed.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
```

Types: `docs`, `feat`, `fix`, `refactor`, `chore`

---

## User Preferences

| Preference | Setting |
|------------|---------|
| **Output language** | Chinese explanations, technical terms in English |
| **Output style** | Explanatory (with "★ Insight" blocks) |
| **Code references** | Use markdown `[link](path)` format, not backticks |
| **Format validation** | Fix markdown linting warnings when possible |

---

## Common Tasks

### Creating a New Task

1. Follow Hong Kong tutorial standard structure
2. Include: PRE-STUDY → GUIDED PRACTICE → MODEL ANSWER → COACH'S NOTES
3. Add RELATED TASKS section with links to related tasks
4. Link back from related tasks
5. Update PROGRESS-TRACKER.md if creating new task

### Updating Quick References

1. Check existing quick-reference files first
2. Add new patterns to appropriate week's reference
3. Update TOPIC-INDEX.md if topic-related
4. Keep entries concise and actionable

### Modifying Multiple Files

1. Use parallel tool calls when possible
2. Update related tasks together
3. Verify all links work after changes
4. Test markdown syntax

---

## Before Claiming Work Complete

- [ ] All created files exist and have content
- [ ] Markdown linting passes (no CRLF/LF warnings if possible)
- [ ] Links are tested and work
- [ ] Related files are cross-referenced
- [ ] Git status shows expected changes
- [ ] Commit message follows project style
- [ ] Memory updated if decisions were made
- [ ] User notified of what was done

---

## Memory Maintenance

### Review Memory When

- Starting work on a new feature
- User asks "what did we decide about X?"
- Encountering a recurring issue
- Making structural changes

### Memory Sections to Keep Updated

1. **Project Overview** - Structure and purpose
2. **Completed Work** - Recent decisions with rationale
3. **File Format Conventions** - Patterns and templates
4. **Git Configuration** - Workflow decisions
5. **User Preferences** - Stated preferences
6. **Future Work Ideas** - Backlog of ideas

---

## Getting Unstuck

If you don't remember a decision:
1. Check `memory/MEMORY.md` first
2. Search task files for context
3. Review git commit messages
4. Ask user to clarify

---

*This file is read at the start of each conversation. Keep it concise and actionable.*
