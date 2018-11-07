# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        def r(root):
            if not root: return None
            if L <= root.val <= R:
                root.right = r(root.right)
                root.left = r(root.left)
            else:
                if root.val > L:
                    root = r(root.left)
                else:
                    root = r(root.right)
            return root
        return r(root)
