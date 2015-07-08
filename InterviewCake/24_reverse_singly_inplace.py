class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
        
def reverse_linked_list(node):
    if node == None:
        return node
    
    prev_node = node
    next_node = node.next
    while next_node != None:
        next_next_node = next_node.next
    	next_node.next = prev_node
        prev_node = next_node
        next_node = next_next_node
        
    node.next = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

reverse_linked_list(a)

node = d
while node != None:
    print node.data
    node = node.next
    