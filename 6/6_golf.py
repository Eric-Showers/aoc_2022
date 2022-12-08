filedata = open('input.txt', 'r').read()
print([min([i+length for i in range(len(filedata)-length) if len(set([char for char in filedata[i:i+length]])) == length]) for length in [4, 14]])