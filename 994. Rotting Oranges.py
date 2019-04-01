class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxi = 0
        num_of_ones = 0
        queue = collections.deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if  grid[i][j] == 1:
                    num_of_ones += 1
        # print(queue)
        while queue:
            for elem in range(len(queue)):
                x,y = queue.popleft()
                for i,j in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                    if 0 <= i < len(grid) and 0 <= j < len(grid[0]) \
                    and grid[i][j] == 1:
                        grid[i][j] = 2
                        queue.append((i,j))
                        num_of_ones -= 1
            if queue: maxi += 1
        return maxi if num_of_ones == 0 else -1
                