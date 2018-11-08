class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            neg = -1
        else:
            neg = 1
        copyNum = abs(x)
        newNum = 0
        index = 0
        digit = 0
        while copyNum > 0:
            digit = digit + 1
            copyNum /= 10
        print(digit)
        copyNum = abs(x)
        while copyNum > 0:
            newNum = newNum + (10**((digit - index)-1) * (copyNum%10))
            print(newNum)
            index = index+1
            copyNum = copyNum / 10
        if newNum > 2147483647:
            return 0
        else:
            return newNum * neg