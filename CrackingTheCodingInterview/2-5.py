"""
Sum List

you have two numbers represented by a linked list, where each node contains a single digit. The digits are stored
in reverse order, such that the 1's digit is at the head of the list, Write a function that adds the two numbers
and returns the sum as a linked list.

input: (7 -> 1 -> 6) + (5 -> 9 -> 2) that is 617 + 295
output: 2 -> 1 -> 9 that is 912

suppose the digits are stored in forwar order, repeate the problem:
input: (6 -> 1 -> 7) + (2 -> 9 -> 5) that is 617 + 295
output: 9 -> 1 -> 2 that is 912
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

# 1 details:
# 2 example:
"""

"""
# 3 1st solution
"""
read in first list to string, turn to int
read in second list to string, turn to int
add, turn int to list
"""

def Sum_List(a, b):
	# convert list a, b to int
	modifier = 1
	node = a
	a_num = 0
	while node != None:
		a_num += node.value * modifier
		modifier *= 10
		node = node.next

	modifier = 1
	node = b
	b_num = 0
	while node != None:
		b_num += node.value * modifier
		modifier *= 10
		node = node.next

	sum_num = a_num + b_num

	sum_head = None
	sum_node = None
	prev_sum_node = None
	# convert to list
	while sum_num != 0:		
		digit = sum_num % 10
		sum_node = Node(digit)
		if sum_head == None:
			sum_head = sum_node
			prev_sum_node = sum_node
		prev_sum_node.next = sum_node
		prev_sum_node = sum_node
		sum_num /= 10

	return sum_head

a = Node(1)
b = Node(5)
c = Node(2)
d = Node(4)
a.next = b
b.next = c
c.next = d

e = Node(1)
f = Node(2)
g = Node(3)
e.next = f
f.next = g

Print_List(Sum_List(a, e))