class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def generate(k):
            i = 0
            t = ()
            while k > 0:
                if k & 1 == 1:
                    t = t + (nums[i],)
                k = k  >> 1
                i += 1
            return t
        total = 1<<len(nums)
        ans = set()
        for x in range(total):
            ans.add(generate(x))
        return list(ans)