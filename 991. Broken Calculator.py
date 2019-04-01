class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        res = 0
        while X < Y:
            res += Y % 2 + 1
            Y = (Y+1)/ 2
        return res + X - Y