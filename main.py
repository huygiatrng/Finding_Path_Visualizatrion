# main.py
import pygame
from settings import *
from find_path import finding_path
from algorithms import astar, dijkstra

# Initialize pygame
pygame.init()

# Window settings
width, height = WIDTH, HEIGHT
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pathfinding Algorithms")

# Button settings
button_width, button_height = 200, 50
button_font = pygame.font.SysFont(None, 24)


def draw_button(screen, text, x, y, width, height, color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    button_text = button_font.render(text, True, Color.white)
    screen.blit(button_text,
                (x + width // 2 - button_text.get_width() // 2, y + height // 2 - button_text.get_height() // 2))


def main_menu():
    running = True
    while running:
        screen.fill(Color.gray)

        draw_button(screen, "A* Algorithm", width // 2 - button_width // 2, height // 2 - button_height * 3 // 2,
                    button_width, button_height, Color.blue)
        draw_button(screen, "Dijkstra's Algorithm", width // 2 - button_width // 2, height // 2 + button_height // 2,
                    button_width, button_height, Color.green)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                x, y = width // 2 - button_width // 2, height // 2 - button_height * 3 // 2
                if x <= mouse_pos[0] <= x + button_width and y <= mouse_pos[1] <= y + button_height:
                    finding_path(astar, "A* Algorithm")
                x, y = width // 2 - button_width // 2, height // 2 + button_height // 2
                if x <= mouse_pos[0] <= x + button_width and y <= mouse_pos[1] <= y + button_height:
                    finding_path(dijkstra, "Dijkstra Algorithm")

main_menu()
