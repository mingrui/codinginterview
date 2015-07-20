"""
Palindrome

Implement a function to check if a linked list is a palindrome
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
# 2 example
# 3 1st solution
"""
O(2n)
go through list once, construct new list in reverse
compare list
"""
def Check_Palindrome(head):
	# count length
	node = head
	a_stack = []
	count = 0
	while node != None:
		count += 1
		node = node.next
	# construct stack
	node = head
	for i in xrange(count/2):
		a_stack.append(node.value)
		node = node.next
	# if count is odd ignore next node
	if count % 2 == 1:
		node = node.next
	# compare remaining list and stack
	while node != None:
		if a_stack.pop() != node.value:
			return False
		node = node.next

	return True

# 4 optimize
# 5 proof
# 6 implement
# 7 test

a = Node(1)
b = Node(2)
c = Node(2)
d = Node(1)
a.next = b
b.next = c
c.next = d
Print_List(a)
print Check_Palindrome(a)
