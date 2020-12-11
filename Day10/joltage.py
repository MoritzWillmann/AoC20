from itertools import groupby
import numpy as np

with open('Day10/testinput.txt', 'r') as f:
    data = [0] + sorted(map(int, f.readlines()))

#Part 1
diffs = list(np.diff(data)) +[3]
print("Part 1: {} ones times {} threes equals {}".format(diffs.count(1), diffs.count(3), diffs.count(1)*diffs.count(3)))

#Part 2
paths = [1] + [0] * (len(data) - 1)
for i, adapter in enumerate(data):
    for j in range(i - 3, i):
        if(0 <= adapter - data[j] <= 3):
            paths[i] += paths[j]

print("Part 2: There are {} different ways to legally connect the adapters".format(paths[-1]))
