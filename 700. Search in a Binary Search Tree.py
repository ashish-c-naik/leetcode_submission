# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def chngeRoot(root):
            if not root:
                return None
            else:
                if root.val > val:
                    root = chngeRoot(root.left)
                elif root.val < val:
                    root = chngeRoot(root.right)
                return root
        return chngeRoot(root)
            
        