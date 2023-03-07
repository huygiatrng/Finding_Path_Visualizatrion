import pygame
import heapq
import random

# Define the obstacle probability
obstacle_prob = 0.3
# Set up the game window
pygame.init()
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dijkstra's Algorithm")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
orange = (255, 165, 0)

# Define the board size and the start and target positions
board_size = (50, 50)
start_pos = (2, 2)
target_pos = (48, 48)

# Define the cell size
cell_size = (width // board_size[0], height // board_size[1])

# Define the cell types
EMPTY = 0
WALL = 1
START = 2
TARGET = 3
PATH = 4
FASTEST_PATH = 5  # Define the FASTEST_PATH color constant
IN_PROGRESS = 6  # Define the IN_PROGRESS color constant

# Define the font
font = pygame.font.SysFont(None, 30)

# Define the board
board = [[EMPTY for j in range(board_size[1])] for i in range(board_size[0])]
board[start_pos[0]][start_pos[1]] = START
board[target_pos[0]][target_pos[1]] = TARGET

for i in range(board_size[0]):
    for j in range(board_size[1]):
        if random.random() < obstacle_prob and (i, j) not in [start_pos, target_pos]:
            board[i][j] = WALL
# Define the neighbors function
def neighbors(pos):
    x, y = pos
    result = []
    if x > 0 and board[x-1][y] != WALL:
        result.append((x-1, y))
    if x < board_size[0]-1 and board[x+1][y] != WALL:
        result.append((x+1, y))
    if y > 0 and board[x][y-1] != WALL:
        result.append((x, y-1))
    if y < board_size[1]-1 and board[x][y+1] != WALL:
        result.append((x, y+1))
    return result


# Define the heuristic function
def heuristic(pos):
    return abs(pos[0] - target_pos[0]) + abs(pos[1] - target_pos[1])

def draw_board():
    # Draw the board
    for i in range(board_size[0]):
        for j in range(board_size[1]):
            if board[i][j] == EMPTY:
                pygame.draw.rect(screen, white, (i * cell_size[0], j * cell_size[1], cell_size[0], cell_size[1]))
            elif board[i][j] == WALL:
                pygame.draw.rect(screen, black, (i * cell_size[0], j * cell_size[1], cell_size[0], cell_size[1]))
            elif board[i][j] == START:
                pygame.draw.rect(screen, green, (i * cell_size[0], j * cell_size[1], cell_size[0], cell_size[1]))
            elif board[i][j] == TARGET:
                pygame.draw.rect(screen, red, (i * cell_size[0], j * cell_size[1], cell_size[0], cell_size[1]))
            elif board[i][j] == PATH:
                pygame.draw.rect(screen, yellow, (i * cell_size[0], j * cell_size[1], cell_size[0], cell_size[1]))
            elif board[i][j] == FASTEST_PATH:
                pygame.draw.rect(screen, blue, (i * cell_size[0], j * cell_size[1], cell_size[0], cell_size[1]))
            else:
                pygame.draw.rect(screen, gray, (i * cell_size[0], j * cell_size[1], cell_size[0], cell_size[1]))

# Define the Dijkstra's algorithm function
def astar():
    # Initialize the distance and visited dictionaries
    dist = {(i, j): float('inf') for j in range(board_size[1]) for i in range(board_size[0])}
    dist[start_pos] = 0
    prev = {}
    visited = {(i, j): False for j in range(board_size[1]) for i in range(board_size[0])}

    # Initialize the priority queue with the start position
    queue = [(heuristic(start_pos), start_pos)]

    while queue:
        # Get the position with the lowest distance
        current_h, current_pos = heapq.heappop(queue)

        # If the position is the target, return the path
        if current_pos == target_pos:
            path = []
            pos = current_pos
            while pos != start_pos:
                path.append(pos)
                pos = prev[pos]
            path.append(start_pos)
            path.reverse()

            # Color the cells in the fastest path
            for pos in path:
                if pos != start_pos and pos != target_pos:
                    board[pos[0]][pos[1]] = FASTEST_PATH

            # Draw the board
            draw_board()
            pygame.display.update()

            return path

        # Mark the position as visited
        visited[current_pos] = True

        # Update the distance and previous position of the neighbors
        for neighbor_pos in neighbors(current_pos):
            # Calculate the tentative distance
            tentative_dist = dist[current_pos] + 1

            # Update the distance and previous position if the tentative distance is lower
            if tentative_dist < dist[neighbor_pos]:
                dist[neighbor_pos] = tentative_dist
                prev[neighbor_pos] = current_pos

                # Add the neighbor to the priority queue with the f-score (distance + heuristic)
                f_score = tentative_dist + heuristic(neighbor_pos)
                heapq.heappush(queue, (f_score, neighbor_pos))

        # Color the cells in the path so far with yellow
        for pos in visited.keys():
            if visited[pos] and board[pos[0]][pos[1]] == EMPTY:
                board[pos[0]][pos[1]] = IN_PROGRESS

        # Color the cells in the path with blue
        for pos in prev.keys():
            if pos != start_pos and pos != target_pos:
                board[pos[0]][pos[1]] = PATH

        # Draw the board
        draw_board()
        pygame.display.update()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    # Target is unreachable
    return []

path = astar()
print(path)
print("Distance: "+str(len(path))+" steps")
# print(target_pos)
# for pos in path:
#     print(f"Coloring cell ({pos[0]}, {pos[1]})")
#     board[pos[0]][pos[1]] = PATH
# Wait for the user to close the window




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()

