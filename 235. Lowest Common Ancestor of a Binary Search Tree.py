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
        q = q.val
        p = p.val
        pqueue = []
        qqueue = []
        head = root
        while head:
            pqueue.append(head.val)
            if head.val == p:
                break
            if head.val > p:
                head = head.left
            else:
                head = head.right
        head = root
        while head:
            qqueue.append(head.val)
            if head.val == q:
                break
            if head.val > q:
                head = head.left
            else:
                head = head.right
        ans = []
        pqueue,qqueue = pqueue[::-1], qqueue[::-1]
        for x in pqueue:
            if x in qqueue:
                return TreeNode(x)