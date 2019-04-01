class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = []
        x,y = 0,len(A)-1
        while x <= y:
            o,t = abs(A[x]), abs(A[y])
            if o < t:
                ans = [t**2] + ans
                y -= 1
            else:
                ans = [o**2] + ans
                x += 1
        return ans