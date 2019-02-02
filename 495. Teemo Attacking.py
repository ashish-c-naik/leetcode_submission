class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        d, amt = 0, 0
        for x in timeSeries:
            if d > x: amt -= (d - x)
            amt += duration
            d = x + duration
        return amt    
                
                