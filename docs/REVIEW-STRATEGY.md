# IELTS Review Strategy: Ebbinghaus Forgetting Curve Implementation

## Overview

This document outlines the review strategy based on the Ebbinghaus forgetting curve to optimize retention of IELTS skills and knowledge throughout the 4-week intensive sprint. The strategy implements spaced repetition with 4 review rounds scheduled at optimal intervals to combat memory decay.

## Ebbinghaus Forgetting Curve

The Ebbinghaus forgetting curve demonstrates that information is lost over time when there is no attempt to retain it. To combat this, we implement a structured review schedule with the following intervals:

| Review Round | Interval | Purpose |
|-------------|----------|---------|
| **R1** | **1 day** after initial learning | Reinforce immediate recall and solidify new information |
| **R2** | **3 days** after initial learning | Strengthen memory before significant decay |
| **R3** | **7 days** after initial learning | Consolidate long-term memory formation |
| **R4** | **14 days** after initial learning | Ensure permanent retention and mastery |

This 4-round review system follows the optimal spacing intervals identified by research on memory retention, maximizing learning efficiency while minimizing review fatigue.

## Review Content

Each review round focuses on different aspects of IELTS preparation, progressively building from basic recall to comprehensive mastery.

### R1: Daily Review (1 Day After)
**Focus**: Vocabulary, phrases, and basic concepts
- Review all new vocabulary learned in the previous day
- Practice pronunciation and usage of key phrases
- Reinforce grammatical structures introduced
- Quick recall of reading/writing techniques covered
- Self-assessment of understanding level

### R2: Task Type Review (3 Days After)
**Focus**: Task types and specific techniques
- Review strategies for each IELTS task type (Listening, Reading, Writing, Speaking)
- Practice applying techniques to sample questions
- Identify and address common mistakes
- Reinforce timing strategies and pacing
- Review feedback from previous practice sessions

### R3: Error Analysis Review (7 Days After)
**Focus**: Comprehensive error identification and correction
- Analyze mistakes from previous practice tests
- Review weak areas and common errors
- Develop targeted improvement strategies
- Reinforce correct approaches and methodologies
- Track progress on specific skill deficiencies

### R4: Comprehensive Review (14 Days After)
**Focus**: Full integration and mastery
- Complete review of all materials covered in the 2-week period
- Practice full-length mock tests
- Assess overall progress and readiness
- Identify remaining gaps in knowledge
- Develop final preparation strategies

## How to Track Reviews

### Manual Tracking System
Reviews are tracked manually using a combination of:
- **Review Logs**: Create dedicated review entries in the `practice/reviews/` directory
- **Task Scheduling**: Tag review tasks in weekly schedules with R1/R2/R3/R4 indicators
- **Progress Monitoring**: Maintain a review tracking spreadsheet or document

### Review Documentation
Each review should include:
- Date of original learning
- Review round (R1-R4)
- Specific content covered
- Time spent on review
- Key insights or improvements
- Areas still needing attention

### Organization Structure
```
practice/
├── reviews/
│   ├── vocabulary/
│   ├── task-types/
│   ├── error-analysis/
│   └── comprehensive/
└── schedules/
    └── weekly/
```

## Review Schedule Template

### Weekly Review Integration
Incorporate reviews into your weekly schedule with the following structure:

```
Monday: 
- New content learning (Listening, Reading, Writing, Speaking)
- R1 reviews from Sunday's learning

Tuesday:
- Continue new content
- R1 reviews from Monday's learning

Wednesday:
- New content + mid-week assessment
- R2 reviews (3-day intervals)

Thursday:
- New content
- R1 reviews from Wednesday's learning

Friday:
- New content + weekly review
- R3 reviews (7-day intervals)

Saturday:
- Practice test + comprehensive review
- R4 reviews (14-day intervals)

Sunday:
- Rest day or light review
- Plan for next week
```

### Daily Review Time Allocation
- **R1 Reviews**: 15-20 minutes per subject
- **R2 Reviews**: 20-25 minutes per subject  
- **R3 Reviews**: 30-35 minutes per subject
- **R4 Reviews**: 45-60 minutes per subject

## Review Entry Examples

### Example 1: Vocabulary Review (R1)
```
Date: 2024-01-15
Review Round: R1
Original Learning: 2024-01-14
Subject: Vocabulary - Academic Word List 1-10
Time Spent: 18 minutes
Content Reviewed:
- All 50 words from AWL 1-10
- Pronunciation practice for difficult words
- Example sentences for 10 key phrases
- Self-test: 45/50 words recalled correctly
Insights:
- Still struggling with words 23, 37, 42
- Need more context examples for technical terms
Next Steps:
- Create flashcards for missed words
- Add 2-3 example sentences for each
```

### Example 2: Task Type Review (R2)
```
Date: 2024-01-17
Review Round: R2
Original Learning: 2024-01-14
Subject: Listening Task Types
Time Spent: 25 minutes
Content Reviewed:
- Multiple Choice questions: strategy reinforcement
- Matching questions: timing improvement
- Note Completion: common pitfalls identified
- Practice with 2 sample questions per type
Insights:
- Improved accuracy in Multiple Choice (85% vs 70%)
- Still slow on Note Completion - need more practice
Next Steps:
- Focus on Note Completion timing for next session
- Review answer strategies for trick questions
```

## Review Integration with Task Schedules

### Task Tagging System
In weekly schedules, tag each task with the appropriate review indicator:

```
# Monday Schedule
- Listening Practice: Section 1 (R1)
- Reading Practice: True/False/Not Given (R1)
- Writing Task 1: Bar Chart Analysis (New)
- Speaking Practice: Part 1 Questions (R1)
```

### Review Frequency Guidelines
- **Daily Reviews (R1)**: Tag all tasks from previous day's learning
- **3-Day Reviews (R2)**: Tag tasks learned 3 days prior
- **7-Day Reviews (R2)**: Tag tasks learned 7 days prior  
- **14-Day Reviews (R4)**: Tag tasks learned 14 days prior

### Schedule Integration Example
```
# Week 1 Schedule
Monday:
- Listening: Section 1 Practice (R1)
- Reading: True/False/Not Given (R1)
- Writing: Task 1 Bar Chart (New)
- Speaking: Part 1 Questions (R1)

Tuesday:
- Listening: Section 2 Practice (R1)
- Reading: Matching Headings (R1)
- Writing: Task 2 Opinion Essay (New)
- Speaking: Part 2 Cue Card (R1)

Wednesday:
- Listening: Section 3 Practice (R1)
- Reading: Matching Information (R1)
- Writing: Task 1 Process Diagram (New)
- Speaking: Part 3 Discussion (R1)
- Review: Listening Task Types (R2 - 3-day review)
```

## Best Practices

1. **Consistency**: Maintain regular review schedule without skipping rounds
2. **Active Recall**: Use self-testing rather than passive review
3. **Spaced Repetition**: Follow the specified intervals strictly
4. **Progress Tracking**: Document improvements and areas needing work
5. **Adaptation**: Adjust review focus based on performance data
6. **Integration**: Seamlessly incorporate reviews into weekly schedules

This review strategy ensures optimal retention of IELTS skills and knowledge, maximizing learning efficiency throughout the intensive 4-week preparation period.