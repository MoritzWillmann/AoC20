from math import cos, sin, pi
import re
import numpy as np

pattern = re.compile(r'([NSEWLRF])(\d+)')

position = np.array([0.0, 0.0])
angle = 0

def direction(phi):
    return np.array([round(cos(phi/180*pi), 2), round(sin(phi/180*pi), 2)])

with open('Day12/testinput.txt', 'r') as file:
    data = pattern.findall(file.read())
#Part 1
for (instruction, value) in data:
    if instruction == 'N':
        position[1] += float(value)
    elif instruction == 'S':
        position[1] -= float(value)
    elif instruction == 'E':
        position[0] += float(value)
    elif instruction == 'W':
        position[0] -= float(value)
    elif instruction == 'L':
        angle += float(value)
    elif instruction == 'R':
        angle -= float(value)
    elif instruction == 'F':
        position += float(value) * direction(angle)
print("Part 1: The Manhattan distance of the starting point and the current position {} is {}".format(position,np.linalg.norm(position, ord=1)))

#Part 2
def rotation(phi):
    return np.array([[round(cos(phi/180*pi), 2), -round(sin(phi/180*pi), 2)], [round(sin(phi/180*pi), 2), round(cos(phi/180*pi), 2)]])

position = np.array([0.0, 0.0]).T
waypoint = np.array([10.0, 1.0]).T
for (instruction, value) in data:
    if instruction == 'N':
        waypoint[1] += float(value)
    elif instruction == 'S':
        waypoint[1] -= float(value)
    elif instruction == 'E':
        waypoint[0] += float(value)
    elif instruction == 'W':
        waypoint[0] -= float(value)
    elif instruction == 'L':
        waypoint = rotation(float(value)).dot(waypoint.T)
    elif instruction == 'R':
        waypoint = rotation(-float(value)).dot(waypoint.T)
    elif instruction == 'F':
        position += float(value) * waypoint
print("Part 2: The Manhattan distance of the starting point and the current position {} is {}".format(position,np.linalg.norm(position, ord=1)))