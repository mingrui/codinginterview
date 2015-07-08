# singly linked list
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
   
def delete_node(node):
    prev_node = Node(0)
    while(node.next != None):
        prev_node = node
        node.value = node.next.value
        node = node.next
    prev_node.next = None
    
def better_delete_node(node):
    if node.next != None:
        node.value = node.next.value
        node.next = node.next.next
    else:
        node = None
        

a = Node(5)
b = Node(1)
c = Node(9)
d = Node(10)
a.next = b
b.next = c
c.next = d

better_delete_node(d)
print a.next.next.value
