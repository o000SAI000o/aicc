import heapq

# Directions for movement (up, down, left, right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Node:
    def __init__(self, position, g_cost, h_cost, parent=None):
        self.position = position  # Current position in the grid
        self.g_cost = g_cost  # Cost to reach this node from start
        self.h_cost = h_cost  # Heuristic cost (estimated cost to goal)
        self.f_cost = g_cost + h_cost  # Total cost (g + h)
        self.parent = parent  # Parent node to reconstruct the path
        
    def __lt__(self, other):
        return self.f_cost < other.f_cost

# Manhattan distance heuristic
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* algorithm implementation
def a_star(grid, start, goal):
    open_list = []  # Priority queue for open nodes
    closed_list = set()  # Set of visited nodes
    start_node = Node(start, 0, heuristic(start, goal))  # Start node
    heapq.heappush(open_list, start_node)  # Push start node into open list

    while open_list:
        # Pop the node with the lowest f_cost
        current_node = heapq.heappop(open_list)
        current_position = current_node.position

        # If we reached the goal, reconstruct the path
        if current_position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return the reversed path (from start to goal)

        closed_list.add(current_position)  # Mark the node as visited

        # Explore neighbors (up, down, left, right)
        for direction in directions:
            neighbor = (current_position[0] + direction[0], current_position[1] + direction[1])

            # Skip if neighbor is out of bounds or blocked (grid value 1)
            if not (0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0])) or grid[neighbor[0]][neighbor[1]] == 1:
                continue
            
            if neighbor in closed_list:  # Skip if neighbor is already visited
                continue

            # Calculate g_cost, h_cost, and f_cost for the neighbor
            g_cost = current_node.g_cost + 1
            h_cost = heuristic(neighbor, goal)
            neighbor_node = Node(neighbor, g_cost, h_cost, current_node)

            # If neighbor is not in open list or has a lower f_cost, add it to open list
            if not any(node.position == neighbor and node.f_cost <= neighbor_node.f_cost for node in open_list):
                heapq.heappush(open_list, neighbor_node)

    return None  # No path found

# Function to print the grid (for visualizing the grid)
def print_grid(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))

# Example grid (0 = free space, 1 = obstacle)
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)  # Starting position
goal = (4, 4)   # Goal position

# Find the path using A* algorithm
path = a_star(grid, start, goal)

# Print the result
if path:
    print("Path found:", path)
else:
    print("No path found")
