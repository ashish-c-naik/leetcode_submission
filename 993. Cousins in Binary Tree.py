# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        def r(root, depth, parent):
            if not root: return 0
            left = r(root.left, depth + 1, root)
            right = r(root.right, depth + 1, root)
            self.hm[root.val] = (depth, parent)
        self.hm = {}
        r(root, 0, None)
        return self.hm[x][0] == self.hm[y][0] and self.hm[x][1] != self.hm[y][1] if x in self.hm and y in self.hm else False
            