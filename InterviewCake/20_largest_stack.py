class Stack:

    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items: return None

        return self.items.pop()

    # see what the last item is
    def peek(self):
        # if the stack is empty, return None
        if not self.items: return None

        return self.items[len(self.items)-1]
    
class MaxStack:
    def __init__(self):
        self.stack = Stack()
        self.maxStack = Stack()
        self.utilStack = Stack()
        
    def push(self, item):
        self.stack.push(item)
        maxItem = self.maxStack.pop()
        if(maxItem == None):
        	self.maxStack.push(item)
        else:
            while maxItem > item:
                self.utilStack.push(maxItem)
                maxItem = self.maxStack.pop()
            self.maxStack.push(maxItem)
            self.maxStack.push(item)
            utilItem = self.utilStack.pop()
            while utilItem != None:
                self.maxStack.push(utilItem)
                utilItem = self.utilStack.pop()
                
    def pop(self):
        popItem = self.stack.pop()
        if popItem != None :
            maxItem = self.maxStack.pop()
            while maxItem != popItem :
                self.utilStack.push(maxItem)
                maxItem = self.maxStack.pop()
            # maxItem == popItem
            utilItem = self.utilStack.pop()
            while utilItem != None:
                self.maxStack.push(utilItem)
                utilItem = self.utilStack.pop()     
        return popItem
        
    def peek(self):
        return self.stack.peek()
    
    def get_max(self):
        return self.maxStack.peek()
        

        
        
        
class SolMaxStack:

    def __init__(self):
        self.stack      = Stack()
        self.maxs_stack = Stack()

    # Add a new item to the top of our stack. If the item is greater
    # than or equal to the the last item in maxs_stack, it's
    # the new max! So we'll add it to maxs_stack.
    def push(self, item):
        self.stack.push(item)
        if item >= self.maxs_stack.peek():
            self.maxs_stack.push(item)

    # Remove and return the top item from our stack. If it equals
    # the top item in maxs_stack, they must have been pushed in together.
    # So we'll pop it out of maxs_stack too.
    def pop(self):
        item = self.stack.pop()
        if (item == self.maxs_stack.peek()):
            self.maxs_stack.pop()
        return item

    # The last item in maxs_stack is the max item in our stack.
    def get_max(self):
        return self.maxs_stack.peek()     
    
smxStack = SolMaxStack()
smxStack.push(2)
print smxStack.get_max()
smxStack.push(1)
print smxStack.get_max()