# 
# Time Complexity: Average O(nlogn) Best O(nlogn) Worst O(n^2)
# Space Complexity: O(logn)
# Unstable
def QuickSort(aList, left, right):
	index = Partition(aList, left, right)
	if(left < index - 1):
		QuickSort(aList, left, index - 1)
	if(right > index):
		QuickSort(aList, index, right)

def Partition(aList, left, right):
	print left, right
	pivot = aList[(left+right)/2]
	while(left <= right):
		while(aList[left] < pivot):
			left += 1
		while(aList[right] > pivot):
			right -= 1
		if(left <= right):
			print "swap", aList[left], aList[right]
			Swap(aList, left, right)
			left += 1
			right -= 1
	print pivot,  aList, left
	return left

def Swap(aList, one, two):
	temp = aList[one]
	aList[one] = aList[two]
	aList[two] = temp


aList = [2, 4, 1, 3, 6, 5, 7]
QuickSort(aList, 0, len(aList)-1)
print aList

