class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex += 1
        row = []
        for line in xrange(1, rowIndex+1) :
        	C = 1
        	for i in xrange(1, line+1) :
        		if line == rowIndex:
        			row.append(C)
        		C = C * (line - i) / i
        return row

sol = Solution()
print sol.getRow(0)