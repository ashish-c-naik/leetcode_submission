class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = set()
        nums.sort()
        for x,v in enumerate(nums[:-2]):
            if x >= 1 and v == nums[x-1]:
                continue
            d = {}
            for y in range(x+1,len(nums)):
                complement = -(nums[x] + nums[y])
                if nums[y] in d:
                    s,t = d[nums[y]]
                    ans.add((s,t,nums[y]))
                d[complement] = (nums[x],nums[y])
        return [list(i) for i in ans]