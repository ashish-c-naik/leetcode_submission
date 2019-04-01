class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.arr = []
        self.last = N

    def seat(self):
        """
        :rtype: int
        """
        N, L = self.last, self.arr
        if not L: res = 0
        else:
            d, res = L[0], 0
            for a, b in zip(L, L[1:]):
                if (b - a) / 2 > d:
                    d, res = (b - a) / 2, (b + a) / 2
            if N - 1 - L[-1] > d: res = N - 1
        bisect.insort(L, res)
        return res

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        self.arr.remove(p)
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)