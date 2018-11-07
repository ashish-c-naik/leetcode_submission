# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def rec(t1,t2,node):
            if not t1 and not t2:
                return node
            val = 0
            if t1:
                val += t1.val
            if t2:
                val += t2.val
            node = TreeNode(val)
            if t1 and t2:
                node.right = rec(t1.right,t2.right,node.right)
                node.left = rec(t1.left,t2.left,node.left)
            elif t1:
                node.right = rec(t1.right,None,node.right)
                node.left = rec(t1.left,None,node.left)
            elif t2:
                node.right = rec(None,t2.right,node.right)
                node.left = rec(None,t2.left,node.left)
            return node
        return rec(t1,t2,None)