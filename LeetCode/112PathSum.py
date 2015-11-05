# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None :
        	return False
        elif root.val == sum and not root.left and not root.right:
        	return True
        else:
        	remainingSum = sum - root.val
        	return self.hasPathSum(root.left, remainingSum) or self.hasPathSum(root.right, remainingSum)

sol = Solution()
a = TreeNode(5)
a.left = TreeNode(4)
a.right = TreeNode(8)
a.left.left = TreeNode(11)
a.left.left = TreeNode(7)
a.left.right = TreeNode(2)
a.right.left = TreeNode(13)
a.right.right = TreeNode(4)
a.right.right.right = TreeNode(1)
print sol.hasPathSum(a, 22)