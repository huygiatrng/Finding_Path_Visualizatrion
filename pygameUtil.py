# pygameUtil.py
import pygame
from settings import *


def neighbors(pos, board, board_size, WALL):
    x, y = pos
    result = []
    if x > 0 and board[x - 1][y] != WALL:
        result.append((x - 1, y))
    if x < board_size[0] - 1 and board[x + 1][y] != WALL:
        result.append((x + 1, y))
    if y > 0 and board[x][y - 1] != WALL:
        result.append((x, y - 1))
    if y < board_size[1] - 1 and board[x][y + 1] != WALL:
        result.append((x, y + 1))
    return result


def draw_board(screen, board, board_size, cell_size):
    # Draw the board
    for i in range(board_size[0]):
        for j in range(board_size[1]):
            if board[i][j] == EMPTY:
                pygame.draw.rect(screen, Color.white, (i * cell_size[0], j * cell_size[1], cell_size[0], cell_size[1]))
            elif board[i][j] == WALL:
                pygame.draw.rect(screen, Color.black, (i * cell_size[0], j * cell_size[1], cell_size[0], cell_size[1]))
            elif board[i][j] == START:
                pygame.draw.rect(screen, Color.green, (i * cell_size[0], j * cell_size[1], cell_size[0], cell_size[1]))
            elif board[i][j] == TARGET:
                pygame.draw.rect(screen, Color.red, (i * cell_size[0], j * cell_size[1], cell_size[0], cell_size[1]))
            elif board[i][j] == PATH:
                pygame.draw.rect(screen, Color.yellow, (i * cell_size[0], j * cell_size[1], cell_size[0], cell_size[1]))
            elif board[i][j] == FASTEST_PATH:
                pygame.draw.rect(screen, Color.blue, (i * cell_size[0], j * cell_size[1], cell_size[0], cell_size[1]))
            else:
                pygame.draw.rect(screen, Color.gray, (i * cell_size[0], j * cell_size[1], cell_size[0], cell_size[1]))


def draw_back_button(screen, board_size, cell_size):
    back_button_x = 10
    back_button_y = board_size[1] * cell_size[1] - 40
    back_button_width, back_button_height = 100, 30
    pygame.draw.rect(screen, Color.gray, (back_button_x, back_button_y, back_button_width, back_button_height))
    button_font = pygame.font.SysFont(None, 20)
    button_text = button_font.render("Back to Menu", True, Color.white)
    screen.blit(button_text, (back_button_x + back_button_width // 2 - button_text.get_width() // 2,
                              back_button_y + back_button_height // 2 - button_text.get_height() // 2))

    return back_button_x, back_button_y, back_button_width, back_button_height
