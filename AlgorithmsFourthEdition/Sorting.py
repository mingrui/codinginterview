"""
Helpers
"""
def Exch(aList, i, j):
	k = aList[i]
	aList[i] = aList[j]
	aList[j] = k

def Less(a, b):
	return a < b


"""
Elementary Sorts
"""
def SelectionSort(aList):
	N = len(aList)
	for i in xrange(N):
		min = i
		for j in xrange(i+1, N):
			if Less(aList[j], aList[min]):
				min = j
		Exch(aList, i, min)

def InsertionSort(aList):
	N = len(aList)
	for i in xrange(N):
		j = i
		while j > 0 and Less(aList[j], aList[j-1]):
			Exch(aList, j, j-1)
			j -= 1

def ShellSort(aList):
	N = len(aList)
	h = 1
	while h < N/3 :
		h = 3*h + 1
	while h >= 1:
		i = h
		while i < N:
			j = i
			while j >= h and Less(aList[j], aList[j-h]):
				Exch(aList, j, j-1)
				j = j-h
			i += 1
		h = h/3


"""
Merge Sort
"""
def MergeSort(aList):
	aux = aList[:]
	MergeSortWork(aList, 0, len(aList)-1, aux)

def MergeSortWork(aList, lo, hi, aux):
	if hi <= lo:
		return
	mid = lo + (hi-lo)/2
	MergeSortWork(aList, lo, mid, aux)
	MergeSortWork(aList, mid+1, hi, aux)
	Merge(aList, lo, mid, hi, aux)

def MergeSortBU(aList):
	aux = aList[:]
	N = len(aList)
	sz = 1
	while sz < N:
		lo = 0
		while lo < N-sz:
			Merge(aList, lo, lo+sz-1, min(lo+sz+sz-1, N-1), aux)
			lo += sz + sz
		sz = sz + sz

def Merge(aList, lo, mid, hi, aux):
	k = lo
	while k <= hi:
		aux[k] = aList[k]
		k += 1

	i = lo
	j = mid+1
	k = lo
	while k <= hi:
		if i > mid:
			aList[k] = aux[j]
			j += 1
		elif j > hi:
			aList[k] = aux[i]
			i += 1
		elif Less(aux[j], aux[i]):
			aList[k] = aux[j]
			j += 1
		else:
			aList[k] = aux[i]
			i += 1
		k += 1



# test
listOne = [2, 4, 5, 8, -1 ,5, 3, 0]
listTwo = ['E', 'E', 'G', 'M', 'R', 'A', 'C', 'E', 'R', 'T']
MergeSortBU(listOne)
print listOne

