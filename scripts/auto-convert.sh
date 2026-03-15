#!/bin/bash

# auto-convert.sh - Auto-convert EPUB and PDF files to Markdown using pandoc
# Created: 2025-02-06
# Purpose: Automatically convert reference documents to markdown format

# Set working directory to reference/
cd /mnt/d/MyDocs/IELTS_Practice/reference

# Initialize conversion files if they don't exist
if [ ! -f conversion-log.md ]; then
    echo "# Conversion Log" > conversion-log.md
    echo "Created: $(date '+%Y-%m-%d')" >> conversion-log.md
    echo "Purpose: Track all file conversion attempts and results" >> conversion-log.md
    echo "" >> conversion-log.md
    echo "## Conversion History" >> conversion-log.md
    echo "" >> conversion-log.md
fi

if [ ! -f conversion-status.md ]; then
    echo "# Conversion Status" > conversion-status.md
    echo "" >> conversion-status.md
    echo "## 最近转换记录" >> conversion-status.md
    echo "" >> conversion-status.md
    echo "| 原始文件 | 转换后文件 | 状态 | 转换时间 | 备注 |" >> conversion-status.md
    echo "|----------|------------|------|----------|------|" >> conversion-status.md
    echo "" >> conversion-status.md
    echo "## 转换错误" >> conversion-status.md
    echo "" >> conversion-status.md
    echo "| 文件 | 错误时间 | 错误信息 | 处理方式 |" >> conversion-status.md
    echo "|------|----------|----------|----------|" >> conversion-status.md
    echo "" >> conversion-status.md
    echo "## 统计信息" >> conversion-status.md
    echo "- 总转换次数: 0" >> conversion-status.md
    echo "- 成功次数: 0" >> conversion-status.md
    echo "- 失败次数: 0" >> conversion-status.md
fi

echo "Starting auto-conversion process..."
echo "====================================="

# Function to log conversions
log_conversion() {
    local original_file="$1"
    local converted_file="$2"
    local status="$3"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    
    # Append to conversion log
    echo "[$timestamp] $status: $original_file → $converted_file" >> conversion-log.md
    
    # Also add to status table
    echo "| $original_file | $converted_file | $status | $timestamp | - |" >> conversion-status.md
}

# Initialize conversion files
echo "# Conversion Log" > reference/conversion-log.md
echo "# Conversion Status" > reference/conversion-status.md

# EPUB Conversion
echo "Processing EPUB files..."
echo "----------------------"

# Loop through all .epub files
for epub in *.epub; do
    if [ -f "$epub" ]; then
        echo "Found EPUB: $epub"
        
        # Check if already converted
        if [ ! -f "${epub}-converted.md" ]; then
            echo "Converting $epub to Markdown..."
            pandoc "$epub" -o "${epub}-converted.md"
            
            if [ $? -eq 0 ]; then
                echo "✅ Successfully converted: $epub → ${epub}-converted.md"
                log_conversion "$epub" "${epub}-converted.md" "✅ 成功"
            else
                echo "❌ Failed to convert EPUB: $epub"
                log_conversion "$epub" "FAILED" "❌ 失败"
            fi
        else
            echo "⏭️  Already converted: $epub"
            log_conversion "$epub" "${epub}-converted.md" "⏭️ 跳过"
        fi
    fi
done

echo ""
echo "Processing PDF files..."
echo "---------------------"

# Loop through all .pdf files
for pdf in *.pdf; do
    if [ -f "$pdf" ]; then
        echo "Found PDF: $pdf"
        
        # Check if already converted to markdown
        if [ ! -f "${pdf}-converted.md" ]; then
            echo "Converting $pdf to Markdown..."
            pandoc "$pdf" -o "${pdf}-converted.md"
            
            if [ $? -eq 0 ]; then
                echo "✅ Successfully converted: $pdf → ${pdf}-converted.md"
                log_conversion "$pdf" "${pdf}-converted.md" "✅ 成功"
            else
                echo "❌ Markdown conversion failed, trying plain text fallback..."
                pandoc "$pdf" -o "${pdf}-converted.txt" -t plain
                
                if [ $? -eq 0 ]; then
                    echo "✅ Successfully converted to plain text: $pdf → ${pdf}-converted.txt"
                    log_conversion "$pdf" "${pdf}-converted.txt" "✅ 成功 (纯文本)"
                else
                    echo "❌ Failed to convert PDF: $pdf"
                    log_conversion "$pdf" "FAILED" "❌ 失败"
                fi
            fi
        else
            echo "⏭️  Already converted: $pdf"
            log_conversion "$pdf" "${pdf}-converted.md" "⏭️ 跳过"
        fi
    fi
done

echo ""
echo "====================================="
echo "Auto-conversion process completed!"
echo "====================================="

# Display summary
echo ""
echo "Conversion Summary:"
echo "-----------------"
if [ -f conversion-log.md ]; then
    echo "📄 Log file: conversion-log.md"
    echo "📊 Status file: conversion-status.md"
    
    # Count conversions from log
    total_conversions=$(grep -c "✅ 成功" conversion-log.md 2>/dev/null || echo "0")
    failed_conversions=$(grep -c "❌ 失败" conversion-log.md 2>/dev/null || echo "0")
    
    echo "📈 Total conversions: $total_conversions"
    echo "❌ Failed conversions: $failed_conversions"
fi

echo ""
echo "Note: Original EPUB and PDF files have been preserved."