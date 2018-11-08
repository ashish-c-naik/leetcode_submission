class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        alpha = []
        for x in range(len(s)):
            if s[x] not in d:
                if t[x] not in alpha:
                    d[s[x]] = t[x]
                    alpha.append(t[x])
                else:
                    return False
            elif d[s[x]] != t[x]:
                return False
        return True