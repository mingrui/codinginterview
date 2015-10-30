class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = [nums[x] for x in range(len(nums)) if nums[x] != nums[x-1] or x == 0]
        return len(nums)

    def simpleSolution(self, nums):
    	if len(nums) == 0:
    		return 0

    	lastItem = nums[0]
    	m, n = 1, 1
    	for n in range(len(nums)):
    		x = nums[n]
    		if x != lastItem:
    			lastItem = x
    			nums[m] = x
    			m += 1
    	del nums[m:]
    	return len(nums)