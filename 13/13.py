import json
from functools import cmp_to_key

def compare_values(val1, val2):
    if isinstance(val1, list) and isinstance(val2, list):
        i = 0
        while i < len(val1) and i < len(val2):
            comparison = compare_values(val1[i], val2[i])
            if comparison == -1:
                return comparison
            elif comparison == 1:
                return comparison
            i += 1
        if i == len(val1) and i < len(val2):
            return -1
        if i < len(val1) and i == len(val2):
            return 1
    elif isinstance(val1, list) and not isinstance(val2, list):
        return compare_values(val1, [val2])
    elif not isinstance(val1, list) and isinstance(val2, list):
        return compare_values([val1], val2)
    else:
        if val1 < val2:
            return -1
        elif val1 == val2:
            return 0
        else:
            return 1
    return 0

pairs = [
    [
        json.loads(packet)
        for packet in pair.split('\n')
    ]
    for pair in open('input.txt').read().split('\n\n')
]


sum_pairs = 0
i = 1
for pair in pairs:
    if compare_values(pair[0], pair[1]) == -1:
        sum_pairs += i
        print(i)
    i += 1

print(sum_pairs)
packets = [
    [[2]],
    [[6]]
]
for pair in pairs:
    packets.append(pair[0])
    packets.append(pair[1])
sorted_packets = sorted(packets, key=cmp_to_key(compare_values))
print((sorted_packets.index([[2]])+1) * (sorted_packets.index([[6]])+1))