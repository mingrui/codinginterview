def BinarySearchRecursive(aList, x, low, high):
	if (low > high):
		return -1

	mid = (low + high) / 2
	if(aList[mid] < x):
		return BinarySearchRecursive(aList, x, mid+1, high)
	elif(aList[mid] > x):
		return BinarySearchRecursive(aList, x, low, mid-1)
	else:
		return mid

aList = [1, 2, 3, 4, 5]
print BinarySearchRecursive(aList, 5, 0, len(aList)-1)