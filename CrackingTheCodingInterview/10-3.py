"""
Search in Rotated Array

Given a sorted array of n integers that has been rotated an unknown
number of times, write code to find an element in the array.
You may assume that the array was originally sorted in increasing
order.
"""

# 1 notice details
"""
one of either left or right half must be sorted, the other one
must contain rotation point

similar to binary search, tweak the algorithm to handle these two
different situations
"""
# 2 example
# 3 brute force
# 4 optimize
# 5 walkthrough algorithm
# 6 implement
def SearchRotatedList(aList, x, lo, hi):
	mid = (lo + hi) / 2
	if aList[mid] == x :
		return mid

	if lo > hi :
		return -1

	if aList[lo] < aList[mid]: # left is normally ordered
		if x >= aList[lo] and x < aList[mid] :
			return SearchRotatedList(aList, x, lo, mid-1)
		else:
			return SearchRotatedList(aList, x, mid+1, hi)
	elif aList[mid] < aList[hi]: # right is normally ordered
		if x > aList[mid] and x <= aList[hi]:
			return SearchRotatedList(aList, x, mid+1, hi)
		else:
			return SearchRotatedList(aList, x, lo, mid-1)
	elif aList[lo] == aList[mid]: # left half is all repeats
		if aList[mid] != aList[hi]: # if right is different, search it
			return SearchRotatedList(aList, x, mid+1, hi)
		else:
			result = SearchRotatedList(aList, x, lo, mid-1)
			if result == -1 :
				return SearchRotatedList(aList, x, mid+1, hi)
			else:
				return result
	return -1

aList = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
print SearchRotatedList(aList, 5, 0, len(aList)-1)
