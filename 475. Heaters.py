class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        def bins(k,heaters,x,y):
            if abs(x-y) > 1:
                mid = (x + y) // 2
                if heaters[mid] == k:
                    return 0
                elif heaters[mid] >= k:
                    y = mid
                else:
                    x = mid
                return bins(k,heaters,x,y)
            else:
                return min(abs(heaters[x]-k),abs(heaters[y]-k))
        import sys
        d = {}
        heaters.sort()
        for x in houses:
            d[x] = sys.maxint
        for k,v in d.iteritems():
            val = bins(k,heaters,0,len(heaters)-1)
            d[k] = min(v,val)
        return (max(d.values()))