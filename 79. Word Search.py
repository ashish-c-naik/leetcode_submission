class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word == '': return True
        def adjacent(x,y,char):
            ans = []
            for i in (-1,1):
                if 0<= x+i < len(board) and board[x+i][y] == char:
                    ans.append((x+i,y))
            for i in (-1,1):
                if 0<= y+i < len(board[0]) and board[x][y+i] == char:
                    ans.append((x,y+i))
            return ans
        def search(x,y,seen, index):
            if (x,y) in seen and seen[(x,y)]:
                return False
            if index > len(word) - 1:
                return True
            seen[(x,y)] = True
            f = False
            for value in adjacent(x,y,word[index]):
                f = f or search(value[0], value[1],seen, index + 1)
            if f: return f
            seen[(x,y)] = False
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if search(i,j,{}, 1):
                        return True
        return False
        