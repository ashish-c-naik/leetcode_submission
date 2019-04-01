class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        l = [x.upper() for x in S if x.isalnum()]
        s = ""
        c = 0
        for i in l[::-1]:
            if c == 0:
                s += "-"+i
                c = K
            else:
                s += i
            c-=1
        return s[::-1].strip("-")