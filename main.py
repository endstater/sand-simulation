import pygame as pg
from random import randint
from time import sleep

def draw_pixel(x,y,c):
    pg.draw.rect(screen, c,pg.Rect(x*10,y*10,10,10))

def sand_phis(i,j):
    if j < 49:
        if board[i][j+1] == 0:
            board[i][j] = 0
            board[i][j+1] = 1
        elif i > 0 and board[i-1][j+1] == 0:
            board[i][j]=0
            board[i-1][j+1] = 1
        elif i < 50 and board[i+1][j+1] == 0:
            board[i][j]=0
            board[i+1][j+1] = 1
        elif board[i][j+1] == 2 and randint(1,10)<2:
            board[i][j] = 2
            board[i][j+1] = 1
        elif i > 0 and board[i-1][j+1] == 2 and randint(1,10)<2:
            board[i][j]=2
            board[i-1][j+1] = 1
        elif i < 50 and board[i+1][j+1] == 2 and randint(1,10)<2:
            board[i][j]=2
            board[i+1][j+1] = 1
    draw_pixel(i,j,(224,195,45))

def water_phis(i,j):
    if j < 49:
        if board[i][j+1] == 0:
            board[i][j] = 0
            board[i][j+1] = 2
        elif i > 0 and board[i-1][j+1] == 0:
            board[i][j]=0
            board[i-1][j+1] = 2
        elif i < 50 and board[i+1][j+1] == 0:
            board[i][j]=0
            board[i+1][j+1] = 2
        elif i > 0 and board[i-1][j] == 0:
            board[i][j]=0
            board[i-1][j] = 2
        elif i < 50 and board[i+1][j] == 0:
            board[i][j]=0
            board[i+1][j] = 2
    draw_pixel(i,j,(124,135,245))

pg.init()

screen = pg.display.set_mode([500, 500])

running = True
drawing = False
mod = 0

board = [[0]*50]
for i in range(50):
    line = [0]*50
    board.append(line)

while running:    # Did the user click the window close button?
    pos = pg.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            drawing = True
        if event.type == pg.MOUSEBUTTONUP:
            drawing = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_s:
                mod = 1 
            if event.key == pg.K_w:
                mod = 2
            if event.key == pg.K_x:
                mod = 0

    if drawing:
        board[pos[0]//10][pos[1]//10] = mod
        board[pos[0]//10-1][pos[1]//10] = mod
        board[pos[0]//10][pos[1]//10+1] = mod
        board[pos[0]//10+1][pos[1]//10] = mod
        board[pos[0]//10][pos[1]//10-1] = mod

    screen.fill((0,20,40))
    for i in range(49,-1,-1):
        for j in range(49,-1,-1):
            if board[i][j] == 1:
                sand_phis(i,j)
            elif board[i][j] == 2:
                water_phis(i,j)

    pg.display.flip()
    sleep(0.03)
pg.quit()
