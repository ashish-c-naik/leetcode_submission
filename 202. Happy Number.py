class Solution(object):
    def getnext(self,n):
        sum = 0
        while n > 0:
            s = n%10
            sum += s*s
            n/=10
        return sum
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        while True:
            num = self.getnext(n)
            if num in visited:
                return False
            if num == 1:
                return True
            visited.add(num)
            n = num
        return False
            