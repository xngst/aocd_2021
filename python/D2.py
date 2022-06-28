"""
AoCd Day 2
https://adventofcode.com/2021/day/2
"""
import sys

with open(sys.argv[1]) as f:
	data = [l.strip() for l in f.readlines() if l.strip()]

def sumif(data, crit):
    return sum([int(i[-1: ]) for i in data if i.startswith(str(crit))])

print(sumif(data,"f"))
print(sumif(data,"d"))
print(sumif(data,"u"))

result_1 = sumif(data,"f") * (sumif(data,"d") - sumif(data,"u"))

h = 0 #horizontal
d = 0 #depth
a = 0 #aim

for i in data:
    if i.startswith("f"):
        h += int(i[-1: ])
        d += a * int(i[-1: ])
    if i.startswith("u"):
        a -= int(i[-1: ])
    if i.startswith("d"):
        a += int(i[-1: ])

result_2 = h * d

print(f"res_1={result_1}\nres_2={result_2}")
