# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(root,arr):
            if root:
                arr = inorder(root.left,arr)
                arr.append(root.val)
                arr = inorder(root.right,arr)
            return arr
        arr = inorder(root,[])
        return arr[k-1]