class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        i = 0
        j = 0
        flag = True
        cntz = 0
        maxi = 0
        while j < len(A) and i < len(A):
            if flag:
                if A[j] == 0:
                    cntz += 1
                    if cntz > K:
                        flag = False
                j += 1
            else:
                if A[i] == 0:
                    cntz -= 1
                    if cntz <= K:
                        flag = True
                i += 1
            if flag: maxi = max(maxi, j-i)
        return maxi