class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = num % 2147483646
        return int(bin(num)[2:].replace("0","u").replace("1","0").replace("u","1"),2)
        