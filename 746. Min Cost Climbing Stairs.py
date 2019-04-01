class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        import numpy as np
        
        hm = [0 for _ in range(len(cost)+1)]
        
        for i in range(len(cost)-1,-1,-1):
            hm[i] = np.min([hm[j]+cost[i] for j in range(i+1,i+3) if j < len(cost)+1])

        return (hm[0].item(), hm[1].item())[hm[1]<hm[0]]
