def get_priority(char):
    if ord(char) > 90:
        priority = ord(char) - 96
    else:
        priority = ord(char) - 38
    return priority

def part1(rucksack):
    priority = 0
    items = [item for item in rucksack]
    compart1 = items[:int(len(items)/2)]
    for char in items[int(len(items)/2):]:
        if char in compart1:
            priority += get_priority(char)
            break
    return priority

rucksacks = [line for line in open("input.txt", "r").read().split('\n')[:-1]]

part1Priority = 0
part2Priority = 0
for i in  range(0, len(rucksacks), 3):
    group = rucksacks[i:i+3]
    commonItem = set.intersection(*map(set, group))
    assert len(commonItem) == 1
    part2Priority += get_priority(commonItem.pop())
    for rucksack in group:
        part1Priority += part1(rucksack)

print('Part 1: ', part1Priority)
print('Part 2: ', part2Priority)