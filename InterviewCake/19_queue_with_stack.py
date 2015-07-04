class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)
    
class Queue:
    def __init__(self):
        self.sOne = Stack()
        self.sTwo = Stack()
	
    def size(self):
        return self.sOne.size()
    
    def isEmpty(self):
        return self.sOne.empty()
    
    def enqueue(self, item):
        while self.sOne.size() > 0:
            self.sTwo.push(self.sOne.pop())
        self.sOne.push(item)
        while self.sTwo.size() > 0:
            self.sOne.push(self.sTwo.pop())
        
    def dequeue(self):
        if self.sOne.isEmpty() == False :
        	return self.sOne.pop()
        else:
            raise Exception('trying to dequeue empty queue')
            
class BetterQueue:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()
        
    def size(self):
        return self.inStack.size() + self.outStack.size()
    
    def isEmpty(self):
        return self.inStack.isEmpty() and self.outStack.isEmpty()
    
    def enqueue(self, item):
        self.inStack.push(item)
        
    def dequeue(self):
        if self.outStack.isEmpty() == False:
            return self.outStack.pop()
        else:
            while self.inStack.isEmpty() == False:
                self.outStack.push(self.inStack.pop())
            if self.outStack.isEmpty():
                return None
            else:
            	return self.outStack.pop()
    


bqOne = BetterQueue()
bqOne.enqueue(1)
bqOne.enqueue(2)
bqOne.enqueue(3)
print bqOne.dequeue()
print bqOne.dequeue()
bqOne.enqueue(4)
bqOne.enqueue(5)
print bqOne.dequeue()
print bqOne.dequeue()
print bqOne.dequeue()
print bqOne.dequeue()
    
