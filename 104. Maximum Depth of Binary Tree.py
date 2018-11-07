# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxd(root,depth):
            if root:
                    depth = max(maxd(root.right,depth+1),maxd(root.left,depth+1))
            return depth
        return maxd(root,0)