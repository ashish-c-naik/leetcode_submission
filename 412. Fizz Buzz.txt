class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for x in range(1,n+1):
            if x%3 != 0 and x%5 != 0:
                ans.append(str(x))
            elif x%3 == 0 and x%5 == 0:
                ans.append("FizzBuzz")
            else:
                if x%3 == 0:
                    ans.append("Fizz")
                if x%5 == 0:
                    ans.append("Buzz")
        return ans