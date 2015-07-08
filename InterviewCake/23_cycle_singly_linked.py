class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
# if there is cycle, two step node will catch up to one step node
def contains_cycle(node):
    one_step_node = node
    two_step_node = node
    while one_step_node != None and two_step_node != None:
        one_step_node = one_step_node.next
        two_step_node = two_step_node.next.next
        if one_step_node == two_step_node:
            return True
    
    return False
        
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d

print contains_cycle(a)