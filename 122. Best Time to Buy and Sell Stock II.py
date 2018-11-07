class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        mini = None
        maxi = None
        profit = 0
        for x in prices:
            if mini == None and maxi == None:
                mini = x
                maxi = x
            else:
                if maxi < x:
                    maxi = x
                else:
                    profit += maxi - mini
                    maxi = x
                    mini = x
        profit+= maxi-mini
        return profit
        