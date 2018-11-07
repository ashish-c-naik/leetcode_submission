class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "": return ""
        strings = {}
        def calculate(i,j):
            string = ""
            while 0<= i and j <= len(s) - 1 and s[i]==s[j]:
                if i == j: string+=s[i]
                else: string = (s[i] + string + s[i])
                i-=1
                j+=1
            return string
        for i in range(len(s)):
            n = (calculate(i,i))
            strings[len(n)] = n
            if i+1 < len(s):
                n = (calculate(i,i+1))
                strings[len(n)] = n
        return strings[max(strings.keys())]