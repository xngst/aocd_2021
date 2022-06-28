"""
AoCd Day 1
https://adventofcode.com/2021/day/1
"""
import sys

with open(sys.argv[1]) as f:
	d = [int(l.strip()) for l in f.readlines() if l.strip()]

result_1 = len([i for i in range(len(d) - 1) if d[i] < d[i + 1]])
result_2 = len([i for i in range(len(d)) if sum(d[i:i+3]) < sum(d[i+1: i+4])])

print(f"res_1={result_1}\nres_2={result_2}")
