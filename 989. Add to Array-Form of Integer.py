class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        if K <= 0: return A
        string =  "".join([str(x) for x in A])
        string = int(string) + K
        ans = []
        while string > 0:
            c = string % 10
            string /= 10
            ans = [c] + ans
        return ans