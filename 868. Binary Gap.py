class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        b = bin(N)[2:]
        start = 0
        if b[start] == '1':
            flag = True
        else:
            flag = False
        m = 0
        for x in range(1,len(b)):
            if b[x] == '1' and flag:
                if m < (x - start):
                    m = x - start
                flag = True
                start = x
            elif b[x] == '1' and not flag:
                flag = True
                start = x
        return m
            