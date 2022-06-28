"""
AoCd Day 10
https://adventofcode.com/2021/day/10
r1 = 413733
r2 = 3354640192
"""
import sys

def bad_syntax_value(line: str, points: dict, mapping: dict) -> int:
    check_stack = [ ]
    for char in line:
        if char in mapping.keys():
            if check_stack.pop() != mapping[char]:
                return points[char]
        else:
            check_stack.append(char)
    return 0

fail_points = {")":3,"]":57,"}":1197,">":25137}
autocomplete_points = {")":1,"]":2,"}":3,">":4}

open_mapping = {")":"(","]":"[",">":"<","}":"{"}
close_mapping = {"(":")","[":"]","<":">","{":"}"}

with open(sys.argv[1]) as data:
    result_1 = sum([bad_syntax_value(line, fail_points, open_mapping) for line in data.readlines()])

with open(sys.argv[1]) as data:
    score_list = [ ]
    for line in data.readlines():
        value = bad_syntax_value(line, fail_points, open_mapping)
        if value == 0:
            check_stack = [ ]
            for char in line.strip():
                if char in open_mapping.keys():
                    check_stack.pop()
                else:
                    check_stack.append(char)

            close_braces = list(reversed([close_mapping[brace] for brace in check_stack]))
            line_score = 0
            for brace in close_braces:
                line_score = (5 * line_score) + autocomplete_points[brace]
            score_list.append(line_score)
result_2 = sorted(score_list)[len(score_list) // 2]

print(f"res_1={result_1}\nres_2={result_2}")
