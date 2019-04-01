class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        l = [float(target-x)/y for x,y in sorted(zip(position, speed), reverse=True)]
        res = cur = 0
        for x in l:
            if x > cur:
                res+=1
                cur = x
        return res