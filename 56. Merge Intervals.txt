# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        d = {}
        for x in intervals:
            if x.start in d:
                if x.end > d[x.start][1]:
                    d[x.start] = [x.start,x.end]
            else:
                d[x.start] = [x.start,x.end]
        prevend = prevstart = None
        ans = []
        for x in sorted(d.keys()):
            if prevend == None:
                prevend = d[x][1]
                prevstart = d[x][0]
            else:
                if prevend >= d[x][0]:
                    prevend = max(d[x][1], prevend)
                else:
                    ans.append([prevstart,prevend])
                    prevend = d[x][1]
                    prevstart = d[x][0]
        if prevstart != None and prevend != None:
            ans.append([prevstart,prevend])
        return ans
            
                