filedata = open('input.txt', 'r').read()
stackStrings, instructions = filedata.split('\n\n')
stackStrings = stackStrings.splitlines()[:-1]   # Split rows, remove numbered row

# Stack indices are 0-8 but instructions will be given for 1-9
stacks1 = [[],[],[],[],[],[],[],[],[]]

# Loop through each row and stack crates in the correct stack
for rowNum in range(len(stackStrings), 0, -1):
    row = stackStrings[rowNum-1]
    for i in range(0, len(row)-3, 4):
        if row[i:i+3] != '   ':
            stacks1[i//4].append(row[i:i+3])
    else:
        if row[-3:] != '   ':
            stacks1[i//4+1].append(row[-3:])

# Part 2 has the same input as part 1
stacks2 = [
    [crate for crate in stack]
    for stack in stacks1
]

# Loop through each instruction and move the crates
for instruction in instructions.splitlines():
    moveAmount, fromStack, toStack = instruction.split()[1::2]
    stacks2[int(toStack)-1] += stacks2[int(fromStack)-1][-int(moveAmount):]
    stacks2[int(fromStack)-1] = stacks2[int(fromStack)-1][:-int(moveAmount)]
    for i in range(int(moveAmount)):
        toMove = stacks1[int(fromStack)-1].pop()
        stacks1[int(toStack)-1].append(toMove)

# Print part 1 solution
for stack in stacks1:
    print(stack[-1].strip('[]'), end='')
else:
    print()

# Print part 2 solution
for stack in stacks2:
    print(stack[-1].strip('[]'), end='')
else:
    print()