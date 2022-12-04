# GPT-3 prompt string followed by it's output. 
# Line 40 added by me and the final new line was removed from the given input.
"""
On input:
'''5-96,6-99
29-97,80-97
3-87,3-4
12-12,6-12
64-65,24-66
52-54,1-53
86-89,85-88
37-69,38-38
81-96,47-75
1-13,18-44'''

Where each line represents a pair of ranges.

This python script counts in how many such pairs, one member fully contains the other. It also counts the number of pairs that overlap at all.
"""

# count of pairs where one member fully contains the other
contained_pairs = 0

# count of pairs that overlap at all
overlap_pairs = 0

# sample input
# each line is a pair of ranges
pairs = '''5-96,6-99
29-97,80-97
3-87,3-4
12-12,6-12
64-65,24-66
52-54,1-53
86-89,85-88
37-69,38-38
81-96,47-75
1-13,18-44'''

pairs = open("input.txt").read()    # Added by me

# split the input into lines
lines = pairs.split('\n')

# loop over the lines
for line in lines:
  # split each line into the two ranges
  l_range, r_range = line.split(',')

  # split each range into its min and max values
  l_min, l_max = l_range.split('-')
  r_min, r_max = r_range.split('-')

  # cast min/max strings to ints
  l_min = int(l_min)
  l_max = int(l_max)
  r_min = int(r_min)
  r_max = int(r_max)

  # if one range fully contains the other, add one to `contained_pairs`
  if l_min <= r_min and l_max >= r_max:
    contained_pairs += 1
  elif l_min >= r_min and l_max <= r_max:
    contained_pairs += 1

  # if the ranges overlap at all, add one to `overlap_pairs`
  if l_min <= r_max and l_max >= r_min:
    overlap_pairs += 1

print(f'Number of pairs where one member fully contains the other: {contained_pairs}')
print(f'Number of pairs that overlap at all: {overlap_pairs}')