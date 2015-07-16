"""
Return Kth to Last

Implement an algorithm to find the kth to last element of a singly linked list
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
Singly linked list

K to last element
"""
# 2 example
"""
don't know how long the list is, have to count O(n)

special case: len(list) < k
"""
# 3 1st solution
"""
A. run through the loop twice, the first time, count list len
	the second time, find len(list) - K element (start counting from 1)

B. have a K length "ruler", two ends of the ruler move at the same speed, when the
	right end ruler hits the end, the left end of the ruler is the result
"""
# 4 optimize
# 5 proof
# 6 Implement
def Ruler_K(head, k):
	if head == None or head.next == None:
		if k != 0:
			return
		else:
			return head

	right_node = head
	left_node = head

	counter = 0
	while right_node != None:
		if counter == k:
			if right_node.next != None:
				left_node = left_node.next
		else:
			counter += 1

		right_node = right_node.next

	# len(list) < k
	if counter <= k:
		print "error: len(list) <= k"
		return

	print left_node.value

# 7 test

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d

Print_List(a)
Ruler_K(a, 4)