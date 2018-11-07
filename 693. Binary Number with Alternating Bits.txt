class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary = bin(n)[2:]
        for i in range(len(binary)-1):
            if int(binary[i]) ^ 1 == int(binary[i+1]): continue
            else: return False
        return True