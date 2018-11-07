class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 0
        maxtillnow = 0
        for x in nums:
            if x ^ 1 == 0:
                m += 1
            else:
                maxtillnow = max(m,maxtillnow)
                m = 0
        if m:
            maxtillnow = max(m,maxtillnow)
        return maxtillnow
        