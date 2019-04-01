# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def findSpot(node, val):
            if not node:
                return TreeNode(val)
            else:
                if val < node.val:
                    node.right = findSpot(node.right, val)
                else:
                    newNode = TreeNode(val)
                    newNode.left = node
                    return newNode
                return node
        return findSpot(root, val)