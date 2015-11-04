class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for line in xrange(numRows) :
        	triangle.append([0] * (line+1))
        	for i in xrange(line + 1) :
        		if i == 0 or line == i :
        			triangle[line][i] = 1
        		else:
        			triangle[line][i] = triangle[line-1][i-1] + triangle[line-1][i]
        return triangle