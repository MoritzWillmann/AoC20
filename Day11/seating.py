import numpy as np
with open('Day11/input.txt', 'r') as file:
    grid = np.array([[char for char in line.strip()] for line in file.readlines()])

data = np.copy(grid)
(m, n) = data.shape

## Part 1
maxit = 1000
for it in range(maxit):
    newdata = np.empty((m,n), dtype=str)
    for i in range(m):
        for j in range(n):
            if data[i,j] == '.':
                newdata[i,j] = '.'
            else:
                if '#' not in list(data[max(0,i-1):i+2,max(0,j-1):j+2].ravel()):
                    newdata[i,j] = '#'
                elif list(data[max(0,i-1):i+2,max(0,j-1):j+2].ravel()).count('#')>4:
                    newdata[i,j] = 'L'
                else:
                    newdata[i,j] = data[i,j]
    if list(newdata.ravel()) == list(data.ravel()):
        break
    data = np.copy(newdata)

print("Part 1: {} seats end up occupied after {} iterations".format(list(data.ravel()).count('#'),it))

##Part 2
data = np.copy(grid)
occupancy = data != '.'

def next_chair(i,j,dir, data):
    while True:
        i += dir[0]
        j += dir[1]
        if i <0 or i >= m or j <0 or j >= n:
            return None
        elif occupancy[i,j]:
            return data[i,j]
    return None

for it in range(maxit):
    newdata = np.empty((m,n), dtype=str)
    for i in range(m):
        for j in range(n):
            if not occupancy[i,j]:
                newdata[i,j] = '.'
            else:
                next_chairs = [next_chair(i,j,dir,data) for dir in [(-1,-1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]]
                if '#' not in next_chairs:
                    newdata[i,j] = '#'
                elif next_chairs.count('#')>4:
                    newdata[i,j] = 'L'
                else:
                    newdata[i,j] = data[i,j]
    if list(newdata.ravel()) == list(data.ravel()):
        break
    data = newdata

print("Part 2: {} seats end up occupied after {} iterations".format(list(data.ravel()).count('#'),it))