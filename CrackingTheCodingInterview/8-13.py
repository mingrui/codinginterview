"""
Stack of Boxes

a stack of n boxes, width w1, heights h1, and depths d1.
boxes can't be rotated and can only be stacked on top of on another if each box in the stack
is strictly larger than the box above it in width, height, and depth.
Implement a method to compute the height of the tallest possible stack.
The height of the stack is the sum of the heights of each box
"""

# 1 notice details
# 2 work on example
# 3 brute force solution
# 4 optimize using overlooked details
"""
memoize
"""
# 5 walk through optimized algorithm
# 6 Implement
class myBox:
	def __init__(self, w, h, d):
		self.w = w
		self.h = h
		self.d = d

def Smaller_Box(box_one, box_two):
	if box_one.w < box_two.w and box_one.h < box_two.h and box_one.d < box_two.d :
		return box_one
	elif box_one.w > box_two.w and box_one.h > box_two.h and box_one.d > box_two.d:
		return box_two
	else:
		return None

def Create_Stack(boxes):
	boxes.sort(key = lambda x : x.w, reverse = True)
	maxHeight = 0
	stack_map = [0] * len(boxes)
	for i in xrange(len(boxes)):
		height = Create_Stack_Work(boxes, i, stack_map)
		maxHeight = max(maxHeight, height)
	return maxHeight

def Create_Stack_Work(boxes, bottom_index, stack_map):
	if stack_map[bottom_index] > 0:
		print "using stack map for bottom_index: %d which is height %d" %(bottom_index, stack_map[bottom_index])
		return stack_map[bottom_index]

	bottom_box = boxes[bottom_index]
	maxHeight = 0
	for i in xrange(bottom_index+1, len(boxes)):
		if (Smaller_Box(boxes[i], bottom_box) == boxes[i]):
			height = Create_Stack_Work(boxes, i, stack_map)
			maxHeight = max(maxHeight, height)
	maxHeight += bottom_box.h
	stack_map[bottom_index] = maxHeight
	return maxHeight

"""
2nd SOLUTION
"""

# 7 test
boxes = []
boxes.append(myBox(1, 1, 1))
boxes.append(myBox(2, 2, 2))
boxes.append(myBox(4, 4, 4))
boxes.append(myBox(3 ,5, 3))
print Create_Stack(boxes)