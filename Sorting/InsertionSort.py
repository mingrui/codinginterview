# https://en.wikipedia.org/wiki/Insertion_sort
# Time Complexity: Average O(n^2) Best O(n) Worst O(n^2) 
# Space Complexity: O(1)
# Stable
def InsertionSort(aList):
	N = len(aList)
	for i in xrange(N):
		print i, aList
		j = i
		while j > 0 and aList[j] < aList[j-1]:
			Swap(aList, j-1, j)
			j -= 1


def Swap(aList, one, two):
	temp = aList[one]
	aList[one] = aList[two]
	aList[two] = temp

aList = [3, 4, 1, 2, 6, 5, 7]
InsertionSort(aList)
print aList