class RecentCounter(object):

    def __init__(self):
        self.list = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.list.append(t)
        while True:
            if t-3000 <= self.list[0] <= t:
                break
            else:
                del self.list[0]
        return len(self.list)