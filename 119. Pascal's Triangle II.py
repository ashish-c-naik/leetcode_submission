class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        l = []
        count = 1
        while rowIndex+1>0:
            ll = [1]*count
            if l:
                x=1
                while x<len(ll)-1:
                    ll[x]=l[-1][x-1]+l[-1][x]
                    x+=1
            l.append(ll)
            rowIndex-=1
            count+=1
        return l[-1]