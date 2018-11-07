class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        count = 0
        t = 0
        for x in s:
            if count > 0:
                t += (26**count)*(ord(x) - ord('A') + 1)
            else:
                t += ord(x) - ord('A') + 1
            count += 1
        return t