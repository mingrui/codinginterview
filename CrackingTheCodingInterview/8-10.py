"""
Paint Fill

Fill in surrounding area
"""
# 1 notice details
# 2 work on example
# 3 brute force solution
# 4 optimize using overlooked details
# 5 walk through optimized algorithm
# 6 implement
def Paint_Fill(color_coord, row, col, new_color):
	if color_coord[row][col] == new_color :
		return
	else:
		Paint_Fill_Work(color_coord, row, col, color_coord[row][col], new_color)

def Paint_Fill_Work(color_coord, row, col, old_color, new_color):
	if row < 0 or row > len(color_coord)-1 or col < 0 or col > len(color_coord[0])-1 :
		return

	if color_coord[row][col] == old_color:
		color_coord[row][col] = new_color
		Paint_Fill_Work(color_coord, row-1, col, old_color, new_color)
		Paint_Fill_Work(color_coord, row+1, col, old_color, new_color)
		Paint_Fill_Work(color_coord, row, col-1, old_color, new_color)
		Paint_Fill_Work(color_coord, row, col+1, old_color, new_color)

# 7 test
color_coord = [[0 for x in xrange(5)] for x in xrange(5)]
color_coord[0][1] = 2
color_coord[1][2] = 2
Paint_Fill(color_coord, 1, 1, 1)
print color_coord