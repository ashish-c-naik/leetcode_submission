class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentSum = nums[0]
        maximum = currentSum
        if not nums:
            return 0
        for i in range(1,len(nums)):
            if currentSum < 0:
                currentSum = 0
            currentSum += nums[i]
            maximum = max(currentSum,maximum)
        return maximum