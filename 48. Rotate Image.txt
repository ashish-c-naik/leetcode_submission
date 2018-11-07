class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix:
            r1 = 0
            r2 = len(matrix) - 1
            c1 = 0
            c2 = len(matrix[0]) - 1
            while r1<r2 and c1<c2:
                for i in range(0,c2-c1):
                    t = matrix[r1+i][c2]
                    matrix[r1+i][c2] = matrix[r1][c1+i]
                    t2 = matrix[r2][c2-i]
                    matrix[r2][c2-i] = t
                    t = t2
                    t2 = matrix[r2-i][c1]
                    matrix[r2-i][c1] = t
                    matrix[r1][c1+i] = t2
                r1+=1
                r2-=1
                c1+=1
                c2-=1
