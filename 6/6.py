filedata = open('input.txt', 'r').read()

# Loop through each character in the file, and check if the next 4 are unique
# Output the index of the last character of the first unique 4 characters
for i in range(len(filedata)-4):
    chunk = [char for char in filedata[i:i+4]]
    if len(set(chunk)) == 4:
        print(i+4)
        break

# Loop through each character in the file, and check if the next 14 are unique
# Output the index of the last character of the first unique 14 characters
for i in range(len(filedata)-14):
    chunk = [char for char in filedata[i:i+14]]
    if len(set(chunk)) == 14:
        print(i+14)
        break

