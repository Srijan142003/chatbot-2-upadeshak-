#!/usr/bin/env python3
"""Test the new formatting for different sources."""

from retriever import retrieve, format_passages_for_prompt

# Test 1: Bhagavad Gita
print('TEST 1 - BHAGAVAD GITA QUERY:')
print('='*80)
passages = retrieve('I have a career dilemma', top_k=2)
print(format_passages_for_prompt(passages))

print('\n\nTEST 2 - GENERAL WISDOM QUERY:')
print('='*80)
passages = retrieve('How should I handle obstacles?', top_k=2)
print(format_passages_for_prompt(passages))
