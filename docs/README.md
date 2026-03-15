# IELTS Practice Repository

A comprehensive repository for structured IELTS practice with reading, writing, grammar, listening, and speaking modules.

## Repository Structure

```
IELTS_Practice/
├── *.py                        # Python utility scripts
├── docs/                       # Project documentation
│   ├── README.md              # Main documentation (this file)
│   ├── IELTS_ANNOTATOR_GUIDE.md
│   ├── MATERIAL-EXTRACTION-STANDARDS.md
│   ├── REVIEW-STRATEGY.md
│   ├── SPEAKING_100_TASKS.md  # 100-task speaking practice checklist
│   ├── TOOLS_SUMMARY.md
│   └── VALIDATION-REPORT.md
├── practice/                    # Practice materials
│   ├── README.md
│   ├── daily/                 # Daily practice records (organized by month)
│   │   ├── YYYY-MM/           # Month-based subdirectories
│   │   │   ├── YYYY-MM-DD-sync.md
│   │   │   ├── YYYY-MM-DD-noon-card.md
│   │   │   └── YYYY-MM-DD-evening-card.md
│   ├── reading/               # Reading practice materials
│   └── writing/               # Writing practice materials
├── notes/                      # Learning notes
│   ├── README.md
│   ├── grammar/               # Grammar notes
│   │   └── ielts-verb-phrases-idioms-2026-03-15.md
│   ├── listening/             # Listening notes
│   ├── summaries/             # Learning summaries
│   │   └── week-1-learning-summary-2026-03-15.md
│   ├── tech-notes/            # Technical notes
│   │   └── 什么算高质量Vibe Coding.md
│   └── writing-structures/     # Writing structure notes
├── progress/                   # Progress tracking
│   └── README.md
├── reference/                  # Reference materials
│   └── README.md
├── scripts/                    # Utility scripts
│   └── README.md
└── .sisyphus/                  # Task planning and scheduling
    ├── plans/                 # Task planning and scheduling
    ├── drafts/                # Design documentation
    └── notepads/              # Learning and progress tracking
```

## Module Guide

### Reading Module
- **Articles**: Authentic reading materials from various sources
- **Exercises**: Comprehension questions, vocabulary building, inference practice
- **Focus**: Academic reading skills, speed reading, comprehension accuracy

### Writing Module
- **Task 1**: Academic writing (describing charts, graphs, diagrams)
- **Task 2**: Essay writing (argumentative, discursive, problem-solution)
- **Focus**: Structure, coherence, vocabulary, grammar, task response

### Grammar Module
- **Exercises**: Topic-specific grammar practice
- **Rules**: Clear explanations of grammar concepts
- **Tests**: Progress assessments and improvement tracking

### Listening Module
- **Audio**: Authentic listening materials with transcripts
- **Exercises**: Multiple choice, fill-in-the-blank, note-taking practice
- **Focus**: Listening comprehension, accent recognition, detail extraction

### Speaking Module
- **Topics**: Cue cards, discussion questions, interview practice
- **Samples**: Model answers and responses
- **Focus**: Fluency, pronunciation, coherence, vocabulary range
- **100-Task Program**: [SPEAKING_100_TASKS.md](SPEAKING_100_TASKS.md) - Complete 4-week speaking practice schedule
- **Detailed Materials**: See [`口语练习材料/`](../口语练习材料/) for full task guides

## How to Use

### Setup
1. Install required dependencies (see Pandoc Installation section)
2. Place reference materials in the appropriate `reference/` subdirectories
3. Ensure audio files are placed in `modules/listening/audio/`

### Daily Practice
1. **Choose a module**: Select one module per day for focused practice
2. **Complete exercises**: Work through the materials in the chosen module
3. **Review mistakes**: Check answers and understand errors
4. **Track progress**: Update your progress in the `data/progress/` directory

### Weekly Review
1. **Review completed work**: Go through all exercises from the week
2. **Identify weaknesses**: Note areas needing improvement
3. **Plan next week**: Focus on weak areas and maintain strengths
4. **Update schedule**: Adjust your 4-week plan if needed

### Monthly Assessment
1. **Take full practice tests**: Simulate exam conditions
2. **Evaluate performance**: Score yourself and identify areas for improvement
3. **Adjust study plan**: Refocus based on assessment results
4. **Set new goals**: Establish targets for the next month

## 4-Week Task Schedule

