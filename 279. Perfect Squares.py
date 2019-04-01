class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import numpy as np
        t = int(math.floor(math.sqrt(n)))
        hm = []
        for i in range(t,-1,-1):
            hm.append(i**2)
        def helper(index, remain, total):
            if index == len(hm) or remain == 0:
                if remain == 0:
                    self.mini = min(self.mini, total)
            else:
                for i in range(len(hm)):
                    if hm[i] <= remain < hm[i]*(self.mini-total):
                        helper(i, remain-hm[i], total+1)
        self.mini = float('inf')
        helper(0,n,0)
        return self.mini