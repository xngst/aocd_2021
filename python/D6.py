"""
AoCd Day 6
https://adventofcode.com/2021/day/6
"""
import sys

def get_fish_population(init_pop:list, days:int):
    "calculates pupulation of fishes after n days"
   
    a_d = {}
   
    for i in range(9):
        a_d[i] = init_pop.count(i)
       
    for i in range(days):
        null_c = a_d[0]
        a_d[0] = a_d[1]
        a_d[1] = a_d[2]
        a_d[2] = a_d[3]
        a_d[3] = a_d[4]
        a_d[4] = a_d[5]
        a_d[5] = a_d[6]
        a_d[6] = a_d[7] + null_c
        a_d[7] = a_d[8]
        a_d[8] = null_c
       
    return sum(a_d.values())

with open(sys.argv[1]) as f:
	data = [l.strip() for l in f.readlines() if l.strip()]
	
lines = [int(l) for l in data[0].split(',')]

res_1 = get_fish_population(lines,80)
res_2 = get_fish_population(lines,256)

print(f"res_1={result_1}\nres_2={result_2}")
