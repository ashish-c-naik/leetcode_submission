class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # l = [[[-1]*(n+1)]*(m+1)]*(len(strs)+1) DONT USE!!!
        # the * is for shallow copy, it will only point everything to the same list of [-1].
        l = [[[-1]*(n+1) for _ in range(m+1)] for _ in range(len(strs)+1)]
        def r(rem, m, n):
            if l[rem][m][n] != -1: return l[rem][m][n]
            if (m == 0 and n == 0) or rem < 0:
                return 0
            zero = strs[rem].count("0")
            one = strs[rem].count("1")
            if zero > m or one > n:
                result = r(rem-1, m,n)
            else:
                t1 = r(rem-1, m, n)
                t2 = r(rem-1, m - zero, n - one) + 1
                result = max(t1, t2)
            l[rem][m][n] = result
            return result
        return r(len(strs)-1, m, n)