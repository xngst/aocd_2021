"""
AoCd Day 5
https://adventofcode.com/2021/day/5
"""

import sys
import numpy as np 

def get_dimension(lines):
    ""
    max_x = 0
    max_y = 0
   
    for line in lines:
       
        x1, y1 = line.split(' -> ')[0].split(',')
        x2, y2 = line.split(' -> ')[1].split(',')
       
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
       
        if y1 > max_y:
            max_y = y1
        if y2 > max_y:
            max_y = y2
        if x1 > max_x:
            max_x = x1
        if x2 > max_x:
            max_x = x2  
    return (max_y+1,max_x+1)

def get_vent_matrix(vent_lines: list, dimension: tuple, diagonal=False):
    ""
    base_matrix = np.zeros(dimension)

    for line in vent_lines:

        x1, y1 = line.split(' -> ')[0].split(',')
        x2, y2 = line.split(' -> ')[1].split(',')

        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        
        #vertical
        if x1 == x2:
            if y1 > y2:
                v_vect = tuple(range(y1, y2-1,-1))
            else:
                v_vect = tuple(range(y1, y2+1))
            base_matrix[v_vect,x1] = base_matrix[v_vect,x1] + 1
        
        #horizontal
        if y1 == y2:
            if x1 > x2:
                h_vect = tuple(range(x1,x2-1,-1))
            else:
                h_vect = tuple(range(x1, x2+1))
            
            base_matrix[y1,h_vect] = base_matrix[y1,h_vect] + 1
            
        #diagonal
        if diagonal:
            if abs(x1-x2) == abs(y1-y2):

                if x1 > x2:
                    x_list = list(range(x1,x2-1,-1))
                if x1 < x2:
                    x_list = list(range(x1,x2+1))
                if y1 > y2:
                    y_list = list(range(y1,y2-1,-1))
                if y1 < y2:
                    y_list = list(range(y1,y2+1))

                for yx in list(zip(y_list,x_list)):
                    base_matrix[yx] = base_matrix[yx] + 1

        else:
            #no line
            pass 
    return base_matrix

with open(sys.argv[1]) as f:
	lines = [l.strip() for l in f.readlines() if l.strip()]
	
vent_matrix = get_vent_matrix(lines,get_dimension(lines),diagonal=False)
res_1 = np.count_nonzero(vent_matrix > 1)

vent_matrix = get_vent_matrix(lines,get_dimension(lines),diagonal=True)
res_2 = np.count_nonzero(vent_matrix > 1)

print(f"res_1={result_1}\nres_2={result_2}")
