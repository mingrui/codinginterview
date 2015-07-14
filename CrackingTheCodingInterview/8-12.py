"""
8 queens

8 x 8 board, none of the queens share the same row, coloumn or diagonal
"""

# 1 details
# 2 work out example
"""
0. start at (0, 0) -> (0, 1) -> (0, 2) -> ... -> (0, 7)
1. put in one queen, mark row, coloumn and diagonal as not available
2. put in next queen in available space on board, then again mark out row, coloumn, diagonal as not available
3. recurse
"""
# 3 brute force solution

# 4 optimize using overlooked details
"""
1. stop after first row
"""
# 5 walk through optimized algorithm
# 6 implement
def Solve_Eight_Queens(board_result, row, col_result):
	if row == len(col_result):
 		board_result.append(col_result)
 	else:
 		for col in xrange(len(col_result)):
 			if Check_Valid(col_result, row, col) :
 				col_result_copy = col_result[:]
 				col_result_copy[row] = col
 				Solve_Eight_Queens(board_result, row+1, col_result_copy)

def Check_Valid(col_result, row, col):
	for r in xrange(row):
		# check column
		# column already taken by a previous row
		if col == col_result[r]:
			return False

		# check diagonal
		# column distance and row distance is the same
		if abs(col - col_result[r]) == abs(row - r):
			return False

	return True

# 7 test

BOARD_SIZE = 8
col_result = [0] * BOARD_SIZE
board_result = []
Solve_Eight_Queens(board_result, 0, col_result)
print len(board_result)