class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        x = 0
        y = 0
        while x < len(nums) and y < len(nums):
            while x < len(nums):
                if nums[x] != 0:
                    x+=1
                else:
                    break
            y = x
            while y < len(nums):
                if nums[y] == 0:
                    y+=1
                else: break
            if x<len(nums) and y < len(nums) and x < y:
                nums[x], nums[y] = nums[y], nums[x]
                x+=1
                y+=1
            