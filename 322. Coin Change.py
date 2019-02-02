class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins = list(set(coins))
        coins = sorted(coins, reverse=True)
        self.res = float('inf')
        def r(total, remain, index):
            if index == len(coins) or remain == 0:
                if remain == 0:
                    self.res = min(self.res, total)
            else:
                for i in range(index, len(coins)):
                    if coins[i] <= remain < coins[i] * (self.res-total):
                        r(total+1, remain-coins[i], i)
        r(0, amount, 0)
        return self.res if self.res != float('inf') else -1