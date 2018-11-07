class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        peri = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    if 0 <= i-1 < len(grid) and  0 <= j < len(grid[0]) and not grid[i-1][j]:
                        peri+=1
                    elif not (0 <= i-1 < len(grid) and  0 <= j < len(grid[0])):
                        peri+=1
                    if 0 <= i < len(grid) and 0 <= j-1 < len(grid[0]) and not grid[i][j-1]:
                        peri+=1
                    elif not ( 0 <= i < len(grid) and 0 <= j-1 < len(grid[0])):
                        peri+=1
                    if 0 <= i < len(grid) and 0 <= j+1 < len(grid[0]) and not grid[i][j+1]:
                        peri+=1
                    elif not (0 <= i < len(grid) and 0 <= j+1 < len(grid[0])):
                        peri+=1
                    if 0 <= i+1 < len(grid) and 0 <= j < len(grid[0]) and not grid[i+1][j]:
                        peri+=1
                    elif not (0 <= i+1 < len(grid) and 0 <= j < len(grid[0])):
                        peri+=1                   
        return peri