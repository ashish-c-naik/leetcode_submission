# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def height(root):
            if not root: return 0
            return 1 + max(height(root.left), height(root.right))
        def r(root):
            if not root: return 0
            left = r(root.left)
            right = r(root.right)
            return max(max(right , left), height(root.right) + height(root.left))
        return r(root)