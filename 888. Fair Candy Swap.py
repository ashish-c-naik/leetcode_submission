class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        d = collections.Counter(B)
        s1 = sum(A)
        s2 = sum(B)
        for x in A:
            if (s1 - s2 - 2*x)//-2 in d:
                return [x, (s1 - s2 - 2*x)//-2]