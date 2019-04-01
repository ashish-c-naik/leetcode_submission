class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if N == 0: return -1
        
        adjacency_matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
        
        for value in trust:
            adjacency_matrix[value[0]][value[1]] = 1
        
        def isJudge(label):
            for col in range(1, N+1):
                if adjacency_matrix[label][col] == 1:
                    return False
            for row in range(1, N+1):
                if adjacency_matrix[row][label] == 0 and row != label:
                    return False
            return True
        
        for label in range(1, N+1):
            if isJudge(label):
                return label
        return -1
        