# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumTree(self,root, sum):
        sum += str(root.val)
        if root.left and root.right:
            self.sumTree(root.left, sum)
            self.sumTree(root.right, sum)
        elif root.left: 
            self.sumTree(root.left, sum)
        elif root.right: 
            self.sumTree(root.right, sum)
        else:
            self.sum += int(sum)

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.sum = 0
        self.sumTree(root, "")
        return self.sum
        