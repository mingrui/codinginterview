# use caching to run faster

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
        	return 0
        elif len(nums) == 1:
        	return nums[0]
        else:
        	numSet = {}
        	return max(self.robRecursive(nums, 0, numSet), self.robRecursive(nums, 1, numSet))
    
    def robRecursive(self, nums, i, numSet):
    	result = 0
    	if numSet.has_key(i):
    		return numSet[i]

    	if i + 2 > len(nums) - 1 :
    		result = nums[i]
    	elif i + 3 > len(nums) - 1 :
    		result = nums[i] + nums[i+2]
    	else:
    		result = nums[i] + max(self.robRecursive(nums, i+2, numSet), self.robRecursive(nums, i+3, numSet))

    	numSet[i] = result
    	return result


sol = Solution()
aList = [6,6,4,8,4,3,3,10]
print sol.rob(aList)