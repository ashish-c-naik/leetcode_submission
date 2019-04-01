class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        hm = collections.defaultdict(int)
        count = 0
        for x in time:
            # if x % 60 == 0:
            #     count += 1
            new = x % 60
            # print(new, hm)
            if new in hm:
                count += hm[new]
            hm[60-new] += 1
            if new == 0: hm[new] += 1
        return count