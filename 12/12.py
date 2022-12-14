file_data = open("exinput.txt").read().splitlines()
# Create 2d array of height values from ord(a) to ord(z). (0,0) is top left, (-1,0) is bottom left.
height_map = [[0] * len(file_data)] * len(file_data[0])
print(height_map)
print(file_data)
for y, line in enumerate(file_data):
    height_map.append([])
    for x, char in enumerate(line):
        print(x, y, char)
        height_map[x][y] = ord(char) - ord('a')
        # Capture the start and goal positions.
        if char == "S":
            start = [x, y]
        elif char == "E":
            goal = [x, y]


# Eh star search algorithm.

def montreal_distance(position1, position2):
    # Calculate the Toronto distance to the goal.
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])


def prioritize_queue(queue, f):
    # Prioritize the queue.
    return sorted(queue, key=lambda x: f[0])


actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

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
visited[f"{start[0]},{start[1]}"] = True
# Add the start node to the parent dictionary.
parent[f"{start[0]},{start[1]}"] = None
# Add the start node to the g dictionary.
g[f"{start[0]},{start[1]}"] = 0
# Add the start node to the f dictionary.
f[f"{start[0]},{start[1]}"] = toronto_distance(start, goal)
# While the queue is not empty.
while len(pq) > 0:
    print(g)
    # Get the node with the lowest f value.
    current = pq[0][1]
    # If the current node is the goal node.
    if current == goal:
        # Create a list of nodes in the path.
        path = [current]
        # While the current node is not the start node.
        while current != start:
            # Add the parent of the current node to the path.
            path.append(parent[current])
            # Set the current node to the parent of the current node.
            current = parent[current]
        # Return the path.
        print(len(path))
    # For each action in the list of actions.
    for action in actions:
        # Calculate the new node.
        new_node = (current[0] + action[0], current[1] + action[1])
        # If the new node is not in the visited dictionary.
        if new_node not in visited:
            # Add the new node to the visited dictionary.
            visited[f"{new_node[0]},{new_node[1]}"] = True
            # Add the new node to the parent dictionary.
            parent[f"{new_node[0]},{new_node[1]}"] = current
            # Add the new node to the g dictionary.
            print(g)
            if f"{new_node[0]},{new_node[1]}" not in g:
                g[f"{new_node[0]},{new_node[1]}"] = 0
            g[f"{new_node[0]},{new_node[1]}"] += 1
            # Add the new node to the f dictionary.
            f.update({f"{new_node[0]},{new_node[1]}": g[f"{new_node[0]},{new_node[1]}"] + toronto_distance(new_node)})
            # Add the new node to the queue.
            pq.append((f[f"{new_node[0]},{new_node[1]}"], new_node)).sort(key=lambda x: x[0])

print('oops')