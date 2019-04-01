class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        import numpy as np
        hm = [0 for _ in range(len(s) + 1)]
        for i in range(len(s)-1,-1,-1):
            hm[i] = np.min([hm[j] + (0,float('inf'))[s[i:j] not in wordDict] for j in range(i+1,len(s) + 1)])
        return True if hm[0] == 0 else False