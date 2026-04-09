#!/usr/bin/env python3
"""Test formatting for Chanakya, Vidura, and Hitopadesha sources."""

from retriever import _retrieve_legacy, format_passages_for_prompt

# Test with legacy retriever which doesn't filter by taxonomy
print('TEST: LEGACY RETRIEVER (All Sources):')
print('='*80)
passages = _retrieve_legacy('wisdom and strategy', top_k=5)

# Filter to show only non-Bhagavad Gita sources
non_bg = [p for p in passages if "Bhagavad Gita" not in p.source]

if non_bg:
    print("Non-Bhagavad Gita passages found:")
    print(format_passages_for_prompt(non_bg[:3]))
else:
    print("No non-BG passages in this retrieval. Let me try the full set:")
    print(format_passages_for_prompt(passages[:3]))
