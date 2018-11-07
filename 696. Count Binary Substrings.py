class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = list(map(len, s.replace("01", "0 1").replace("10", "1 0").split()))
        return sum(min(a,b) for a,b in zip(m,m[1:]))