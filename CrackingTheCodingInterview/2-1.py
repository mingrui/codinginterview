"""
Remove Dups

write code to remove duplicates from an unsorted linked list
how would you solve this problem if a temporary buffer is not allowed
"""

# singly linked list
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    


# 1 read details
# 2 example
# 3 first solution
"""
A. use a dictionary to keep track, O(n) time, O(n) space

B. with out extra buffer, use 2 pointers the first one after the second one, the second one searches the list
	O(n^2) time, O(1) space
"""
# 4 optimize
# 5 proof
# 6 implement

"""A"""

def Remove_Dup(head):
	# 0 or 1 node
	if head == None or head.next == None:
		return head

	node_dict = {}
	node_dict[head.value] = 1
	prev_node = head
	node = head.next

	while node != None:
		if node.value in node_dict:
			prev_node.next = node.next
		else:
			node_dict[node.value] = 1

		prev_node = node
		node = node.next

def Remove_Dup_Slow(head):
	if head == None or head.next == None:
		return head

	tracker = head
	searcher_prev = tracker
	searcher = tracker.next

	while tracker != None:
		searcher_prev = tracker
		searcher = tracker.next
		while searcher != None:
			if tracker.value == searcher.value:
				searcher_prev.next = searcher.next

			searcher_prev = searcher
			searcher = searcher.next

		tracker = tracker.next

# 7 test
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(1)
a.next = b
b.next = c
c.next = d

def Print_List(node):
	while node != None:
		print node.value
		node = node.next

Remove_Dup_Slow(a)
Print_List(a)
