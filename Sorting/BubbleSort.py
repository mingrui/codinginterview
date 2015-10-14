# 
# Time Complexity: Average O(n^2) Best O(n) Worst O(n^2)
# Space Complexity: O(1)
# Stable
def BubbleSort(aList):
	N = len(aList)
	swapped = True
	while(swapped):
		swapped = False
		for i in xrange(1, N):
			if aList[i-1] > aList[i]:
				Swap(aList, i-1, i)
				swapped = True
			print i, aList

		N -= 1


def Swap(aList, one, two):
	temp = aList[one]
	aList[one] = aList[two]
	aList[two] = temp

aList = [3, 4, 1, 2, 6, 5, 7]
BubbleSort(aList)
print aList