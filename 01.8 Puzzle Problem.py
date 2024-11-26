import heapq

def manhattan_distance(state, goal):
    """Calculate Manhattan distance for the current state."""
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x, goal_y = [(x, y) for x in range(3) for y in range(3) if goal[x][y] == value][0]
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance

def get_neighbors(state):
    """Generate all possible neighbors by sliding the blank."""
    neighbors = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
                break
    moves = [("UP", (x - 1, y)), ("DOWN", (x + 1, y)), 
             ("LEFT", (x, y - 1)), ("RIGHT", (x, y + 1))]
    for action, (new_x, new_y) in moves:
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append((tuple(tuple(row) for row in new_state), action))
    return neighbors

def a_star(initial, goal):
    """Solve the 8-puzzle using A* search with Manhattan distance."""
    open_set = []
    heapq.heappush(open_set, (0, initial, []))  # (cost, state, path)
    visited = set()
    visited.add(initial)

    while open_set:
        cost, current, path = heapq.heappop(open_set)

        if current == goal:
            return path

        for neighbor, action in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                g = len(path) + 1  # Actual cost
                h = manhattan_distance(neighbor, goal)  # Heuristic
                heapq.heappush(open_set, (g + h, neighbor, path + [action]))
    return None

# Example usage
initial_state = (
    (1, 5, 3),
    (0, 4, 2),
    (7, 8, 6)
)

goal_state = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

solution = a_star(initial_state, goal_state)
if solution:
    print("Solution steps:", solution)
else:
    print("No solution found.")
