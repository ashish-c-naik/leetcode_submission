# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find(self,root):
        if not root: return 0
        left , right = self.find(root.left), self.find(root.right)
        l = left + 1 if root.left and root.left.val == root.val else 0
        r = right + 1 if root.right and root.right.val == root.val else 0
        self.final = max(self.final, l+r)
        return max(l,r)
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.final = 0
        self.find(root)
        return self.final