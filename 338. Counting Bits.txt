class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]*(num+1)
        for x in range(1,num+1):
            ans[x] = ans[x&(x-1)] + 1
        return ans