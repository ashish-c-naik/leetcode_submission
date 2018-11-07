class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for x in nums:
            if x in d:
                return x
            else:
                d[x] = 1
        return -1