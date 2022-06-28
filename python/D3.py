"""
AoCd Day 3
https://adventofcode.com/2021/day/3
"""
import sys

with open(sys.argv[1]) as f:
	data = [l.strip() for l in f.readlines() if l.strip()]

#1
def mcb(data: list, local_value: int) -> int:
    "find most common bit"
    if sum([int(i[local_value]) for i in data]) / len(data) > 0.5:
        mcb = 1
    elif sum([int(i[local_value]) for i in data]) / len(data) == 0.5:
        mcb = 1
    else:
        mcb = 0
    return mcb

#2
def lcb(data: list, local_value: int) -> int:
    "find least common bit"
    if sum([int(i[local_value]) for i in data]) / len(data) < 0.5:
        mcb = 1
    elif sum([int(i[local_value]) for i in data]) / len(data) == 0.5:
        mcb = 0
    else:
        mcb = 0
    return mcb

def filter_criteria(data: list, cycle: int, criteria: int):
    ""
    filter_list = []
    for i in range(len(data)):
        if int(data[i][cycle]) == criteria:
            filter_list.append(data[i])
    return filter_list

def get_rating(data: list, occurance_type: str):
    ""
    filtered_list = data
    for cycle in range(len(filtered_list[0])):
        if occurance_type == 'mcb':
            criteria = mcb(filtered_list,cycle)
            filtered_list = filter_criteria(filtered_list,cycle,criteria)
            if len(filtered_list) == 1:
                return int(str(filtered_list[0]),2)
        if occurance_type == 'lcb':
            criteria = lcb(filtered_list,cycle)
            filtered_list = filter_criteria(filtered_list,cycle,criteria)
            if len(filtered_list) == 1:
                return int(str(filtered_list[0]),2)

gamma = [str(mcb(data, i)) for i in range(len(data[0]))]
epsilon = ''.join('1' if x == '0' else '0' for x in gamma)

oxygen_generator_rating = get_rating(data,'mcb')
CO2_scrubber_rating = get_rating(data,'lcb')

result_1 = int(''.join(gamma),2) * int(epsilon,2)
result_2 = oxygen_generator_rating * CO2_scrubber_rating

print(f"res_1={result_1}\nres_2={result_2}")
