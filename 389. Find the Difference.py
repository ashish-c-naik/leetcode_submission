class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        n = 0
        for x in s:
            n ^= ord(x)
        for y in t:
            n^= ord(y) 
        return chr(n)