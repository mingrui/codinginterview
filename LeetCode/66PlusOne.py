class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        N = len(digits)
        if digits[-1] + 1 < 10 :
        	digits[-1] += 1;
        	return digits
        else:
        	digits[-1] = (digits[-1] + n) % 10
        	for i in xrange(N-2, -1, -1):
        		if digits[i] + 1 < 10:
        			digits[i] += 1
        			return digits
        		else:
        			digits[i] = 0

        new = [0] * (N + 1)
        new[0] = 1
        return new