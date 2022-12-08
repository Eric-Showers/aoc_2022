treemap = []   # Using matrix indices ie. [row][column]
with open('input.txt', 'r') as file:
    for row in file.read().splitlines():
        treemap.append([int(char) for char in row])

height = len(treemap)
width = len(treemap[0])

numvisible = 0
highestscore = 0
# Loop through rows and columns. Count visible trees
for i in range(height):
    for j in range(width):
        # Check how many trees are visible from this tree
        visibleoutside = False  # If the tree can see the outside, it is visible
        visibleUp = 0
        for iterUp in range(i-1, -1, -1):
            visibleUp += 1
            if treemap[iterUp][j] >= treemap[i][j]:
                break
        else:
            visibleoutside = True
        visibleDown = 0
        for iterDown in range(i+1, height):
            visibleDown += 1
            if treemap[iterDown][j] >= treemap[i][j]:
                break
        else:
            visibleoutside = True
        visibleLeft = 0
        for iterLeft in range(j-1, -1, -1):
            visibleLeft += 1
            if treemap[i][iterLeft] >= treemap[i][j]:
                break
        else:
            visibleoutside = True
        visibleRight = 0
        for iterRight in range(j+1, width):
            visibleRight += 1
            if treemap[i][iterRight] >= treemap[i][j]:
                break
        else:
            visibleoutside = True
        # Calculate the score for this tree
        score = visibleUp * visibleDown * visibleLeft * visibleRight
        if score > highestscore:
            highestscore = score
        if visibleoutside:
            numvisible += 1

print(numvisible)
print(highestscore)
