class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        B = []
        index = 0
        for x in A:
            if K == 0 or x >= 0: break
            B.append(-x)
            index+=1
            K-=1
        B += A[index:]
        B.sort()
        if K%2!=0:
            B[0] = -B[0]
        else:
            B[0] = B[0]
        return sum(B)
                
            