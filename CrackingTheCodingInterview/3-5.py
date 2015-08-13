"""
Sort Stack

Write a program to sort a stack such that the smallest items are on the top.
You can use an additional temporary stack, but you may not copy the elements into any
other data structure(such as an array) the stack supports the following operations:
push, pop, peek, isEmpty
"""

class Node(object):
	def __init__(self, item):
		self.item = item
		self.next = None

class Stack(object):
	def __init__(self):
		self._first = None # top of stack, most recently added node
		self._size = 0 # number of items

	@property
	def size(self):
		return self._size

	def isEmpty(self):
		return first == None

	def push(self, item):
		n = Node(item)
		n.next = self._first
		self._first = n
		self._size += 1

	def pop(self):
		if self.isEmpty() :
			raise IndexError("pop from empty stack")
		n = self._first
		self._first = self._first.next
		self._size -= 1
		return n.item

	def peek(self):
		# can be None
		return self._first.item

	def __iter__(self):
		current = self._first
		while current:
			yield current.item
			current = current.next

	def __str__(self):
		return " ".join(reversed([str(item) for item in self]))

	def __repr__(self):
		return "Stack(" + str(self) + ")"

def SortStack(ogStack):
	tempStack = Stack()
	while ogStack.size() > 0 :
		v = ogStack.pop()
		while tempStack.isEmpty() == False and tempStack.peek() < v:
			ogStack.push(tempStack.pop())
		tempStack.push(v)
	return tempStack










