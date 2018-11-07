class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for x in s:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        count1 = -1
        total = 0
        for k,v in d.items():
            total += v - v%2
            if count1 == -1 and v%2 != 0:
                total += 1
                count1 = 1
        return total