class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = 0
        stack = []
        stack_ = []
        if N >=4:
            stack.append(((N*(N-1))/(N-2)))
            stack.append(N-3)
            for x in range(N-4,0,-4):
                if x-3 >= 1:
                    stack_.append(((x*(x-1))/(x-2)))
                    stack.append((x -3))
                else:
                    k = x
                    if k == 3:
                        stack_.append((x*(x-1))/(x-2))
                    if k == 2:
                        stack_.append((x*(x-1)))
                    if k == 1:
                        stack_.append(x)
            return sum(stack) - sum(stack_)
        else:
            if N==3: s = 6
            elif N==2: s = 2
            elif N ==1: s = 1
        return s
        