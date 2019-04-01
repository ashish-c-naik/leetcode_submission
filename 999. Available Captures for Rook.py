class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        def goTillEnd(row, col, direction):
            while 0<= row <= len(board) -1 and 0<= col <= len(board[0]) - 1:
                if board[row][col] == 'p':
                    return 1
                elif board[row][col] == 'B':
                    return 0
                else:
                    if direction == '1':
                        row -= 1
                    elif direction == '2':
                        col += 1
                    elif direction == '3':
                        row += 1
                    else:
                        col -= 1
            return 0
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'R':
                    total = 0
                    total += goTillEnd(row, col, '1')
                    total += goTillEnd(row, col, '2')
                    total += goTillEnd(row, col, '3')
                    total += goTillEnd(row, col, '4')
                    return total
