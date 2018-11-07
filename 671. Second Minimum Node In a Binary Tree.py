# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recur(self,root,arr):
        if root == None:
            return arr
        else:
            self.recur(root.right,arr)
            arr.append(root.val)
            self.recur(root.left,arr)
        return arr
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        n = []
        arr = self.recur(root,[])
        ans = list(set(arr))
        ans.sort()
        return (ans[1] if len(ans) != 1 else -1)
        