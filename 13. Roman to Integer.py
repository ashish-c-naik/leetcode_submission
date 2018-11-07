class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        curr = 0
        prev = 0
        currsum = 0
        for x in s:
            curr = d[x]
            if curr <= prev: currsum += curr
            else: 
                currsum -= prev
                currsum += (curr-prev)
            prev = curr
        return currsum