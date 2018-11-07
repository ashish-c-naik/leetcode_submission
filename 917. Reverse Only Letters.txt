class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        letters = [x for x in S if ord('A') <= ord(x) <= ord('Z') or ord('a')<= ord(x) <= ord('z')]
        s = ""
        for x in S:
            if ord('A') <= ord(x) <= ord('Z') or ord('a')<= ord(x) <= ord('z'):
                s += letters.pop()
            else:
                s += x
        return s