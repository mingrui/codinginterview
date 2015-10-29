# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.depthAndBalan(root)[1]

    def depthAndBalan(self, root):
    	if root is None:
    		return 1, True
    	leftDep, leftBal = self.depthAndBalan(root.left)
    	rightDep, rightBal = self.depthAndBalan(root.right)
    	curBal = abs(leftDep - rightDep) <= 1
    	return max(leftDep, rightDep) + 1, curBal and leftBal and rightBal
