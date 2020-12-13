import numpy as np
import re

pattern = re.compile(r'(\d+)')

with open('Day13/input.txt', 'r') as file:
    [time, bus_lines_str] = file.readlines()
    time = int(time.strip())
    bus_lines = np.array(pattern.findall(bus_lines_str), dtype=int)

#Part 1
waiting_times = bus_lines - (time % bus_lines)
first_id = int(np.where(waiting_times == np.min(waiting_times))[0])
print("Part 1: Bus {} will arrive first at {}, you'll have to wait {} minutes.\n ID x waiting time = {}".format(bus_lines[first_id], time+waiting_times[first_id], waiting_times[first_id], bus_lines[first_id]*waiting_times[first_id]))

#Part 2
offset = np.where(np.array(pattern.findall(bus_lines_str.strip().replace('x','0')),dtype = int)!=0)[0]
n = bus_lines.prod()/bus_lines
time = sum([(bus_lines[i]-offset[i])*n[i]*pow(int(n[i]), -1, int(bus_lines[i])) for i in range(len(n))]) % bus_lines.prod()
print("Part 2: {} is the first timestamp where the departure times match their offset in the list.".format(time))
