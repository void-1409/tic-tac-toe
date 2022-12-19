from random import randrange
from copy import deepcopy
from numpy import transpose


class AI:
    def __init__(self, level=0, player=2):
        self.player = player
        self.level = level

    def final_state(self, board):
        for row in board:
            if (min(row) == max(row) != 0):
                return row[0]

        for col in transpose(board):
            if (min(col) == max(col) != 0):
                return col[0]

        if (board[0][0] == board[1][1] == board[2][2] != 0):
            return board[1][1]

        elif(board[0][2] == board[1][1] == board[2][0]):
            return board[1][1]

        elif(board.all() > 0):
            return 3

        else:
            return 0

    def get_emptysqrs(self, board):
        emptySqurs = []
        for i in range(3):
            for j in range(3):
                if (board[i][j] == 0):
                    emptySqurs.append((i, j))

        return emptySqurs

    def mark_sqr(self, board, row, column, player):
        board[row][column] = player

    def rndm(self, board):
        emptySqurs = self.get_emptysqrs(board)
        idx = randrange(0, len(emptySqurs))

        return emptySqurs[idx]

    def minmax(self, board, maximizing):
        case = self.final_state(board)

        if (case == 1):
            return 1, None

        elif (case == 2):
            return -1, None

        elif (case == 3):
            return 0, None

        if (maximizing):
            max_eval = -100
            best_move = None
            emptySqurs = self.get_emptysqrs(board)

            for (row, col) in emptySqurs:
                temp_board = deepcopy(board)
                self.mark_sqr(temp_board, row, col, player=1)
                eval = self.minmax(temp_board, False)[0]
                if (eval > max_eval):
                    max_eval = eval
                    best_move = (row, col)
            return max_eval, best_move

        elif (not maximizing):
            min_eval = 100
            best_move = None
            emptySqurs = self.get_emptysqrs(board)

            for (row, col) in emptySqurs:
                temp_board = deepcopy(board)
                self.mark_sqr(temp_board, row, col, player=2)
                eval = self.minmax(temp_board, True)[0]
                if (eval < min_eval):
                    min_eval = eval
                    best_move = (row, col)
            return min_eval, best_move

    def eval(self, gameBoard, level):
        test_board = deepcopy(gameBoard)
        self.level = level
        if (self.level) == 0:
            emptySqurs = self.get_emptysqrs(test_board)
            if ((1, 1) in emptySqurs):
                move = (1, 1)
            else:
                move = self.rndm(test_board)

        else:
            eval, move = self.minmax(test_board, False)

        return move
