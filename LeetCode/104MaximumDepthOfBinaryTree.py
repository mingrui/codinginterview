# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
	def __init__(self):
		self.max_depth_count = 0

	def maxDepth(self, root):
		self.inOrderTraversal(root, 0)
		return self.max_depth_count

	def inOrderTraversal(self, node, depth_count):
		if(node != None):
			depth_count += 1
    		if depth_count > self.max_depth_count:
    			self.max_depth_count = depth_count
    		if(node.left != None):
    			self.inOrderTraversal(node.left, depth_count)
    		if(node.right != None):
    			self.inOrderTraversal(node.right, depth_count)


root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(5)

sol = Solution()
print sol.maxDepth(root)

# good solution

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1