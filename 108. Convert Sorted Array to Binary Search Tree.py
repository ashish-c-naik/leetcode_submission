# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def tobst(arr,x,y):
            if arr and x <= y:
                mid = (x+y)//2
                node = TreeNode(arr[mid])
                node.right = tobst(arr,mid+1,y)
                node.left = tobst(arr,x,mid-1)
                return node
        return tobst(nums,0,len(nums) - 1) 
        