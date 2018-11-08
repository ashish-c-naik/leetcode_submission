class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        l = []
        for index, x in enumerate(nums[::-1]):
            if index < k:
                l.append(x)
            else:
                break
        emptypos = len(nums) - 1
        nonempty = len(nums) - 1 - index
        while nonempty >= 0:
            nums[emptypos], nums[nonempty] = nums[nonempty], nums[emptypos]
            emptypos -= 1
            nonempty -= 1
        index = 0
        while l:
            nums[index] = l.pop()
            index += 1
        
        