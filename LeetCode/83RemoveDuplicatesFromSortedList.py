# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = head
        prev = ListNode(None)
        while head :
        	if prev.val == head.val:
        		prev.next = head.next
        	else:
        		prev = head
        	head = head.next
        return dummy
