class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        hm = {1:0,2:1}
        for i in range(3,n+1,2):
            hm[i+1] = hm[(i+1)//2] + 1
            hm[i] = min(hm[i-1], hm[i+1]) + 1
        return hm[n]