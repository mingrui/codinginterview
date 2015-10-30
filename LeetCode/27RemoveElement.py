class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        backNumber = len(nums)-1
        while backNumber > 0:
        	if nums[backNumber] != val:
        		break
        	backNumber -= 1
        x = 0
        while x < backNumber :
        	if nums[x] == val :
        		nums[x], nums[backNumber] = nums[backNumber], nums[x]
        		backNumber -= 1
        	x += 1
        if nums[backNumber] == val:
        	backNumber -= 1
        print nums
        return backNumber+1

sol = Solution()
nums = [4, 4]
val = 4
print sol.removeElement(nums, val)