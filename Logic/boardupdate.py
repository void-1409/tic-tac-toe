from numpy import transpose
from pygame import image, transform


class Update:
    def __init__(self, window):
        self.window = window
        self.xPosition = self.yPosition = [25, 225, 425]
        self.oimage = image.load("data/oimage.png")
        self.oimage = transform.scale(self.oimage, (150, 150))
        self.ximage = image.load("data/ximage.png")
        self.ximage = transform.scale(self.ximage, (150, 150))

    def displayBoard(self, board):
        board = transpose(board)
        print(board)

    def addx(self, x, y):
        self.window.blit(self.ximage, (self.xPosition[x], self.yPosition[y]))

    def addo(self, x, y):
        self.window.blit(self.oimage, (self.xPosition[x], self.yPosition[y]))

    def playerTurn(self, position, player, board):
        if (position[0] > 2 and position[1] > 2):
            x = position[0] // 200
            y = position[1] // 200
        else:
            x = position[0]
            y = position[1]
        player %= 2
        if (player == 1):
            board[x][y] = 1
            self.addx(x, y)
        elif (player == 0):
            board[x][y] = 2
            self.addo(x, y)
