class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        start = 0
        end = start + k - 1
        newarr = []
        maxn = 0
        while end < len(nums):
            maxn = nums[start]
            s=0
            for i in range(start+1,end+1):
                if maxn < nums[i]:
                    maxn = nums[i]
            newarr.append(maxn)
            start += 1
            end += 1
        return newarr