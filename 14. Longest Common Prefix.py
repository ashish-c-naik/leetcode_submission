class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        def commonPrefix(one,two):
            s = ""
            pointer = 0
            while pointer < len(one) and pointer < len(two):
                if one[pointer] == two[pointer]:
                    s += one[pointer]
                else:
                    return s
                pointer += 1
            return s
        s = None
        for x in range(0,len(strs)):
            if s==None:
                s = strs[x]
                continue
            s = commonPrefix(s,strs[x])
        return s