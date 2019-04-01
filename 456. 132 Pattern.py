class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == []: return False
        mini = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]: continue
            for j in range(i+1,len(nums)):
                if nums[j] == nums[j-1]: continue
                if mini < nums[j] < nums[i]:
                    return True
            mini = min(mini, nums[i])
        return False