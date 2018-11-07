class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        sum1=sum(nums)
        nums=set(nums)
        sum2=sum(nums)
        rep=sum1-sum2
        mis=(1+n)*n/2-sum2
        return [rep,mis]