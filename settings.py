import pygame

OBSTACLE_PROB = 0.3
WIDTH, HEIGHT = 600, 600
BOARD_SIZE = (50, 50)
START_POS = (2, 2)
TARGET_POS = (48, 48)
BACK_BUTTON_X = 10
CELL_SIZE = (WIDTH // BOARD_SIZE[0], HEIGHT // BOARD_SIZE[1])
BACK_BUTTON_Y = BOARD_SIZE[1] * CELL_SIZE[1] - 40
BACK_BUTTON_WIDTH, BACK_BUTTON_HEIGHT = 100, 30


# Define colors
class Color:
    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (200, 200, 200)
    green = (0, 255, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    orange = (255, 165, 0)


EMPTY = 0
WALL = 1
START = 2
TARGET = 3
PATH = 4
FASTEST_PATH = 5  # Define the FASTEST_PATH color constant
IN_PROGRESS = 6  # Define the IN_PROGRESS color constant
