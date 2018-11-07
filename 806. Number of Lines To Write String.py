class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        if not S:
            return [0,0]
        d = {}
        maxlength = 100
        numberoflines = 1
        length = 0
        letters = "abcdefghijklmnopqrstuvwxyz"
        for index,char in enumerate(letters):
            d[char] = widths[index]
        for x in S:
            l = d[x]
            length += l
            if length > maxlength:
                numberoflines += 1
                length = l
            if length == maxlength:
                length = 0
                numberoflines += 1
        return [numberoflines,length]
        