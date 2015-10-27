class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
        	return 0
        elif n == 0:
        	return 1
        else:
        	return self.climbStairs(n-1) + self.climbStairs(n-2)
    def climbStairsBetter(self, n):
    	a = b = 1
    	for x in range(2, n+1):
    		a, b = b, a + b
    	return b

# too slow

sol = Solution()
print sol.climbStairs(35)