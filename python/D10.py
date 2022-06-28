"""
AoCd Day 10
https://adventofcode.com/2021/day/10
"""

import sys

with open(sys.argv[1]) as f:
	data = [l.strip() for l in f.readlines() if l.strip()]

illegal_points = {')': 3,']': 57,'}': 1197,'>': 25137}

def get_ill_char_point(data,illegal_points):
    ""
    illegal_chars = []
    for input in data:
        stack = []
        for char in input:
            is_gt = char == '>' and len(stack) > 0 and stack[-1] == '<'
            is_sq = char == ']' and len(stack) > 0 and stack[-1] == '['
            is_cl = char == '}' and len(stack) > 0 and stack[-1] == '{'
            is_ci = char == ')' and len(stack) > 0 and stack[-1] == '('
            if is_gt or is_sq or is_cl or is_ci:
                stack.pop()
            elif char in ['(', '[', '{', '<']:
                stack.append(char)
            else:
                illegal_chars.append(char)
                break
    return sum([illegal_points[char] for char in illegal_chars])



points = {')': 1,']': 2,'}': 3,'>': 4}
bracket_mapping = {'(': ')','[': ']','{': '}','<': '>'}

total_scores = []
for input in data:
    is_corrupt = False
    stack = []# Repeat of Part 1
    for char in input:
        is_gt = char == '>' and len(stack) > 0 and stack[-1] == '<'
        is_sq = char == ']' and len(stack) > 0 and stack[-1] == '['
        is_cl = char == '}' and len(stack) > 0 and stack[-1] == '{'
        is_ci = char == ')' and len(stack) > 0 and stack[-1] == '('
        if is_gt or is_sq or is_cl or is_ci:
            stack.pop()
        elif char in ['(', '[', '{', '<']:
            stack.append(char)
        else:
            is_corrupt = True
            break
    if is_corrupt:
        continue
    score = 0
    stack.reverse()
    for char in stack:
        score = score * 5 + points[bracket_mapping[char]]
    total_scores.append(score)
    
total_scores.sort()

result_1 = sum([illegal_points[char] for char in illegal_chars])
result_2 = total_scores[len(total_scores) // 2]

print(f"res_1={result_1}\nres_2={result_2}")
