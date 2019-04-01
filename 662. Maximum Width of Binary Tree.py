# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        curr = {root:1}
        next = {}
        w = 0
        while len(curr) > 0:
            mini = float('inf')
            maxi = float('-inf')
            for k, v in curr.items():
                maxi = max(maxi, v)
                mini = min(mini, v)
                if k.left: next[k.left] = v*2
                if k.right: next[k.right] = v*2+1
            curr = next
            next = {}
            w = max(w, maxi - mini + 1)
        return w