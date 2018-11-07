class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        ans = []
        index = 0
        for elem in nums:
            if elem in d:
                ans.append(d[elem])
                ans.append(index)
                return ans
            d[target - elem] = index
            index += 1
        return False
            
        