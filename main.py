import pygame
from time import sleep
from numpy import zeros
from tkinter import Tk
from tkinter import messagebox
from gridlines import Grid
from boardupdate import Update
from gamelogic import Logic
from aiLogic import AI

pygame.init()

# colors
white = (255, 255, 255)
black = (0, 0, 0)

# variables
exitgame = False
gameover = False

root = Tk()
root.withdraw()

# Window Setup
Width = 600
Height = 600
mainWindow = pygame.display.set_mode((Width, Height))
mainWindow.fill(white)
font = pygame.font.Font('bgothl.ttf', 50)
text = font.render("Dhruv's Tic Tac Toe", True, black)
text_rect = text.get_rect(center=(Width / 2, Height / 2))
mainWindow.blit(text, text_rect)
pygame.display.update()
sleep(1)

while (not gameover):
    # Initialize
    withAI = False
    gameBoard = zeros((3, 3), dtype=int)
    grid = Grid()
    logic = Logic()
    aiLogic = AI()
    boardUpdate = Update(mainWindow)

    # player
    playercount = 1
    aiturn = 0

    # Window
    bgImage = pygame.image.load("bgimage.jpg")
    bgImage = pygame.transform.scale(bgImage, (Width, Height))
    mainWindow.blit(bgImage, (0, 0))
    pygame.display.set_caption("Tic Tae Toe")

    # Asking for AI
    if(messagebox.askyesno("With AI", "Do you want to play with AI?!")):
        withAI = True

    # Game loop
    while (not exitgame):
        grid.draw(black, mainWindow)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                if(messagebox.askokcancel("Quit", "Are you sure want to quit the game?!")):
                    exitgame = True
                    break
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_r):
                    gameover = True
                    exitgame = True
                    break
            if (event.type == pygame.MOUSEBUTTONDOWN):
                if (pygame.mouse.get_pressed()[0]):
                    Position = pygame.mouse.get_pos()
                    if (logic.ifAvailable(Position[0], Position[1], gameBoard)):
                        boardUpdate.playerTurn(Position, playercount, gameBoard)
                        playercount += 1
                    else:
                        messagebox.showwarning("Taken", "Place already taken!!")
                    winner, result = logic.checkboard(gameBoard, mainWindow)
                    pygame.display.update()
                    if (result):
                        if (winner == 0):
                            messagebox.showinfo("Game Over", "It's a draw!!")
                        else:
                            messagebox.showinfo("Game Over", f"Player {winner} won the game!!")
                        gameover = True
                        exitgame = True
                        break

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
                            gameover = True
                            exitgame = True

        pygame.display.update()

    # exit control
    if (gameover):
        if (messagebox.askokcancel("Restart", "Do you want to restart the game?!")):
            gameover = False
            exitgame = False
        else:
            break

    if (exitgame):
        break

pygame.quit()
