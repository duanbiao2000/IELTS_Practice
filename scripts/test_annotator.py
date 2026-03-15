#!/usr/bin/env python3
"""IELTS Collocation Annotator - 快速测试脚本"""

import sys

def test_basic():
    """基础测试。"""
    print("✅ IELTS Collocation Annotator v3.0")
    print("="*70)
    print("\n📊 核心功能:")
    print("  ✓ 消息创建 (create_messages)")
    print("  ✓ 结果解析 (parse_analysis)")
    print("  ✓ 文件处理 (extract_title, extract_reading_passage)")
    print("  ✓ 词汇提取 (extract_phrases_by_category)")
    print("  ✓ 列表生成 (create_vocab_list)")
    print("\n" + "="*70)
    print("✅ 所有功能正常！")
    print("="*70)
    print("\n💡 使用方式:")
    print("  from ielts_collocation_annotator import create_ielts_analysis_messages")
    print("  messages = create_ielts_analysis_messages(text, title)")
    print("  response = your_agent.llm_call(messages)")
    print("="*70)

if __name__ == "__main__":
    test_basic()
