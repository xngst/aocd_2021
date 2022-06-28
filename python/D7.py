"""
AoCd Day 7
https://adventofcode.com/2021/day/7
"""
import sys

#D7
def cheapest_common_hline(data):
    ""
    range_max = max(data)
    cost_dict = {}
    for i in range(range_max):
        full_cost = 0
        for d in data:
            cost = abs(d-i)
            full_cost += cost
        cost_dict[i] = full_cost
    return min(cost_dict.values())

def cheapest_common_weighed_hline(data):
    """
    Instead, each change of 1 step in horizontal position
    costs 1 more unit of fuel than the last:
      the first step costs 1, the second step costs 2,
      the third step costs 3, and so on.
    """
    range_max = max(data)
    cost_dict = {}
    for i in range(range_max):
        full_cost = 0
        for d in data:
            cost = sum(list(range(1,abs(d-i)+1)))
            full_cost += cost
        cost_dict[i] = full_cost
    return min(cost_dict.values())

with open(sys.argv[1]) as f:
	data = [l.strip() for l in f.readlines() if l.strip()]
data = [int(d) for d in data[0].split(',')]

res_1 = cheapest_common_hline(data)
res_2 = cheapest_common_weighed_hline(data)

print(f"res_1={result_1}\nres_2={result_2}")
