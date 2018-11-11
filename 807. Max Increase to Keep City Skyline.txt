class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        leftright = [-1]*len(grid)
        topbottom = [-1]*len(grid)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if topbottom[col] < grid[row][col]:
                    topbottom[col] = grid[row][col]
                if leftright[row] < grid[row][col]:
                    leftright[row] = grid[row][col]
        total = 0
        for row in range(len(grid)):
            for col in range(len(grid)):
                if topbottom[col] < leftright[row]:
                    small = topbottom[col]
                else:
                    small = leftright[row]
                total += small - grid[row][col]
                grid[row][col] = small
        return (total)