# Scripts and Automation

This directory contains automation scripts, data processing tools, and utilities for IELTS repository management.

## Structure

- `conversion/` - File format conversion scripts
- `analysis/` - Data analysis and progress reporting scripts
- `export/` - Export and backup utilities
- `utilities/` - Helper scripts and functions

## Available Scripts

### File Conversion
- `auto-convert.sh` - Automatically converts uploaded PDFs/EPUBs to markdown format
- `format-cleaner.py` - Cleans and standardizes formatted text
- `extract-images.py` - Extracts and organizes images from documents

### Progress Analysis
- `progress-report.py` - Generates weekly progress summaries
- `score-trend.py` - Analyzes score trends over time
- `weakness-analyzer.py` - Identifies consistent problem areas

### Data Export
- `export-to-pdf.py` - Exports study materials to PDF format
- `backup-script.sh` - Regular backup of repository data
- `sync-script.py` - Synchronizes with cloud storage

## Usage

### Running Scripts
```bash
# Run conversion script
./auto-convert.sh

# Generate progress report
python progress-report.py

# Create backup
./backup-script.sh
```

### Adding New Scripts

1. Place scripts in appropriate subdirectory
2. Add executable permissions: `chmod +x script-name`
3. Update documentation in this README
4. Test script thoroughly before use

## Integration Scripts

Scripts are designed to work together:
- Conversion scripts produce content for practice materials
- Analysis scripts read practice results for progress tracking
- Export scripts can format materials for different devices
- Backup scripts ensure data safety and portability