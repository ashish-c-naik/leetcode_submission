class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        l = [x for x in s if x in vowels]
        ns = ""
        for index,x in enumerate(s):
            if x in vowels:
                ns += str(l.pop())
            else:
                ns += x
        return ns