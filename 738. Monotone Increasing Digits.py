class Solution(object):
    def recurseFindNumber(self, num, place):
            if place > self.l: return int(num), int(self.N) >= int(num)
            for x in range(9,-1,-1):
                if place >= 1 and x < int(num[-1]): break
                n, f = self.recurseFindNumber(num+str(x), place+1)
                if f: return n, f
            return None, False
        
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        self.N = str(N)
        self.l = len(self.N) - 1
        return self.recurseFindNumber("", 0)[0]