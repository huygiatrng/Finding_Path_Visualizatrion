import heapq
import random
from settings import *
import pygame
from pygameUtil import *


def dijkstra(screen, cell_size, board, board_size, start_pos, target_pos):
    # Initialize the distance and visited dictionaries
    dist = {(i, j): float('inf') for j in range(board_size[1]) for i in range(board_size[0])}
    dist[start_pos] = 0
    prev = {}
    visited = {(i, j): False for j in range(board_size[1]) for i in range(board_size[0])}

    # Initialize the priority queue with the start position
    queue = [(0, start_pos)]

    while queue:
        # Get the position with the lowest distance
        current_dist, current_pos = heapq.heappop(queue)

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
            draw_board(screen, board, board_size, cell_size)
            pygame.display.update()

            return path

        # Mark the position as visited
        visited[current_pos] = True

        # Update the distance and previous position of the neighbors
        for neighbor_pos in neighbors(current_pos, board, board_size, WALL):
            # Calculate the tentative distance
            tentative_dist = current_dist + 1

            # Update the distance and previous position if the tentative distance is lower
            if tentative_dist < dist[neighbor_pos]:
                dist[neighbor_pos] = tentative_dist
                prev[neighbor_pos] = current_pos

                # Add the neighbor to the priority queue
                heapq.heappush(queue, (tentative_dist, neighbor_pos))

        # Color the cells in the path so far with yellow
        for pos in visited.keys():
            if visited[pos] and board[pos[0]][pos[1]] == EMPTY:
                board[pos[0]][pos[1]] = IN_PROGRESS

        # Color the cells in the path with blue
        for pos in prev.keys():
            if pos != start_pos and pos != target_pos:
                board[pos[0]][pos[1]] = PATH

        # Draw the board
        draw_board(screen, board, board_size, cell_size)
        pygame.display.update()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    # Target is unreachable
    return []


def astar(screen, cell_size, board, board_size, start_pos, target_pos):
    # Define the heuristic function
    def heuristic(pos):
        return abs(pos[0] - target_pos[0]) + abs(pos[1] - target_pos[1])

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
            draw_board(screen, board, board_size, cell_size)
            pygame.display.update()

            return path

        # Mark the position as visited
        visited[current_pos] = True

        # Update the distance and previous position of the neighbors
        for neighbor_pos in neighbors(current_pos, board, board_size, WALL):
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
        draw_board(screen, board, board_size, cell_size)
        pygame.display.update()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    # Target is unreachable
    return []
