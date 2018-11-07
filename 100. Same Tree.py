# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def recur(root):
            ans = []
            def r(root):
                if root == None:
                    ans.append(None)
                    return
                else:
                    if root.right == None and root.left == None:
                        ans.append(root.val)
                        return
                    else:
                        ans.append(root.val)
                        r(root.left)
                        r(root.right)
                return
            r(root)
            return ans
        return recur(p) == recur(q)