"""
Sorted Matrix Search

Given an M x N matrix in which each row and each column is sorted in ascending
order, write a method to find an element.
"""
"""
5 5
1  2  3  4  5
3  7  8  9 11
5  9 10 17 18
7 12 15 19 23
9 13 16 20 25
"""

aMatrix = [[1, 2, 3, 4, 5],
		   [3, 7, 8, 9, 11],
		   [5, 9, 10, 17, 18],
		   [7, 12, 15, 19, 23],
		   [9, 13, 16, 20, 25]]

# first solution
def SortedMatrixSearch(aMatrix, value):
	row = 0
	col = len(aMatrix[0]) - 1
	while row < len(aMatrix) and col >= 0 :
		if aMatrix[row][col] == value :
			return [row, col]
		elif aMatrix[row][col] > value :
			col -= 1
		else:
			row += 1
	return -1

print SortedMatrixSearch(aMatrix, 10)

# binary search solution