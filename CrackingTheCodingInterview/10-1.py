"""
Sorted Merge

You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order
"""

# 1 notice details
# 2 example
# 3 brute force
# 4 optimize
# 5 walk through algorithm
"""
3 indexes, aIndex, bIndex, mergeIndex
start backwards, cmp A and B elements and put to end of A list
"""
# 6 implement
def SortedMerge(aList, bList, lastA, lastB):
	aIndex = lastA - 1
	bIndex = lastB - 1
	mergeIndex = lastA + lastB - 1

	while bIndex >= 0 :
		if aIndex >= 0 and aList[aIndex] > bList[bIndex] :
			aList[mergeIndex] = aList[aIndex]
			aIndex -= 1
		else:
			aList[mergeIndex] = bList[bIndex]
			bIndex -= 1
		mergeIndex -= 1

# 7 test
aList = [1, 3, 5, 7, 9, 0, 0, 0]
bList = [2, 4, 6]
lastA = 5
lastB = 3
SortedMerge(aList, bList, lastA, lastB)
print aList