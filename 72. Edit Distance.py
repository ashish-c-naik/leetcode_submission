class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) == 0: return len(word2)
        if len(word2) == 0: return len(word1)
        hm = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2)+1)]
        for i in range(len(word2)+1):
            hm[i][0] = i
        for j in range(len(word1)+1):
            hm[0][j] = j
        for i in range(1,len(word2)+1):
            for j in range(1,len(word1)+1):
                hm[i][j] = min(
                            hm[i][j-1] + 1,
                            hm[i-1][j] + 1,
                            hm[i-1][j-1] + (1,0)[word1[j-1] == word2[i-1]]
                        )
        return hm[len(word2)][len(word1)]
                