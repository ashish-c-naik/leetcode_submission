class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        if len(nums) == 0: return 0
        if len(nums) == 2: return max(nums[0], nums[1])
        def helper(nums):
            # print(nums)
            for i in range(2, len(nums)):
                nums[i] = max(nums[i-2] + nums[i], nums[i] + (0,nums[i-3])[i-3>=0])
            # print(nums)
            return max(nums[-1], nums[-2])
        return max(helper(nums[0:len(nums)-1]),helper(nums[1:]))