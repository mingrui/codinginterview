"""
Rotate Matrix

Given an image represented by an N * N matrix, where each pixel in the image is 4 bytes, write
a method to rotate the image by 90 degrees. 
Try to do this in place
"""

# 1 details
# 2 example
"""
matrix
1 2
3 4

after rotation
3 1
4 2

matrix
1 2 3
4 5 6
7 8 9

after rotation
7 4 1
8 5 2
9 6 3

matix
 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 15 16

after rotation
13  9  5  1
14 10  6  2
15 11  7  3
16 12  8  4
"""
# 3 1st solution
"""
0 <= x <= N-1, 0 <= y <= N-1
M[x][y] = M[N-y][x]
"""
# 4 optimize
"""
swap in layers
for i = 0 to n:
	temp = top[i]
	top[i] = left[i]
	left[i] = bottom[i]
	bottom[i] = right[i]
	right[i] = temp
"""
# 5 validate
# 6 implement
def Rotate(matrix, n):
	for layer in xrange(n/2):
		first = layer
		last = n - 1 - layer
		i = first
		while i < last:
			offset = i - first
			top = matrix[first][i]
			matrix[first][i] = matrix[last-offset][first]
			matrix[last-offset][first] = matrix[last][last - offset]
			matrix[last][last-offset] = matrix[i][last]
			matrix[i][last] = top
			i += 1

# 7 test
n = 4
matrix = [[0 for x in xrange(n)] for x in range(n)]
i = 1
for r in xrange(n):
	for c in xrange(n):
		matrix[r][c] = i
		i += 1
print matrix
Rotate(matrix, n)
print matrix




