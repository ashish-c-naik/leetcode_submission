class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlength = 0
        l = list()
        for char in s:
            if char in l:
                index = l.index(char)
                l = l[index+1:]
                l.append(char)
                
            else:
                l.append(char)
            length = len(l)
            if maxlength < length:
                maxlength = length
        return maxlength