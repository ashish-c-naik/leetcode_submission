class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        mini = float("inf")
        i = 0
        j = 0
        ran = [-1,-1]
        flag = False
        hm_ = collections.Counter(t)
        hm = collections.defaultdict(int)
        while  j < len(s) or i < len(s):
            if not flag and j < len(s):
                hm[s[j]] += 1
                if not any(hm[x] < hm_[x] for x in hm_.keys()): flag = True
                j += 1
            else:
                if s[i] in hm_: 
                    hm[s[i]] = hm[s[i]] - 1 if hm[s[i]] > 1 else 0
                    if hm[s[i]] < hm_[s[i]]: flag = False
                i += 1
            if flag: 
                mini = min(mini, j-i)
                if mini == j-i:
                    ran[0] = i
                    ran[1] = j
        return s[ran[0]:ran[1]] if ran[0] != -1 and ran[1] != -1 else ""