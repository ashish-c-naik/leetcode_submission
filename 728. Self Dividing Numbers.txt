class Solution(object):
    def check(self,num):
        numcopy = num
        while num:
            digit = num % 10
            num /= 10
            if digit == 0 or numcopy % digit != 0 :
                return False
        return True
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = list()
        for x in range(left,right+1):
            if self.check(x):
                ans.append(x)
        return ans