class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def check(s1):
            return s1==s1[::-1] and len(s1) > 0
        m = {}
        for i in range(len(s)):
            for j in range(i, len(s)+1):
                if check(s[i:j]):
                    if s[i:j] in m:
                        m[s[i:j]] += 1
                    else:
                        m[s[i:j]] = 1
        return sum(m.values())
        