class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        ans = []
        for x in ops:
            if x == '+':
                if ans[-1]: s = ans[-1]
                if ans[-2]: s+=ans[-2]
                ans.append(s)
            elif x == 'D':
                ans.append(ans[-1]*2)
            elif x == 'C':
                ans.pop()
            else:
                ans.append(int(x))
        #print(ans)
        return sum(ans)
            