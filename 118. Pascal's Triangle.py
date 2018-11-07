class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l = []
        count = 1
        while numRows>0:
            ll = [1]*count
            if l:
                x=1
                while x<len(ll)-1:
                    ll[x]=l[-1][x-1]+l[-1][x]
                    x+=1
            l.append(ll)
            numRows-=1
            count+=1
        return l