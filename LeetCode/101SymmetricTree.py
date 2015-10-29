# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
        	return True

        return self.isSymmetricRecursive(root.left, root.right)
        
    def isSymmetricRecursive(self, left, right):
    	if left == None and right == None:
    		return True
    	elif left == None or right == None:
    		return False
    	elif left.val != right.val :
    		return False

    	return self.isSymmetricRecursive(left.left, right.right) and self.isSymmetricRecursive(left.right, right.left)