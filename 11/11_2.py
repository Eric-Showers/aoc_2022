# Optimized with help from my friend: 
# https://github.com/Venats/AdventOfCode2022/blob/master/day11/src/day11.cpp

class Monkey:
  def __init__(self):
    # Numbers represent worry level for items, will be refered to as "items"
    self.item_worries = []  
    self.operation_string = ''
    self.divisor = None
    self.throw_to = []
    self.inspection_count = 0
    self.lcm = 1

  def inspect(self):
    # Get item to inspect
    item = self.item_worries[0]
    # Perform worry update operations
    newWorry = eval(self.operation_string.replace('old', str(item))) % lcm
    # Update item worry
    self.item_worries[0] = newWorry
    self.inspection_count += 1

  def test(self):
    # Get item to throw
    item = self.item_worries.pop(0)
    # Return number of monkey to throw to and item worry number
    return self.throw_to[item % self.divisor == 0], item

file_data = open('input.txt').read().splitlines()
monkey_info_list = [
    file_data[i:i+6]
    for i in range(0, len(file_data), 7)
]

# Create list of monkey objects
monkeys = []
for monkey_info in monkey_info_list:
    monkey = Monkey()
    monkey.item_worries = [
        int(worry) 
        for worry in monkey_info[1].split(':')[1].split(',')
    ]
    monkey.operation_string = monkey_info[2].split('= ')[1]
    monkey.divisor = int(monkey_info[3].split('by ')[1])
    # Store as [false, true] so that index matches comparison boolean result
    monkey.throw_to = [
        int(monkey_info[5].split('monkey ')[1]),
        int(monkey_info[4].split('monkey ')[1])
    ]
    monkeys.append(monkey)

lcm = 1
for monkey in monkeys:
    lcm *= monkey.divisor
for monkey in monkeys:
    monkey.lcm = lcm

# Simulate monkeys
for i in range(10000):
    for monkey in monkeys:
        while len(monkey.item_worries) > 0:  
            # Inspect item
            monkey.inspect()
            # Test item
            throw_to, item_worry = monkey.test()
            # Throw item to other monkey. Item removed from monkey during test
            monkeys[throw_to].item_worries.append(item_worry)
    
inspection_counts = [monkey.inspection_count for monkey in monkeys]
inspection_counts.sort()
print(inspection_counts[-1]*inspection_counts[-2])