### Week 1: Foundation Building
- **Day 1-2**: Reading Module - Introduction and basic exercises
- **Day 3-4**: Writing Module - Task 1 basics and structure
- **Day 5-6**: Grammar Module - Essential grammar review
- **Day 7**: Review and assessment

### Week 2: Skill Development
- **Day 8-9**: Reading Module - Advanced comprehension
- **Day 10-11**: Writing Module - Task 2 essay writing
- **Day 12-13**: Listening Module - Basic listening practice
- **Day 14**: Review and assessment

### Week 3: Integration Practice
- **Day 15-16**: Writing Module - Full task practice
- **Day 17-18**: Listening Module - Advanced listening
- **Day 19-20**: Speaking Module - Introduction to speaking
- **Day 21**: Review and assessment

### Week 4: Exam Simulation
- **Day 22-23**: Full reading and writing practice
- **Day 24-25**: Full listening and speaking practice
- **Day 26-27**: Timed practice tests
- **Day 28-30**: Final review and preparation

## Progress Tracking

### Daily Tracking
1. **Complete exercises**: Mark exercises as completed in your preferred format
2. **Note mistakes**: Record errors and corrections in a log file
3. **Time spent**: Log practice time for each module

### Weekly Tracking
1. **Update progress file**: Create weekly summary files in `data/progress/`
2. **Score exercises**: Give yourself scores for completed work
3. **Identify patterns**: Note recurring mistakes or improvements

### Monthly Tracking
1. **Practice test results**: Record scores from full practice tests
2. **Skill assessment**: Evaluate each module's improvement
3. **Goal setting**: Set new targets for the following month

### File Format for Progress Tracking
```
Progress files should be in .md format with the following structure:
# Week [Number] Progress
## Reading
- Completed exercises: [count]
- Average score: [percentage]
- Areas for improvement: [list]

## Writing
- Essays completed: [count]
- Average score: [percentage]
- Areas for improvement: [list]

## Grammar
- Exercises completed: [count]
- Average score: [percentage]
- Areas for improvement: [list]

## Listening
- Listening exercises: [count]
- Average score: [percentage]
- Areas for improvement: [list]

## Speaking
- Practice sessions: [count]
- Areas for improvement: [list]
```

## Reference Materials

### Supported Formats
- **.md files**: Markdown format for easy reading and editing
- **.txt files**: Plain text format for simple reference
- **.epub files**: E-book format (auto-converted to .md using scripts/auto-convert.sh)
- **.pdf files**: PDF format (auto-converted to .md using scripts/auto-convert.sh)

### File Organization
- **Reading**: Place articles and reading materials in `reference/reading/`
- **Writing**: Place sample essays and writing guides in `reference/writing/`
- **Grammar**: Place grammar rules and exercises in `reference/grammar/`
- **Listening**: Place transcripts and listening materials in `reference/listening/`
- **Speaking**: Place speaking topics and samples in `reference/speaking/`

### Conversion Process
1. Place .epub or .pdf files in the appropriate reference directory
2. Run the auto-conversion script: `./scripts/auto-convert.sh`
3. Check converted files in the corresponding directory
4. Review converted content for accuracy

## Pandoc Installation

### Prerequisites
- Install Pandoc: Download from [https://pandoc.org/installing.html](https://pandoc.org/installing.html)
- Install Python 3.6+ for script execution

### Installation Commands

#### Ubuntu/Debian
```bash
# Install Pandoc
sudo apt-get update
sudo apt-get install pandoc

# Install Python dependencies
pip install pandoc
```

#### macOS
```bash
# Install Pandoc using Homebrew
brew install pandoc

# Install Python dependencies
pip install pandoc
```

#### Windows
```bash
# Install Pandoc using Chocolatey
choco install pandoc

# Install Python dependencies
pip install pandoc
```

### Verification
```bash
# Check Pandoc installation
pandoc --version

# Test the auto-conversion script
./scripts/auto-convert.sh --help
```

### Usage
```bash
# Convert all .epub files in reference directory
./scripts/auto-convert.sh

# Convert specific file
./scripts/auto-convert.sh reference/reading/material.epub

# Check conversion status
./scripts/auto-convert.sh --status
```

### Troubleshooting
- Ensure Pandoc is installed and accessible in PATH
- Check file permissions for the conversion script
- Verify input files are not corrupted
- Review conversion logs for errors