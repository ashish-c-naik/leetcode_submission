# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def G(root,string):
            if not root:
                return string
            else:
                if not root.left and  not root.right:
                    return string+str(root.val)
                else:
                    string += str(root.val)
                    if root.left:
                        string = G(root.left, string+str('('))
                        string += str(')')
                    else:
                        string+=str("()")
                    if root.right:
                        string = G(root.right, string+str('('))
                        string += str(')')
            return string
        return G(t,"")
