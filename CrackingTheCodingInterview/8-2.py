"""
grid of r rows and c columns
robot in the upper left corner, can only move right and down
certain cells are "off limits" or a wall
find a path to bottom right corner

* = wall
  = empty cell
V = path
X = dead end
S = Start
E = End
"""

def Check_Cell(map_grid, r, c):
	return map_grid[r][c]

def Mark_Cell(map_grid, r, c, mark):
	map_grid[r][c] = mark

def Walk_Grid(map_grid, r, c, cache):
	if r > 3 or c > 3 or Check_Cell(map_grid, r, c) in ["*", "V"]:
		return False
	elif cache[r][c] != "o":
		print "use cache"
		if cache[r][c] == "V":
			return True
		else:
			return False
	elif Check_Cell(map_grid, r, c) == "E":
		return True

	Mark_Cell(map_grid, r, c, "V")

	found = Walk_Grid(map_grid, r+1, c, cache) or Walk_Grid(map_grid, r, c+1, cache)
	if found:
		cache[r][c] = "V"
	else:
		cache[r][c] = "X"
	
	return found

cache = [["o"]*4 for x in xrange(4)]
Matrix = [["o"] * 4 for x in xrange(4)]
Matrix[3][3] = "E"
Matrix[1][0] = "*"
Matrix[2][1] = "*"
Matrix[1][2] = "*"
for m in Matrix:
	print "".join(m)

print Walk_Grid(Matrix, 0, 0, cache)

for m in Matrix:
	print "".join(m)

print "\n"

for c in cache:
	print "".join(c)
