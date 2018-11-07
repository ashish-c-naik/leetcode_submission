class Solution(object):
    def DFS(self,x,y, grid):
        grid[x][y] = 'X'
        for i in (-1,0,1):
            if 0 <= x+i < self.row and grid[x+i][y] == "1":
                self.DFS(x+i, y, grid)
        for j in (-1,0,1):
            if 0 <= y+j < self.col and grid[x][y+j] == "1":
                self.DFS(x, y+j, grid)
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []: return 0
        self.row = len(grid)
        self.col = len(grid[0])
        self.count = 0
        for x in range(self.row):
            for y in range(self.col):
                if grid[x][y] == "1":
                    self.DFS(x,y,grid)
                    self.count += 1
        return self.count