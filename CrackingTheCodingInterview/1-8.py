"""
Zero Matrix

Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0
"""

# 1 details
# 2 example
# 3 1st solution
"""
1. go through matrix row by row, encounter 0, record [r][c], stop and go to next row
2. with the record, change [r] and [c] to 0
"""
# 4 optimize
# 5 proof
# 6 implement
def Zero_Matrix(matrix):
	# check first row and first column 0
	firstRowZero = False
	firstColZero = True
	for c in xrange(len(matrix[0])) :
		if matrix[0][c] == 0 :
			firstRowZero = True
			break

	for r in xrange(len(matrix)) :
		if matrix[r][0] == 0 :
			firstColZero = True
			break

	# check other rows and cols
	for r in xrange(1, len(matrix[0])) :
		for c in xrange(1, len(matrix)) :
			if matrix[r][c] == 0 :
				matrix[r][0] == 0
				matrix[0][c] == 0

	# nullify rows and cols
	# nullify first row and first col

# 7 test