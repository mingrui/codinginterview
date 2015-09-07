from random import shuffle

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
def BubbleSort(aList):
	N = len(aList)
	swapped = True
	while(swapped):
		swapped = False
		for i in xrange(1, N): #inclusive n-1
			if aList[i-1] > aList[i] :
				Exch(aList, i-1, i)
				swapped = True
		N -= 1


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
				Exch(aList, j, j-h)
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

"""
Quick Sort
"""

def QuickSort(aList):
	shuffle(aList) # eliminate dependence on input
	QuickSortWork(aList, 0, len(aList)-1)

def QuickSortWork(aList, lo, hi):
	if hi <= lo:
		return
	j = Partition(aList, lo, hi)
	QuickSortWork(aList, lo, j-1)
	QuickSortWork(aList, j+1, hi)

def Partition(aList, lo, hi):
	i = lo+1
	j = hi
	v = aList[lo]
	while True :
		while Less(aList[i], v):
			if i == hi:
				break
			i += 1
		while Less(v, aList[j]):
			if j == lo:
				break
			j -= 1
		if i >= j :
			break
		Exch(aList, i, j)
	Exch(aList, lo, j)
	return j

def QuickSortThreeWay(aList):
	shuffle(aList)
	QuickSortWorkThreeWay(aList, 0, len(aList)-1)

def QuickSortWorkThreeWay(aList, lo, hi):
	if hi <= lo :
		return
	lt = lo
	i = lo+1
	gt = hi
	v = aList[lo]
	while i <= gt :
		cmp = aList[i] - v
		if cmp < 0 :
			Exch(aList, lt, i)
			lt += 1
			i += 1
		elif cmp > 0 :
			Exch(aList, i, gt)
			gt -= 1
		else:
			i += 1
	QuickSortWorkThreeWay(aList, lo, lt-1)
	QuickSortWorkThreeWay(aList, gt+1, hi)


"""
Heap
"""
class MaxPQ(object):
	def __init__(self):
		self.pq = []
		self.N = 0

	def IsEmpty(self):
		return N == 0

	def Size(self):
		return self.N

	def Insert(self, key):
		self.N += 1
		self.pq[self.N] = key
		self.Swim(self.N)

	def DelMax():
		_max = self.pq[1]
		Exch(self.pq, 1 , self.N)
		self.N -= 1
		self.pq[self.N+1] = None
		self.Sink(1)
		return _max

	def Swim(self, k):
		while k > 1 and Less(k/2, k):
			Exch(self.pq, k/2, k)
			k = k/2

	def Sink(self, k):
		while 2*k <= self.N :
			j = 2 * k
			if j < self.N and Less(j, j + 1) :
				j += 1
			if not Less(k, j) :
				break
			Exch(self.pq, k, j)
			k = j

# test
listOne = [2, 4, 5, 8, -1 ,5, 3, 0, -1, 2]
QuickSortThreeWay(listOne)
print listOne

