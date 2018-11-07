class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        l = []
        for index,x in enumerate(S):
            if x == C:
                l.append(index)
        return [min([abs(index-v) for v in l]) for index in range(len(S))]
        