class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = [-1]*len(nums)
        def rob(index):
            if index >= len(nums):
                return 0
            elif hash_table[index] != -1:
                return hash_table[index]
            else:
                hash_table[index] = max(nums[index] + rob(index + 2), nums[index] + rob(index + 3))
                return hash_table[index]
        maxi = 0
        for x in range(len(nums)):
            maxi = max(maxi, rob(x))
        return maxi
        