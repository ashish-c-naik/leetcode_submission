class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return 0
        l = nums[:]
        m = max(nums)
        nums.remove(m)
        n = max(nums)
        return l.index(m) if m >= n*2 else -1