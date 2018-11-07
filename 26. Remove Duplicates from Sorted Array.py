class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        x = 1
        y = 1
        prev = nums[0]
        while y < len(nums) and x < len(nums):
            while y<len(nums) and prev == nums[y]:
                y+=1
            if y >= len(nums):
                break
            prev = nums[y]
            nums[x] = nums[y]
            x+=1
        return x