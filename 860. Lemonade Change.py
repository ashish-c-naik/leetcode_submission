class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        d = {5:0, 10: 0, 20: 0}
        for x in bills:
            change = x - 5
            d[x] += 1
            while change > 0 and change - 20 >= 0 and d[20] > 0:
                change -= 20
                d[20] -= 1
            while change > 0 and change - 10 >= 0 and d[10] > 0:
                change -= 10
                d[10] -= 1
            while change > 0 and change - 5 >= 0 and d[5] > 0:
                change -= 5
                d[5] -= 1
            if change > 0:
                return False
        return True