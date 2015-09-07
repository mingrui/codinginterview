"""
Sparse Search

Given a sorted array of strings that is interspersed with empty strings, write
a method to find the location of a given string.
"""

aList = [-1, -1, 1, -1, -1, -1, 1, -1, -1, -1, 2, -1, -1, 3]

# walkthrough algorithm
"""
1. sub problem when looking at mid, if mid == "", then search left and right
for the nearest non "", use that as the new mid
2. modified binary search
"""
# implement
def SparseSearch(aList, value):
	lo = 0
	hi = len(aList) - 1

	while lo <= hi:
		mid = (lo + hi) / 2
		if aList[mid] == -1 :
			left = mid-1
			right = mid+1
			while True:
				print left
				print right
				# this part is important
				# book is wrong
				if left < 0 or right > len(aList) - 1:
					return -1
				elif right <= len(aList) - 1 and aList[right] != -1:
					mid = right
					break
				elif left >= 0 and aList[left] != -1:
					mid = left
					break
				left -= 1
				right += 1

		if aList[mid] < value:
			lo = mid+1
		elif aList[mid] > value:
			hi = mid-1
		else:
			return mid

	return -1

print SparseSearch(aList, 0)