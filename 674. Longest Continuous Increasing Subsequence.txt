class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = 0
        curr = 1
        for x in range(len(nums)):
            if x == len(nums) - 1:
                length = max(length, curr)
                break
            if nums[x] < nums[x+1]:
                curr += 1
            else:
                length = max(length, curr)
                curr = 1
        if length == 0 and len(nums) > 0: return 1
        else: return length