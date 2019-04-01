class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        def how_many_valid(board):
            valid_x = 0
            valid_y = 0
            for x in list(zip(board)):
                if "".join(x).count('X') == 3:
                    valid_x += 1
                if "".join(x).count('O') == 3:
                    valid_y += 1
            for x in list(zip(*board)):
                if "".join(x).count('X') == 3:
                    valid_x += 1
                if "".join(x).count('O') == 3:
                    valid_y += 1
            i = j = 0
            x = 0
            y = 2
            string = ""
            string_ = ""
            while i < 3:
                string += board[i][j]
                string_ += board[x][y]
                i += 1
                j += 1
                x += 1
                y -= 1
            if string.count('X') == 3:
                valid_x += 1
            if string.count('O') == 3:
                valid_y += 1
            if string_.count('X') == 3:
                valid_x += 1
            if string_.count('O') == 3:
                valid_y += 1
            return valid_x, valid_y
        n_x = 0
        n_y = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == "X":
                    n_x += 1
                if board[i][j] == "O":
                    n_y += 1
        # print(how_many_valid(board))
        v_x, v_y = how_many_valid(board)
        f = True
        if v_x > 0:
            f =  v_y == 0 and (n_x - n_y) == 1
        elif v_y > 0:
            f =  v_x == 0 and (n_x - n_y) == 0
        return True if (n_x - n_y) in (0,1) and f else False