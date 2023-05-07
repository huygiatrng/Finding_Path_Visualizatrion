import pygame
import random
from settings import *
from pygameUtil import *
from algorithms import dijkstra, astar


def finding_path(algo, title):
    # Set up the game window
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(title)

    # Define the font
    font = pygame.font.SysFont(None, 30)

    # Define the board
    board = [[EMPTY for j in range(BOARD_SIZE[1])] for i in range(BOARD_SIZE[0])]
    board[START_POS[0]][START_POS[1]] = START
    board[TARGET_POS[0]][TARGET_POS[1]] = TARGET

    for i in range(BOARD_SIZE[0]):
        for j in range(BOARD_SIZE[1]):
            if random.random() < OBSTACLE_PROB and (i, j) not in [START_POS, TARGET_POS]:
                board[i][j] = WALL

    path = algo(screen, CELL_SIZE, board, BOARD_SIZE, START_POS, TARGET_POS)
    print(path)
    print("Distance: " + str(len(path)) + " steps")
    draw_back_button(screen, BOARD_SIZE, CELL_SIZE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if BACK_BUTTON_X <= mouse_pos[0] <= BACK_BUTTON_X + BACK_BUTTON_WIDTH and BACK_BUTTON_Y <= mouse_pos[1] <= BACK_BUTTON_Y + BACK_BUTTON_HEIGHT:
                    print("SSSS")
                    return
        pygame.display.update()
