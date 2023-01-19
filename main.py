import pygame
import sys
from numpy import zeros
from tkinter import messagebox
from Logic.gridlines import Grid
from Logic.boardupdate import Update
from Logic.gamelogic import Logic
from Logic.aiLogic import AI

pygame.init()

# colors
white = (255, 255, 255)
black = (0, 0, 0)

# variables
gameover = False

# Window Setup
Width = 600
Height = 600
mainWindow = pygame.display.set_mode((Width, Height))
mainWindow.fill(white)
font = pygame.font.Font('data/bgothl.ttf', 50)
text = font.render("Dhruv's Tic Tac Toe", True, black)
text_rect = text.get_rect(center=(Width / 2, Height / 2))
mainWindow.blit(text, text_rect)
pygame.display.update()
pygame.time.wait(1000)

if (messagebox.askyesno("with AI", "Do you want to play with AI?")):
    withAI = True
else:
    withAI = False

while (not gameover):
    # Initialize
    restart = False
    gameBoard = zeros((3, 3), dtype=int)
    grid = Grid()
    logic = Logic()
    aiLogic = AI()
    boardUpdate = Update(mainWindow)

    # player
    playercount = 1
    aiturn = 0

    # Window
    bgImage = pygame.image.load("data/bgimage.jpg")
    bgImage = pygame.transform.scale(bgImage, (Width, Height))
    mainWindow.blit(bgImage, (0, 0))
    pygame.display.set_caption("Tic Tae Toe")

    # Game loop
    while (not restart):
        grid.draw(black, mainWindow)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                if(messagebox.askyesno("Quit", "Are you sure want to quit the game?!")):
                    sys.exit()
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_r):
                    restart = True
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (pygame.mouse.get_pressed()[0]):
                    Position = pygame.mouse.get_pos()
                    if (logic.ifAvailable(Position[0], Position[1], gameBoard)):
                        boardUpdate.playerTurn(Position, playercount, gameBoard)
                        playercount += 1
                    else:
                        messagebox.showwarning("Taken!", "Place is already taken!")
                    winner, result = logic.checkboard(gameBoard, mainWindow)
                    pygame.display.update()
                    if (result):
                        if (winner == 0):
                            messagebox.showinfo("Game Over", "It's a draw!!")
                        else:
                            messagebox.showinfo("Game Over", f"Player {winner} won the game!!")
                        restart = True

                    if (withAI):
                        move = aiLogic.eval(gameBoard, aiturn)
                        boardUpdate.playerTurn(move, playercount, gameBoard)
                        pygame.display.update()
                        aiturn += 1
                        playercount += 1
                        winner, result = logic.checkboard(gameBoard, mainWindow)
                        pygame.display.update()
                        if (result):
                            if (winner == 0):
                                messagebox.showinfo("Game Over", "It's a draw!!")
                            elif (winner == 1):
                                messagebox.showinfo("Game Over", f"Player {winner} won the game!!")
                            else:
                                messagebox.showinfo("Game Over", f"AI won the game!!")
                            restart = True

        pygame.display.update()

        # exit control
        if (restart):
            break

pygame.quit()
