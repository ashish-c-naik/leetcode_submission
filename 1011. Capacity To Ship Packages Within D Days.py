class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        left, right = max(weights), max(weights)*len(weights)
        while left < right:
            mid = (left+right)//2
            req, i, cap = 0, 0, 0
            while i < len(weights):
                cap += weights[i]
                if cap > mid:
                    req += 1
                    cap = weights[i]
                i+=1
            # print(req, mid)
            if req <= D - 1: right = mid
            else: left = mid + 1
        return left
                
                    