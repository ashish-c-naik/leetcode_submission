class Solution(object):
    """
    Recurrsive solution below:
    """
    # def generate(self,val):
    #     if val in self.hm: return self.hm[val]
    #     for i in range(1, val+1):
    #         self.hm[val] += self.generate(i-1) * self.generate(val-i)
    # def numTrees(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     self.hm = collections.defaultdict(int)
    #     self.hm[0] = self.hm[1] = 1
    #     for i in range(2,n+1):
    #         self.generate(i)
    #     return self.hm[n]
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.hm = collections.defaultdict(int)
        self.hm[0] = self.hm[1] = 1
        for i in range(2,n+1):
            for j in range(1, i+1):
                self.hm[i] += self.hm[j-1] * self.hm[i-j]
        return self.hm[n]