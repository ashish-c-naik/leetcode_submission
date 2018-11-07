class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def add(str):
            if len(str) > 1:
                newnum = 0
                for x in str:
                    newnum += int(x)
                return newnum
        while num > 9:
            num = add(str(num))
        return num