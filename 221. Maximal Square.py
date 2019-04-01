class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        hm = [[0 for _ in matrix[0]] for _ in matrix]
        maxi = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    hm[i][j] = (1,0)[matrix[i][j]=="0"]
                elif matrix[i][j] == '1':
                    hm[i][j] = 1 + min(hm[i-1][j],hm[i][j-1],hm[i-1][j-1])
                maxi = max(hm[i][j], maxi)
        return maxi**2