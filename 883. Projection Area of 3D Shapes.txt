class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x = sum([max(i) for i in zip(*grid)])
        print(x)
        x += sum([max(i) for i in grid])
        print(x)
        for i in grid:
            for j in i:
                if j != 0:
                    x += 1
        return x