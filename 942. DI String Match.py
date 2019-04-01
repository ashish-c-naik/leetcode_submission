class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        l = range(len(S)+1)
        i,j = 0, len(S)
        z = 0
        final = []
        while i <= j:
            if  i==j or S[z] == 'I':
                final.append(l[i])
                i+=1
            else:
                final.append(l[j])
                j-=1
            z+=1
        return final