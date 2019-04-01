class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        hm = [0 for x in range(days[-1]+1)]
        for i in range(days[-1]+1):
            hm[i] = hm[max(i-1,0)] if i not in days else \
            min(hm[max(0, i-7)]+costs[1],hm[max(i-1,0)]+costs[0],hm[max(i-30,0)]+costs[2])
        return hm[-1]