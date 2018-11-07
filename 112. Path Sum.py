# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def find(root,sum):
            if root == None:
                return False
            sum -= root.val
            if root.right == None and root.left == None:
                return sum==0
            else:
                return find(root.right,sum) or find(root.left,sum)
        return find(root,sum)
            
            