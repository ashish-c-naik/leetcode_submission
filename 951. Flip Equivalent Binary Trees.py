# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        d = collections.defaultdict(list)
        d1 = collections.defaultdict(list)
        def recurse(root, l, d):
            if not root:
                return []
            else:
                l2 = l[:]
                for x in (root.right, root.left):
                    if x:
                        l1 = recurse(x, l[:], d)
                        l2.append(x.val)
                        l2.extend(l1)
                d[root.val].extend(l2)
                return l2
        recurse(root1, [], d)
        recurse(root2, [], d1)
        for k,v in d.items():
            if k not in d1 or sorted(d1[k]) != sorted(v):
                return False
        for k,v in d1.items():
            if  k not in d or sorted(d[k]) != sorted(v):
                return False
        return True
                        