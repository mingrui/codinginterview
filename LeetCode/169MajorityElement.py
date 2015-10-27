class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0
        for e in nums:
        	if count == 0:
        		candidate = e
        		count = 1
        	elif e == candidate:
        		count += 1
        	else:
        		count -=1
        return candidate