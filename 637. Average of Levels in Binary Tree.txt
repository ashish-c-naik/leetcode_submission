# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        def binary(root,level,arr):
            if not root:
                return arr
            else:
                if level >= len(arr):
                    arr.append([])
                l = []
                if root.right:
                    l.append(root.right.val)
                if root.left:
                    l.append(root.left.val)
                arr[level].extend(l)
                binary(root.right,level+1,arr)
                binary(root.left,level+1,arr)
            return arr
        arr = binary(root,1,[[root.val]])
        ans = []
        for x in arr:
            if x == []:
                continue
            ans.append(sum(x)/float(len(x)))
        return(ans)