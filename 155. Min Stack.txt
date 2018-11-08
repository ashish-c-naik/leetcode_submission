class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.mindata = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.data:
            self.data.append(x)
            self.mindata.append(x)
        else:
            self.data.append(x)
            if self.mindata[-1] >= x:
                self.mindata.append(x)
                
    def pop(self):
        """
        :rtype: void
        """
        if self.data:
            if self.mindata and self.data[-1] == self.mindata[-1]:
                self.mindata.pop()
            self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.data: return self.data[-1]
        else: return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.mindata: return self.mindata[-1]
        else: return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()