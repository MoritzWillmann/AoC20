import re
import numpy as np
pattern_ranges = re.compile(r'(\d+\-\d+)\sor\s(\d+\-\d+)')
pattern_tickets = re.compile(r'((?:\d+[,\n]?){20})')

with open('Day16/input.txt', 'r') as f:
    data = f.read()
    ranges = pattern_ranges.findall(data)
    tickets = pattern_tickets.findall(data)

ranges = np.array([[[int(lim) for lim in range_i.split('-')] for range_i in ran] for ran in ranges])
ranges_1 = np.reshape(ranges, (len(ranges)*2, 2)).T

#Part 1
err_rate = 0
i = 1
for ticket in tickets[1:]:
    for val in ticket.strip().split(','):
        if all((ranges_1[0]>int(val)) | (ranges_1[1]<int(val))):
            err_rate += int(val)
            tickets.pop(i)
            i -= 1
            break
    i += 1

print("Part 1: Ticket Scanning Error Rate: {}".format(err_rate))

#Part 2
ranges_2 = np.reshape(ranges, (len(ranges), 4))
tickets = np.array([[int(val) for val in ticket.strip().split(',')] for ticket in tickets])
possible = np.zeros((len(ranges), len(ranges)), dtype=int)
for i, range_i in enumerate(ranges_2):
    for j in range(len(ranges)):
        possible[i,j] = int(all(((range_i[0] <= tickets[:,j]) & (tickets[:,j] <= range_i[1])) | ((range_i[2] <= tickets[:,j]) & (tickets[:,j] <= range_i[3]))))

perm = np.zeros(len(ranges), dtype=int)
rem = 0
for j in range(len(ranges)):
    i = np.argmin(np.ma.masked_where(possible.sum(axis=0)==0, possible.sum(axis=0)))
    k = np.where(possible[:,i]!= 0)[0][0]
    possible[k,:] = 0
    perm[i] = k

print(perm)
perm = np.argsort(perm)
print(perm)
print(tickets[0,perm[:6]].prod())