# Given position on head and tail after head movement, 
# return the position of the tail after tail movement
def moveTail(head, tail):
    # Tail should never be more than 2 rows or columns away from head
    assert abs(head[0] - tail[0]) < 3
    assert abs(head[1] - tail[1]) < 3
    # If head is covering tail do nothing
    if head == tail:
        nextTail = tail.copy()
    # Check if they are in the same column
    elif head[0] == tail[0]:
        # Check if head is above
        if head[1] > tail[1]:
            nextTail = [tail[0], head[1]-1]
        # Head is below
        else:
            nextTail = [tail[0], head[1]+1]
    # Check if they are in the same row
    elif head[1] == tail[1]:
        # Check if head is to the right
        if head[0] > tail[0]:
            nextTail = [head[0]-1, tail[1]]
        # Head is below
        else:
            nextTail = [head[0]+1, tail[1]]
    # They are diagonal
    else:
        # If head is diagonally touching, don't move tail
        if abs(head[1]-tail[1]) == abs(head[0]-tail[0]):
            nextTail = tail.copy()
        # If head is further away left/right then it is up/down
        elif abs(head[0]-tail[0]) > abs(head[1]-tail[1]):
            nextTail = moveTail(head, [tail[0], head[1]])
        # Head is further away up/down then it is left/right
        else:
            nextTail = moveTail(head, [head[0], tail[1]])
    return nextTail

# Move head one space in the given direction
def moveHead(head, direction):
    if direction == 'U':
        head[1] += 1
    elif direction == 'R':
        head[0] += 1
    elif direction == 'D':
        head[1] -= 1
    elif direction == 'L':
        head[0] -= 1
    return head

def printMap(head, tail):
    for row in range(4, -1, -1):
        for col in range(6):
            if [col, row] == head:
                print('H', end='')
            elif [col, row] == tail:
                print('T', end='')
            elif [col, row] == [0,0]:
                print('s', end='')
            else:
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

# Handle the first movement
curHead = [0,0]
curTail = [0,0]
distintTailPositions = [curTail]
for direction, distance in movements:
    for distance in range(distance):
        curHead = moveHead(curHead, direction)
        curTail = moveTail(curHead, curTail)
        if curTail not in distintTailPositions:
            distintTailPositions.append(curTail)

print(len(distintTailPositions))