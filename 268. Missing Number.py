class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum1 = sum(nums)
        return (n*(n+1))/2 - sum1