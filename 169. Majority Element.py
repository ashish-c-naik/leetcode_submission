class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for x in nums:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        for k,v in d.iteritems():
            if v > (len(nums)-1)//2:
                return k
        