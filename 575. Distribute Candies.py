class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        total = len(candies) / 2
        return min(len(set(candies)),total)