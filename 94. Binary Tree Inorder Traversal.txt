# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self,root,arr):
        if root == None:
            return arr
        else:
            if root.left:
                arr = self.inorder(root.left,arr)
            arr.append(root.val)
            if root.right:
                arr = self.inorder(root.right,arr)
        return arr
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = self.inorder(root,[])
        return arr