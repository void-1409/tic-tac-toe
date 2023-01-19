from numpy import transpose, min, max, all
from Logic.gridlines import Grid

grid = Grid()


class Logic:
    def __init__(self):
        self.Result = False
        self.Winner = 0
        self.rowNumber = 0
        self.colNumber = 0
        self.diaNumber = 0

    def ifAvailable(self, x, y, board):
        x //= 200
        y //= 200
        if (board[x][y] == 0):
            return True

    def checkboard(self, board, window):
        self.rowNumber = 0
        self.colNumber = 0
        board = transpose(board)
        for row in board:
            if ((min(row) == max(row) != 0)):
                self.Winner = row[0]
                self.Result = True
                grid.draw_line("row", self.rowNumber, window)
                return(self.Winner, self.Result)
            self.rowNumber += 1

        for column in transpose(board):
            if ((min(column) == max(column) != 0)):
                self.Winner = column[0]
                self.Result = True
                grid.draw_line("col", self.colNumber, window)
                return(self.Winner, self.Result)
            self.colNumber += 1

        if ((board[0][0] == board[1][1] == board[2][2] != 0)):
            self.Winner = board[0][0]
            self.Result = True
            grid.draw_line("dia", 0, window)
            return(self.Winner, self.Result)
        elif ((board[0][2] == board[1][1] == board[2][0] != 0)):
            self.Winner = board[0][2]
            self.Result = True
            grid.draw_line("dia", 1, window)
            return(self.Winner, self.Result)
        if (board.all() > 0):
            self.Result = True
        return (self.Winner, self.Result)
