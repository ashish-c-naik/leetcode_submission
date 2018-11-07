class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for x in s:
            if x in d: d[x] += 1
            else: d[x] = 1
        for index, x in enumerate(list(s)):
            if d[x] == 1: return index
        return -1