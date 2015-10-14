# https://en.wikipedia.org/wiki/Selection_sort
# Time Complexity: Average O(n^2) Best O(n^2) Worst O(n^2)
# Space Complexity: O(1)
# Unstable
def SelectionSort(aList):
	N = len(aList)
	for i in xrange(N):
		print i, aList
		minIndex = i
		for j in xrange(i+1, N):
			if aList[j] < aList[minIndex]:
				minIndex = j
		Swap(aList, i, minIndex)


def Swap(aList, one, two):
	temp = aList[one]
	aList[one] = aList[two]
	aList[two] = temp

aList = [3, 4, 1, 2, 6, 5, 7]
SelectionSort(aList)
print aList