# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import sys
        val = sys.maxint
        def minD(root,arr,val):
            if root:
                if root.right:
                    val = min(val,minD(root.right,arr,val))
                if arr:
                    val = min(val,abs(root.val-arr[-1]))
                arr.append(root.val)
                if root.left:
                    val = min(val,minD(root.left,arr,val))
            return val
        val = minD(root,[],val)
        return val
                