"""
AoCd Day 4
https://adventofcode.com/2021/day/4
"""

import sys
import numpy as np

with open(sys.argv[1]) as f:
	data = [l.strip() for l in f.readlines() if l.strip()]

def find_first_bingo(draw_list, board_list):
    "returns last drawed number and winner bingo board"
    for draw in draw_list:
        for board in board_list:
            board[board == draw] = 'X'
            #print(board)
            for row in board:
                if (row == 'X').sum() == 5:
                    board[board == 'X'] = 0
                    return int(draw), board.astype(int)
            for col in board.T:
                if (col == 'X').sum() == 5:
                    board[board == 'X'] = 0
                    return int(draw), board.astype(int)
#2                
def find_last_board(draw_list, board_list):
    winner_set = set()
    for draw in draw_list: 
        for i, board in enumerate(board_list):
            board[board == draw] = 'X'
            for row in board:
                if (row == 'X').sum() == 5:
                    winner_set.add(i)
            for col in board.T:
                if (col == 'X').sum() == 5:
                    winner_set.add(i)
            if len(winner_set) == len(board_list):
                board[board == 'X'] = 0
                return int(draw), board.astype(int)

with open(sys.argv[1]) as f:
	draw_list = [l.strip() for l in f.readlines() if l.strip()][0].split(",")

with open(sys.argv[2]) as f:
	board_list = [l.strip() for l in f.readlines() if l.strip()]

chunked_list = [board_list[i: i + 5] for i in range(0, len(board_list), 5)]
board_matrices = [np.stack([r.split() for r in i]) for i in chunked_list]

#winner board
last_draw, winner_board = find_first_bingo(draw_list, board_matrices)
result_1 = last_draw * winner_board.astype(int).sum()

#last board
last_draw, last_board = find_last_board(draw_list, board_matrices)
result_2 = last_draw * last_board.sum()

print(f"res_1={result_1}\nres_2={result_2}")
