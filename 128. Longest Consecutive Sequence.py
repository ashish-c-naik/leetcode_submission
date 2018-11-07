class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        ans = []
        for x in nums:
            if x - 1 in nums:
                ans.append(x)
            elif x + 1 in nums:
                ans.append(x)
        ans.sort()
        print(ans)
        return len(ans)