"""
Sorted Search, No Size

you are given an array like data structure Listy which lacks a size method.
It does, however, have an elementAt(i) method thatt returns the element element
at index i in O(1) time. If i is beyond the bounds of the data structure,
it returns -1.

Given a Listy which contains sorted positive integers, find the index at which an
element x occurs. If x occurs multiple times, you may return any index
"""

# walkthrough algorithm
"""
1. Sub problem is finding the length of the array
2. Then use a modified binary search, if mid == -1, search left
"""
# implement
def SortedSearchNoSize(aList, value):
	endIndex = 1
	while aList[endIndex] != -1 and aList[endIndex] < value:
		endIndex *= 2

	# start at endIndex/2 because "aList[endIndex/2] < value" must
	# have been previously satisfied
	return ModifiedBinarySearch(aList, value, endIndex/2, endIndex)

def ModifiedBinarySearch(aList, value, lo, hi):
	while lo <= hi :
		mid = (lo + hi) / 2
		if aList[mid] > value or aList[mid] == -1:
			hi = mid-1
		elif aList[mid] < value :
			lo = mid+1
		else:
			return mid
		return -1

aList = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

print SortedSearchNoSize(aList, 7)