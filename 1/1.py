# Read all data from file
data = open("input.txt", "r").read()

# Split data into list of food items caried by each elf
elfInventories = [
    [
        int(cals)
        for cals in elf.split("\n")
        if cals != ""
    ]
    for elf in data.split("\n\n")
]

# Find the top 3 elfs carrying the greatest sums of calories
mostCalories = [0, 0, 0]
for elf in elfInventories:
    if sum(elf) > mostCalories[2]:
        if sum(elf) > mostCalories[1]:
            if sum(elf) > mostCalories[0]:
                mostCalories[2] = mostCalories[1]
                mostCalories[1] = mostCalories[0]
                mostCalories[0] = sum(elf)
            else:
                mostCalories[2] = mostCalories[1]
                mostCalories[1] = sum(elf)
        else:
            mostCalories[2] = sum(elf)

print("The most calories carried by an elf is: ", mostCalories[0])
print("The top three elfs are carrying ", sum(mostCalories), " calories")
