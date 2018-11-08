class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0: return 0
        s = set()
        d = {}
        for x in nums:
            if x not in d:
                if x+k in d: d[x+k].append(x)
                else: d[x+k] = [x]
                if x-k in d: d[x-k].append(x)
                else: d[x-k] = [x]
            else:
                i = d[x]
                j = x
                for f in i:
                    t = (f,j) if f < j else (j,f)
                    if t in s:
                        continue
                    else:
                        s.add(t)
                        if f != x+k:
                            if x+k in d: d[x+k].append(x)
                            else: d[x+k] = [x]
                        else:
                            if x-k in d: d[x-k].append(x)
                            else: d[x-k] = [x]
        return len(s)