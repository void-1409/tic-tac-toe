import pygame
from numpy import transpose


class Grid:
    def __init__(self):
        self.black = (150, 75, 0)
        self.grid_lines = [((200, 0), (200, 600)),
                           ((400, 0), (400, 600)),
                           ((0, 200), (600, 200)),
                           ((0, 400), (600, 400))]

    def draw(self, color, window):
        for line in self.grid_lines:
            pygame.draw.line(window, color, line[0], line[1], 4)

    def draw_line(self, where, number, window):
        if (where == "row"):
            place = number*200 + 100
            pygame.draw.line(window, self.black, (50, place), (550, place), 10)

        elif (where == "col"):
            place = number*200 + 100
            pygame.draw.line(window, self.black, (place, 50), (place, 550), 10)

        elif (where == "dia"):
            if (number == 0):
                pygame.draw.line(window, self.black, (50, 50), (550, 550), 10)
            else:
                pygame.draw.line(window, self.black, (550, 50), (50, 550), 10)
