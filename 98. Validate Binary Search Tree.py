# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(root,mini,maxi):
            if root:
                if mini < root.val < maxi:
                    return valid(root.right,root.val,maxi) and valid(root.left,mini,root.val)
                else:
                    return False
            return True
        return valid(root,float('-inf'),float('inf'))