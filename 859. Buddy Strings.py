class Solution(object):
    def twosamecharac(self,A):
        d = {}
        for x in A:
            if x in d:
                return True
            else:
                d[x] = 1
        return False
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if not A or not B or len(A) != len(B):
            return False
        newA = []
        newB = []
        for x in range(len(A)):
            if A[x] != B[x]:
                newA.append(A[x])
                newB.append(B[x])
        newA.sort()
        newB.sort()
        if len(newA) == 0:
            return self.twosamecharac(A)
        if len(newA) != 2 or newA != newB:
            return False
        else:
            return True