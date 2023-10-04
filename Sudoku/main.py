import pygame as pg
from SudokuSolver import SudokuSolver
from N2L import *
from SudokuGenerator import SudokuGenerator
pg.init()

b = SudokuGenerator()
a = SudokuSolver(b.get_board())
board = a.get_board()

X, Y = 450, 500
BLACK = (0,0,0)
LIGHT_GRAY = (200,200,200)
SCREEN = pg.display.set_mode((X, Y))
SCREEN.fill((255,255,255))
numbers = { str(i): (pg.transform.scale(pg.image.load("number_images/" + to_verb(str(i)) + ".png"), (50,50))) for i in range(0,10)}

smallfont = pg.font.SysFont("Corbel", 35)
solve_text = smallfont.render("Solve", True, BLACK)
blank_text = smallfont.render("Blank", True, BLACK)
new_text = smallfont.render("New", True, BLACK)

def draw_board():
    for i in range(0,9):
        for j in range(0,9):
            
            SCREEN.blit(numbers[str(board[i][j])], (j*50, i*50))
    pg.display.flip()

def draw_grid():
    for i in range(0,4):
        pg.draw.line(surface=SCREEN, color=(100,100,100), start_pos=(0,i*150), end_pos=(X, i*150), width=3)
        pg.draw.line(surface=SCREEN, color=(100,100,100), start_pos=(i*150,0), end_pos=(i*150, Y-50), width=3)
    
    for i in range(0,9):
        pg.draw.line(surface=SCREEN, color=(200,200,200), start_pos=(0,i*50), end_pos=(X, i*50), width=1)
        pg.draw.line(surface=SCREEN, color=(200,200,200), start_pos=(i*50,0), end_pos=(i*50, Y-50), width=1)

    pg.display.update()


status = True
draw_original = False
while status:
    fpsClock = pg.time.Clock()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            status = False
        
        if event.type == pg.MOUSEBUTTONDOWN:
            if 0 <= mouse[0] <= 80 and 450 <= mouse[1] <= 500:
                a.solve()
                SCREEN.fill((255,255,255))
                draw_board()
                draw_grid()

            elif 85 <= mouse[0] <= 165 and 450 <= mouse[1] <= 500:
                b = [[0 for i in range(0,9)] for j in range(0,9)]
                a = SudokuSolver(b)
                board = a.get_board()
                SCREEN.fill((255,255,255))
                draw_board()
                draw_grid()
            elif 170 <= mouse[0] <= 250 and 450 <= mouse[1] <= 500:
                b = SudokuGenerator()
                a = SudokuSolver(b.get_board())
                board = a.get_board()
                SCREEN.fill((255,255,255))
                draw_board()
                draw_grid()

    if not draw_original:
        draw_board()
        draw_grid()
        draw_original = True
    
    mouse = pg.mouse.get_pos()
    pg.draw.rect(SCREEN, LIGHT_GRAY, [0,450,80,50])
    SCREEN.blit(solve_text, (0, 460))
    pg.draw.rect(SCREEN, LIGHT_GRAY, [85,450,80,50])
    SCREEN.blit(blank_text, (85, 460))
    pg.draw.rect(SCREEN, LIGHT_GRAY, [170,450,80,50])
    SCREEN.blit(new_text, (170, 460))
    pg.display.update()

pg.quit()
