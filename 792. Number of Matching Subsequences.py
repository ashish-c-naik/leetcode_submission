class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        ini = len(words)
        hm = collections.defaultdict(list)
        for index, x in enumerate(words):
            hm[x[0]].append(index) 
        for x in S:
            # print(hm)
            if x in hm:
                l = hm[x]
                del hm[x]
                # print(l, words)
                for i in l:
                    if words[i][0] == "": 
                        continue
                    elif len(words[i]) == 1:
                        words[i] = words[i][1:]
                    else: 
                        hm[words[i][1]].append(i)
                        words[i] = words[i][1:]
        
        return sum([1 for x in words if x == ""])