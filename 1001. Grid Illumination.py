class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        """
        :type N: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        row_, col_, d_, ad_ = collections.defaultdict(int), collections.defaultdict(int), collections.defaultdict(int), collections.defaultdict(int)
        lamps_ = collections.defaultdict(int)
        total = []
        for x in lamps:
            r, c = x[0], x[1]
            row_[r]+=1
            col_[c]+=1
            d_[r-c]+=1
            ad_[r+c]+=1
            lamps_[(r,c)]
        for x in queries:
            r, c = x[0], x[1]
            if r in row_ or c in col_ or r-c in d_ or r+c in ad_:
                total.append(1)
            else:
                total.append(0)
            for i,j in ((-1,-1), (-1,0), (-1,1), (0,-1), (0,0), (0, 1), (1,-1), (1,0), (1,1)):
                if (r+i, c+j) in lamps_:
                    row_[r+i]-=1
                    if row_[r+i] == 0: del row_[r+i]
                    col_[c+j]-=1
                    if col_[c+j] == 0: del col_[c+j]
                    d_[r+i-c-j]-=1
                    if d_[r+i-c-j]==0: del d_[r+i-c-j]
                    ad_[r+i+c+j]-=1
                    if ad_[r+i+c+j]==0: del ad_[r+i+c+j]
                    del lamps_[(r+i,c+j)]
        return total
            
        