class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = "".join([x for x in s if x.isalnum()]).lower()
        return n == n[::-1]