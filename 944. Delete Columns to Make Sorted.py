class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        a = zip(*A)
        d = []
        for index, value in enumerate(a):
            if any([value[i] > value[i+1] for i,x in enumerate(value[:-1])]):
                d.append(index)
        return len(d)