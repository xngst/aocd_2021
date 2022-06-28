"""
AoCd Day 9
https://adventofcode.com/2021/day/9
"""
import sys
import numpy as np
from scipy import ndimage

def low_pont_matrix(data, orienation):
    ""
    if orienation == "row":
        low_pont_matrix = np.zeros((len(data),len(data[0])))
       
    if orienation == "column":
        low_pont_matrix = np.zeros((len(data[0]),len(data)))
        data = data.T
       
    row_count = 0
   
    for row in data:
        for i in range(len(row)):
            if i == 0: #left edge
                if row[i] < row[i+1]:
                    low_pont_matrix[row_count,i] = 1

            if i == len(row) - 1: #right edge
                if int(row[i-1]) > int(row[i]):
                    low_pont_matrix[row_count,i] = 1

            if i != 0 and i != len(row) - 1:
                if int(row[i-1]) > int(row[i]) < int(row[i+1]):
                    low_pont_matrix[row_count,i] = 1
                   
        row_count += 1
       
    return low_pont_matrix

with open(sys.argv[1]) as f:
	data = [l.strip() for l in f.readlines() if l.strip()]
	
data_matrix = np.array([[int(i) for i in row] for row in data])
row_matrix = low_pont_matrix(data_matrix,orienation="row")
col_matrix = low_pont_matrix(data_matrix,orienation="column")
blend_matrix = row_matrix + col_matrix.T
result_1 = sum(data_matrix[blend_matrix > 1] + 1)

label, num_label = ndimage.label(data_matrix < 9)
size = np.bincount(label.ravel())
top3 = sorted(size[1:], reverse=True)[:3]
result_2 = np.prod(top3)

print(f"res_1={result_1}\nres_2={result_2}")
