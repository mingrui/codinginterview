"""
Peak and Valleys

In an array of integers, a "peak" is an element which is greater than or equal to the
adjacent integers and a "valley" is an element which is less than or equal to the adjacent
integers. For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are
valleys. Given an array of integers, sort the array into an alternating sequence of peaks
and valleys.
"""

# Simple solution
# sort array first, than swap and rearrange elements

def Swap(aList, aIndex, bIndex):
	temp = aList[aIndex]
	aList[aIndex] = aList[bIndex]
	aList[bIndex] = temp

# peak is greater than or equal to adjacent integers
# valley is less than or equal to adjacent integers
def PeakAndValleys(aList):
	aList.sort()

	for i in xrange(len(aList)) :
		if i % 2 == 0 :
			continue
		print i
		Swap(aList, i-1, i)

def MaxIndex(aList, left, center, right):
	 # take into account that left, center and/or right might be out of bound

# look at 3 adjacent elements at a time
# if doesn't satisfy peak, swap middle and largest adjacent element
def PeakAndValleysNoSort(aList):
	i = 1
	while i < len(aList) :
		biggestIndex = MaxIndex(aList, i-1, i, i+1)
		if i != biggestIndex :
			Swap(aList, i, biggestIndex)
		i += 2

aList = [3, 2, 1, 4, 5, 8, 9, 6, 7, 5, 5, 5, 10]
PeakAndValleys(aList)
print aList

