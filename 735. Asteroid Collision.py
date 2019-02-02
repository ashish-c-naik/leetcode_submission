class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        self.ans = []
        for val in asteroids:
            neg = val < 0
            if neg:
                while True:
                    if (self.ans and self.ans[-1] < 0) or not self.ans:
                        self.ans.append(val)
                        break
                    if self.ans and self.ans[-1] == abs(val):
                        self.ans.pop()
                        break
                    elif self.ans and self.ans[-1] < abs(val):
                        self.ans.pop()
                    else:
                        break
            else:
                self.ans.append(val)
        return self.ans