class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        from collections import Counter
        def gcd(a,b):
            while b: a,b = b, a%b
            return a
        count = Counter(deck)
        return reduce(gcd, count.values()) > 1