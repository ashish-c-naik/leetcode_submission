class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        for i in range(len(A)-1, 1, -1):
            if A[i] < A[i-1]+A[i-2]:
                return A[i]+A[i-1]+A[i-2]
        return 0