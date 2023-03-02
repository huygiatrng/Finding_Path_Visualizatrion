# Dijkstra Randomized Visualization

This Python program uses the Pygame library to visualize the Dijkstra algorithm, one of the most popular algorithms used in pathfinding and graph traversal.

**Getting Started**

Before running this program, make sure to have Pygame installed. If you don't have Pygame installed, you can install it by running the following command:

<pre>
pip install pygame
</pre>

Once you have Pygame installed, you can run the program by running the following command:

<pre>
python main.py
</pre>

**Program Description**

The program allows you to stimulate the Dijkstra algorithm with randomized obstacles as walls. The client can easily adjust the value of different parameters, such as the resolution, size of the board, obstacle percentage, and positions of the starting and target points.

The program is designed to be highly interactive and user-friendly. The user can change the percentage of obstacle, and can also move the starting and target points around. The program will then use the Dijkstra algorithm to find the shortest path between the two points, while taking the obstacles into account.

**Usage**

To start the program, simply run the **main.py** file. This will open up the Pygame window and show a blank board with the starting and target points marked.

The size of the board that is covered in obstacles can be adjusted by changing the obstacle_prob variable at the top of the main.py file. To change the size of the board, simply adjust the board_size variables.

The user can also change the starting and target points. To change the positions, simply adjust the start_pos and target_pos variables.

The algorithm will then find the shortest path between the two points, while taking the obstacles into account.
