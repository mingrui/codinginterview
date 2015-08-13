"""
Stack of Plates

implement SetOfStacks push and pop, each stack in the set has capacity fixed
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

class SetOfStacks(object):
	def __init__(self, capacity):
		self.setOfStacks = Stack()
		self.capacity = capacity

	def push(self, item):
		last = self.setOfStacks.peek()
		if last != None and last.size() < capacity:
			last.push(item)
		else:
			s = Stack()
			self.setOfStacks.push(s)
			s.push(item)

	def pop(self):
		last = self.setOfStacks.peek()
		if last == None:
			return None
		else:
			v = last.pop()
			if last.size() == 0:
				self.setOfStacks.pop()
			return v

