# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def invert(root):
            if root:
                root.right = invert(root.right)
                root.left = invert(root.left)
                root.right, root.left = root.left,root.right
            return root
        return invert(root)