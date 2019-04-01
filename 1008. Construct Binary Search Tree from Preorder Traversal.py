# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        def generate(preorder):
            if not preorder or len(preorder) == 1: 
                return None if not preorder else TreeNode(preorder[0])
            else:
                index = 0
                while index < len(preorder) and preorder[index] <= preorder[0]:
                    index+=1
                new = TreeNode(preorder[0])
                new.right = generate(preorder[index:])
                new.left = generate(preorder[1:index])
                return new
        return generate(preorder)