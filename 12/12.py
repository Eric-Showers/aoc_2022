class Node:
    def __init__(self, position, parent, g, f, height):
        self.position = position
        self.state = f"{position[0]},{position[1]}"
        self.parent = parent
        self.height = height
        self.path_cost = g
        self.f = f


def montreal_distance(position1, position2):
    # Calculate the Toronto distance to the goal.
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])


def solution(node, initial_node):
    # Create a list of nodes in the path.
    path = [node]
    # While the current node is not the start node.
    while node != initial_node:
        # Add the parent of the current node to the path.
        path.append(node.parent)
        # Set the current node to the parent of the current node.
        node = node.parent
    return path


def eh_star_search(height_map, start_pos, goal_pos):
    actions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    # Create a priority queue.
    pq = []
    # Add the start node to the queue.
    start_node = Node(
        start_pos, 
        None, 
        0, 
        montreal_distance(start_pos, goal_pos), 
        height_map[start_pos[0]][start_pos[1]]
    )
    pq.append(start_node)
    # Create dicts of visited nodes, node parents, f, and g values.
    explored = {}
    # While the queue is not empty.
    while len(pq) > 0:
        # Remove first node from pq with the highest f value.
        cur_node = pq.pop(0)
        # If the current node is the goal node.
        if cur_node.position == goal_pos:
            # Return a list of nodes in the path.
            return solution(cur_node, start_node)
        # Check if current node is unexplored, or if this is a better path.
        if cur_node.state not in explored or explored[cur_node.state] > cur_node.path_cost:
            explored[cur_node.state] = cur_node.path_cost
            # For each action in the list of actions.
            for action in actions:
                # Check if the node is in bounds and a legal move from current position
                new_node_pos = [
                    cur_node.position[0] + action[0], 
                    cur_node.position[1] + action[1]
                ]
                if (
                    new_node_pos[0] < 0 
                    or new_node_pos[0] >= len(height_map) 
                    or new_node_pos[1] < 0 
                    or new_node_pos[1] >= len(height_map[0])
                ):
                    continue
                if height_map[new_node_pos[0]][new_node_pos[1]] - cur_node.height > 1:
                    continue
                # Create a new node.
                new_node = Node(
                    new_node_pos, 
                    cur_node, 
                    cur_node.path_cost + 1, 
                    montreal_distance(new_node_pos, goal_pos) + cur_node.path_cost + 1, 
                    height_map[new_node_pos[0]][new_node_pos[1]]
                )
                # Add the new node to the queue.
                pq = sorted(pq+[new_node], key=lambda x: x.f)
    return False


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


# Remove one from path length because start node not counted.
shortest_hike = len(eh_star_search(height_map, start, goal)) - 1
print('Part 1:', shortest_hike)
for y in range(len(height_map[0])):
    for x in range(len(height_map)):
        if height_map[x][y] == 0:
            hike_path = eh_star_search(height_map, [x, y], goal)
            if hike_path:
                if len(hike_path)-1 < shortest_hike:
                    shortest_hike = len(hike_path)-1


print('Part 2: ', shortest_hike)
