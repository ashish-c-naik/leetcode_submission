class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.replace(".","").replace(",","").replace(";","").replace("'","").replace("?","").replace("!","")
        l = paragraph.split(" ")
        d = {}
        for x in l:
            x = x.lower()
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        for key, value in sorted(d.iteritems(), key=lambda (k,v): (v,k))[::-1]:
            if key not in banned:
                return key
        return ""