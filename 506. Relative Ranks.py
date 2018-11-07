class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        maxi = max(nums)
        d = {}
        for x in nums:
            d[maxi-x] = x
        ans = [-1]*len(nums)
        l = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        count = 1
        for k,v in sorted(d.items()):
            if l:
                ans[nums.index(v)] = l[0]
                l = l[1:]
            else:
                ans[nums.index(v)] = str(count)
            count+=1
        return ans