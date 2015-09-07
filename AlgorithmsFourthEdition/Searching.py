"""
Binary Search Trees

Simple BST, un-balanced
"""

class Node(object):
	def __init__(self, key, value, N):
		self.key = key # key
		self.value = value # associated value
		self.N = N # number of nodes in subtree rooted here
		self.left = None # link to left tree
		self.right = None # link to right tree

class BST(object):
	def __init__(self):
		self.root = None

	def Size(self):
		return self.NodeSize(self.root)

	def NodeSize(self, node):
		if node == None : 
			return 0
		else: 
			return node.N

	def Get(self, key):
		return self.NodeGet(self.root, key)

	def NodeGet(self, node, key):
		if node == None :
			return None
		cmp = key - node.key
		if cmp < 0 :
			return self.NodeGet(node.left, key)
		elif cmp > 0 :
			return self.NodeGet(node.right, key)
		else:
			return node.value

	def Put(self, key, value):
		self.root = self.NodePut(self.root, key, value)

	def NodePut(self, node, key, value):
		if node == None:
			return Node(key, value, 1)
		cmp = key - node.key
		if cmp < 0:
			node.left = self.NodePut(node.left, key, value)
		elif cmp > 0:
			node.right = self.NodePut(node.right, key, value)
		else:
			node.value = value
		node.N = self.NodeSize(node.left) + self.NodeSize(node.right) + 1
		return node

	def Min(self):
		return self.NodeMin(self.root).key

	def NodeMin(self, node):
		if node.left == None :
			return node
		return self.NodeMin(node.left)

	def Max(self):
		return self.NodeMax(self.root).key

	def NodeMax(self, node):
		if node.right == None :
			return node
		return self.NodeMax(node.right)

	# largest key less than or equal to key
	def Floor(self, key):
		x = self.NodeFloor(self.root, key)
		if x == None :
			return None
		return x.key

	def NodeFloor(self, node, key):
		if node == None :
			return None
		cmp = key - node.key
		if cmp == 0 :
			return node
		if cmp < 0 :
			return self.NodeFloor(node.left, key)
		t = self.NodeFloor(node.right, key)
		if t != None :
			return t
		else:
			return node

	# key of rank k
	def Select(self, k):
		return self.NodeSelect(self.root, k).key

	# return node containing key of rank k
	def NodeSelect(self, node, k):
		if node == None :
			return None
		t = self.NodeSize(node.left)
		if t > k :
			return self.NodeSelect(node.left, k)
		elif t < k :
			return self.NodeSelect(node.right, k-t-1)
		else:
			return node

	# number of keys less than key
	def Rank(self, key):
		return self.NodeRank(self.root, key)

	# return number of keys less than key in the subtree rooted at x
	def NodeRank(self, node, key):
		if node == None :
			return 0
		cmp = key - node.key
		if cmp < 0 :
			return self.NodeRank(node.left, key)
		elif cmp > 0 :
			return 1 + self.NodeSize(node.left) + self.NodeRank(node.right, key)
		else:
			return self.NodeSize(node.left)

	def DeleteMin(self):
		self.root = self.NodeDeleteMin(self.root)

	def NodeDeleteMin(self, node):
		if node.left == None :
			return node.right
		node.left = self.NodeDeleteMin(node.left)
		node.N = self.NodeSize(node.left) + self.NodeSize(node.right) + 1
		return node

	def Delete(self, key):
		self.root = self.NodeDelete(self.root, key)

	def NodeDelete(self, node, key):
		if node == None:
			return None
		cmp = key - node.key
		if cmp < 0 :
			node.left = self.NodeDelete(node.left, key)
		elif cmp > 0 :
			node.right = self.NodeDelete(node.right, key)
		else:
			if node.right == None :
				return node.left
			if node.left == None:
				return node.right
			t = node
			node = self.NodeMin(t.right)
			node.right = self.NodeDeleteMin(t.right)
			node.left = t.left
		node.N = self.NodeSize(node.left) + self.NodeSize(node.right) + 1
		return node

	def AllKeys(self):
		return self.RangeKeys(self.Min(), self.Max())

	def RangeKeys(self, lo, hi):
		keysList = []
		self.ListRangeKeys(self.root, keysList, lo, hi)
		return keysList

	def ListRangeKeys(self, node, keysList, lo, hi):
		if node == None :
			return
		cmplo = lo - node.key
		cmphi = hi - node.key
		if cmplo < 0 :
			self.ListRangeKeys(node.left, keysList, lo, hi)
		if cmplo <= 0 and cmphi >= 0 :
			keysList.append(node.key)
		if cmphi > 0 : 
			self.ListRangeKeys(node.right, keysList, lo, hi)


def PrintBST(node):
	if node == None:
		return
	PrintBST(node.left)
	print node.key
	PrintBST(node.right)

bst = BST()
bst.Put(1, "a")
bst.Put(2, "b")
bst.Put(0, "c")
bst.Put(-1, "d")
bst.Put(-2, "e")
bst.Put(2, "bb")
print bst.RangeKeys(-6, 1)





































