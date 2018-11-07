# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def r(root):
            if root:
                l = r(root.left)
                if l:
                    copyl = l
                    while l.right:
                        l = l.right
                    l.right = r(root.right)
                    l = copyl
                else: l = r(root.right)
                root.right = l
                root.left = None
            return root
        r(root)