# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def changehm(self, hm, val, offset):
        if offset == 1:
            hm[val] += 1
        else:
            hm[val] -= 1
        return hm
    def getpaths(self, root, running_sum, target, hm):
        if not root: return 0
        running_sum += root.val
        v = running_sum - target
        total = 0
        if v in hm:
            total += hm[v]
        if running_sum == target:
            total += 1
        hm = self.changehm(hm, running_sum, 1)
        total += self.getpaths(root.left, running_sum, target, hm)
        total += self.getpaths(root.right, running_sum, target, hm)
        hm = self.changehm(hm, running_sum, -1)
        return total
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        hm = collections.defaultdict(int)
        return self.getpaths(root, 0, sum, hm)