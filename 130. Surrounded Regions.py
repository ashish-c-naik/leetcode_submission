class Solution(object):
    def dfs(self, x ,y ,board, symbol, look):
        board[x][y] = symbol
        for i in (-1,0,1):
            if 0 <= x+i < len(board) and board[x+i][y] == look:
                self.dfs(x+i, y, board, symbol, look)
        for i in (-1,0,1):
            if 0 <= y+i < len(board[0]) and board[x][y+i] == look:
                self.dfs(x, y+i, board, symbol, look)
        
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board == []: return
        y = 0
        for i in range(len(board[0])):
            if board[0][y+i]=='O': self.dfs(0, y+i, board, 'N', 'O')
            if board[len(board) - 1][y+i]=='O': self.dfs(len(board)-1, y+i, board, 'N', 'O')
        x = 0
        for i in range(len(board)):
            if board[x+i][0]=='O': self.dfs(x+i, 0, board, 'N', 'O')
            if board[x+i][len(board[0]) - 1]=='O': self.dfs(x+i, len(board[0]) - 1, board, 'N', 'O')
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O": board[i][j] = 'X'
                if board[i][j] == 'N': board[i][j] = 'O'