def BinarySearch(aList, x):
	low = 0
	high = len(aList) - 1

	while(low <= high):
		mid = (low + high) / 2
		if(aList[mid] < x):
			low = mid + 1
		elif(aList[mid] > x):
			high = mid - 1
		else:
			return mid

	return -1

aList = [1, 2, 3, 4, 5]
print BinarySearch(aList, 5)