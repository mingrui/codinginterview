"""
Delete Middle Node

implement an algorithm to delete a node in the middle of a singly linked list
given only access to that node
"""

# 1 details
"""
node is in the middle
"""
# 2 example
"""
given c from a->b->c->d->e
result a->b->d->e
"""
# 3 1st solution
"""
overwrite this node with next node
"""
# 4 optimize
# 5 proof
# 6 implement
def Delete_Middle_Node(delete_node):
	prev_node = delete_node
	node = delete_node
	while node != None:
		if node.next != None:
			node.value = node.next.value
		else:
			prev_node.next = None

		prev_node = node
		node = node.next
# 7 test