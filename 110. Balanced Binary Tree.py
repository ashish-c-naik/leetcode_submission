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
        def r(root, f):
            if root:
                left, f = r(root.left, f)
                right, f = r(root.right, f)
                left += 1
                right += 1
                if abs(left  - right) > 1:
                    f = False
                return max(left,right), f
            else: return 1, f
        height,f = r(root, True)
        return f