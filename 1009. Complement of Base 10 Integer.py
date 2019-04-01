class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        return int("".join(["1" if x=="0" else "0" for x in bin(N)[2:]]), 2)