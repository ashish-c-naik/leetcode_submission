class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in range(1,len(A)):
            for j in range(len(A)):
                A[i][j] += min(A[i-1][j], min(A[i-1][max(j-1, 0)], A[i-1][min(len(A) - 1, j+1)]))
        return min(A[-1])