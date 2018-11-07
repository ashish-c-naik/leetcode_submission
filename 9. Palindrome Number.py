class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        start = 0
        end = len(str(x)) - 1
        strX = str(x)
        while start < end:
            if strX[start] != strX[end]:
                return False
            start+=1
            end-=1
        return True
        
        