class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.left_ = 0
        self.dup = 1
class Solution(object):
    def placeNode(self, root, val, point, ans):
        if not root:
            ans.append(point)
            root = Node(val)
        elif root.val == val:
            root.dup+=1
            ans.append(point+root.left_)
        elif root.val > val:
            root.left_ += 1
            root.left = self.placeNode(root.left, val, point, ans)
        else:
            root.right = self.placeNode(root.right, val, point+root.left_+root.dup, ans)
        return root
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_ = nums[::-1]
        root = None
        ans = []
        for i in nums_:
            root = self.placeNode(root, i, 0, ans)
        return ans[::-1]
                