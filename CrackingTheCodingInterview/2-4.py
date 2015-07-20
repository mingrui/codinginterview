"""
Partition

Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes
greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements
less than x
"""

# singly linked list
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def Print_List(node):
	while node != None:
		print node.value
		node = node.next


# 1 details
"""
order does not matter
"""
# 2 example
"""
input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""
# 3 first solution
"""
small_node
large_node
go through list:
	if node < partition_value
		attach to small_node
	else
		attach to large_node

small_node -> large_node
"""
def Partition(head, partition_value):
	small_node_head = None
	small_node_tail = None
	large_node_head = None
	small_node_tail = None
	node = head
	while node != None:
		if node.value < partition_value:
			if small_node_head == None:
				small_node_head = node
				small_node_tail = node
			else:
				small_node_tail.next = node
				small_node_tail = node
		else:
			if large_node_head == None:
				large_node_head = node
				large_node_tail = node
			else:
				large_node_tail.next = node
				large_node_tail = node
		node = node.next

	# check for special situations
	if small_node_head == None:
		return large_node_head

	small_node_tail.next = large_node_head
	return small_node_head

# 4 optimize
# 5 proof
# 6 implement
# 7 test

a = Node(1)
b = Node(5)
c = Node(2)
d = Node(4)
a.next = b
b.next = c
c.next = d
Print_List(Partition(a, 2))