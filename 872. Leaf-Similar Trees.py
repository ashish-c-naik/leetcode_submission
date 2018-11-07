# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def leafval(root,arr):
            if not root:
                return arr
            else:
                if not root.right and not root.left:
                    arr.append(root.val)
                else:
                    leafval(root.right,arr)
                    leafval(root.left,arr)
            return arr
        return leafval(root1,[])==leafval(root2,[])