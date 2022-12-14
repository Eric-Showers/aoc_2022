file_data = open("input.txt").read().splitlines()
# Create 2d array of height values from ord(a) to ord(z).
# (0,0) is top left, (-1,0) is bottom left.
height_map = [[0] * len(file_data) for i in range(len(file_data[0]))]
for y, line in enumerate(file_data):
    for x, char in enumerate(line):
        # Capture the start and goal positions.
        if char == 'S':
            start = [x, y]
            height_map[x][y] = 0
        elif char == 'E':
            goal = [x, y]
            height_map[x][y] = ord('z') - ord('a')
        else:
            height_map[x][y] = ord(char) - ord('a')


def print_map(h_map, positions):
    for y in range(len(h_map[0])):
        for x in range(len(h_map)):
            if [x, y] in positions:
                print("#", end="")
            else:
                print(file_data[y][x], end="")
        print()


# Eh star search algorithm.


def montreal_distance(position1, position2):
    # Calculate the Toronto distance to the goal.
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])


def prioritize_queue(queue, f):
    # Prioritize the queue.
    return sorted(queue, key=lambda x: f[0])


actions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# Create a priority queue.
pq = []
# Add the start node to the queue.
pq.append((0, start))
# Create dicts of visited nodes, node parents, f, and g values.
visited = {}
parent = {}
f = {}
g = {}
# Add the start node to the visited dictionary.
visited[f"{start[0]},{start[1]}"] = 0
# Add the start node to the parent dictionary.
parent[f"{start[0]},{start[1]}"] = None
# Add the start node to the g dictionary.
g[f"{start[0]},{start[1]}"] = 0
# Add the start node to the f dictionary.
f[f"{start[0]},{start[1]}"] = montreal_distance(start, goal)
# While the queue is not empty.
while len(pq) > 0:
    # Remove first node from pq with the highest f value.
    current = pq.pop()[1]
    curString = f"{current[0]},{current[1]}"
    # If the current node is the goal node.
    if current == goal:
        # Create a list of nodes in the path.
        path = [current]
        # While the current node is not the start node.
        while current != start:
            # Add the parent of the current node to the path.
            path.append(parent[f"{current[0]},{current[1]}"])
            # Set the current node to the parent of the current node.
            current = parent[f"{current[0]},{current[1]}"]
        # Return the path.
        print(len(path)-1)
        break
    # For each action in the list of actions.
    for action in actions:
        # Calculate the new node.
        new_node = [current[0] + action[0], current[1] + action[1]]
        # Check if the new node is in bounds.
        if new_node[0] < 0 or new_node[0] >= len(height_map) or new_node[1] < 0 or new_node[1] >= len(height_map[0]):
            continue
        # Check if the new node is at most one higher
        if height_map[new_node[0]][new_node[1]] - height_map[current[0]][current[1]] > 1:
            continue
        # If the new node is not in the visited dictionary.
        pos_str = f"{new_node[0]},{new_node[1]}"
        if pos_str not in visited or visited[pos_str] > g[curString]+1:
            # Add the new node to the parent dictionary.
            parent[pos_str] = current
            # Add the new node to the g dictionary.
            if pos_str not in g:
                g[pos_str] = g[curString]
            g[pos_str] += 1
            # Add the new node to the visited dictionary.
            visited[pos_str] = g[pos_str]
            # Add the new node to the f dictionary.
            f.update({pos_str: g[pos_str] + montreal_distance(new_node, goal)})
            # Add the new node to the queue.
            pq.append((f[pos_str], new_node))
            pq.sort(key=lambda x: x[0])
