# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def check(qu):
            x=0
            y=len(qu)-1
            while x < y:
                if qu[x].val != qu[y].val:
                    return False
                x+=1
                y-=1
            return True
        def RL(q):
            qu = []
            if q:
                while len(q)!=0:
                    node = q[0]
                    q = q[1:]
                    if node.right:
                        qu.append(node.right)
                    if node.left:
                        qu.append(node.left)
                if not check(qu):
                    return False
                RL(qu)
            return True
        return RL([root])
                