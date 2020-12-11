from itertools import combinations

with open('Day9/input.txt', 'r') as f:
    data = [int(line) for line in f.readlines()]
## PART 1
for i in range(len(data)-25):
    if data[i+25] not in [sum(i) for i in list(combinations(data[i:i+25], 2))]:
        print("Part 1: {}:{} is not any of the sums of its predecessing 25 numbers {}".format(i+25, data[i+25], data[i:i+25]))
        break
## PART 2
ranges = list(combinations(list(range(i)), 2))
for range in ranges:
    if sum(data[range[0]:range[1]]) == data[i+25]:
        print("Part 2: the range {} to {} contains the numbers {} that sum up to {}, the sum of their min and max is {}".format(range[0], range[1], data[range[0]:range[1]], data[i+25], min(data[range[0]:range[1]])+max(data[range[0]:range[1]])))
        break