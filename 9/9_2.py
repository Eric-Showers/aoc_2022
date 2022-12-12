# Given position of knot1 and knot2, 
# return the position of knot2 after movement
def moveKnot2(knot1, knot2):
    # Take difference between knot1 and knot2
    deltax = knot1[0] - knot2[0]
    deltay = knot1[1] - knot2[1]
    newX = knot2[0]
    newY = knot2[1]
    # If they are not touching horizontally
    if abs(deltax) > 1:
        newX = knot2[0] + (deltax // abs(deltax))
        # If they are not in the same row
        if abs(deltay) > 0:
            newY = knot2[1] + (deltay // abs(deltay))
    # If they are not touching vertically
    elif abs(deltay) > 1:
        newY = knot2[1] + (deltay // abs(deltay))
        # If they are not in the same column
        if abs(deltax) > 0:
            newX = knot2[0] + (deltax // abs(deltax))
    return (newX, newY)


# Move head one space in the given direction
def moveHead(head, direction):
    if direction == 'U':
        return (head[0], head[1] + 1)
    elif direction == 'R':
        return (head[0] + 1, head[1])
    elif direction == 'D':
        return (head[0],  head[1] - 1)
    elif direction == 'L':
        return (head[0] - 1, head[1])


# Used to draw state. Scales to local of rope.
def printMap(rope):
    maxRow = max([row[1] for row in rope])
    minRow = min([row[1] for row in rope])
    maxCol = max([row[0] for row in rope])
    minCol = min([row[0] for row in rope])
    for row in range(maxRow+5, minRow-5, -1):
        for col in range(minCol-5, maxCol+5):
            try:
                knotNum = rope.index((col, row))
                if knotNum == 0:
                    print('H', end='')
                else:
                    print(knotNum, end='')
            except ValueError:
                # No knot at this position
                print('.', end='')
        print()
    print()


movements = [
    [
        row[0],
        int(row[1:])
    ]
    for row in open('input.txt', 'r').read().splitlines()
]

rope = [(0,0) for _ in range(10)]
distintTailPositions = [rope[-1]]
for direction, distance in movements:
    for distance in range(distance):
        # Move the head
        rope[0] = moveHead(rope[0], direction)
        # Move each knot
        for knotNum in range(1, 10):
            rope[knotNum] = moveKnot2(rope[knotNum-1], rope[knotNum])
        # Track distinct tail positions
        if rope[-1] not in distintTailPositions:
            distintTailPositions.append(rope[-1])

print(len(distintTailPositions))