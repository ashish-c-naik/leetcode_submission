# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def r(root,p,q):
            if not root: return None
            if root.val == p.val or root.val == q.val: return root
            left = r(root.left,p,q)
            right = r(root.right,p,q)
            if left and (left.val == p.val or left.val == q.val) and right and (right.val == p.val or right.val == q.val):
                return root
            return left or right
        return r(root,p,q)