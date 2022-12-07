import json

filedata = open('input.txt', 'r').read()
#filedata = open('exInput.txt', 'r').read()

# Filesystem starts with root directory
fileSystem = {'/': {}}

curPath = []
curDir = fileSystem
# Loop through each line out terminal output
for line in filedata.splitlines():
    # If the line is a command
    if line[0] == '$':
        cmd = line.split(' ', 2)[1] # Get the command
        # If the command is 'cd'
        if cmd == 'cd':
            # Get the directory name
            arg = line.split(' ', 2)[2]
            if arg != '..':
                curPath.append(arg)
                # Set the current directory to the new directory
                curDir = curDir[curPath[-1]]
            else:
                # Go up a directory
                curPath.pop()
                curDir = fileSystem
                for dir in curPath:
                    curDir = curDir[dir]
        # Command is 'ls'
        else:
            pass
    # Line is not command, it is a member of current directory
    else:
        # If it is a directory
        desc, name = line.split(' ', 1)
        if desc == 'dir':
            # Add it to the current directory
            curDir[name] = {}
        # It is a file
        else:
            # Add it to the current directory
            curDir[name] = int(desc)

# Calculates total size of a directory by recursing through subdirectories
def getSize(curDir):
    size = 0
    for name, item in curDir.items():
        if type(item) == dict:
            size += getSize(item)
        else:
            size += item
    return size

# Recurses through the filesystem for any directory with a size at most max it adds it to the sum
def sumUnderMax(curDir, curSum, maxSize):
    # Loop for all members of current directory
    for name, item in curDir.items():
        # If the member is a directory
        if type(item) == dict:
            curSize = getSize(item)
            # If the size is at most max
            if curSize <= maxSize:
                # Add it to the sum
                curSum += curSize
            # Recurse through the directory
            curSum = sumUnderMax(item, curSum, maxSize)
    return curSum

print(sumUnderMax(fileSystem['/'], 0, 100000))
totalSize = getSize(fileSystem)
freeSpace = 70000000 - totalSize
print('File system size: ', totalSize)
print('Free space: ', freeSpace)

# Recurse through the filesystem and create list of all directory sizes
def getSizes(curDir):
    size = 0
    sizes = []
    for name, item in curDir.items():
        if type(item) == dict:
            size += getSize(item)
            sizes += getSizes(item)
        else:
            size += item
    sizes.append(size)
    return sizes

sizes = [
    size
    for size in getSizes(fileSystem['/'])
    if freeSpace + size >= 30000000
]
print(min(sizes))