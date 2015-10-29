# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
        	return l2
        elif not l2:
        	return l1

        node1 = l1
        node2 = l2
        if node1.val > node2.val:
        	node1, node2 = node2, node1
        last = node1
        while node1 and node2:
        	while node1 and node2 and node1.val <= node2.val:
        		last = node1
        		node1 = node1.next
        	last.next = node2
        	node1, node2 = node2, node1
        if l1.val <= l2.val:
        	return l1
        else:
        	return l2


a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
b = ListNode(1)
b.next = ListNode(4)

sol = Solution()

node = sol.mergeTwoLists(a, b)
while node:
	print node.val
	node = node.next












