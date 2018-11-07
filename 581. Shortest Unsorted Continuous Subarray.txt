class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = nums[:]
        s.sort()
        if s == nums:
            return 0
        l = map(lambda x, y: 1 if x!=y else 0, nums, s)
        return len(l) - l.index(1) - l[::-1].index(1)