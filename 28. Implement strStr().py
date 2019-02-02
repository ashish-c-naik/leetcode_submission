class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '': return 0
        window_size = len(needle)
        window_amt = sum([ord(x) for x in needle])
        size = 0
        amt = 0
        for index, x in enumerate(haystack):
            if size < window_size:
                amt += ord(x)
                size += 1
            elif size == window_size:
                amt -= ord(haystack[index - window_size])
                amt += ord(x)
            if size == window_size and amt == window_amt and \
                needle == haystack[index - window_size + 1:index + 1]:
                return index - window_size + 1
        return -1
        