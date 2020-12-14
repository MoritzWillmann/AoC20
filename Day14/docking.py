import re
mask_pattern = re.compile(r'([01X]+)')
addr_pattern = re.compile(r'mem\[(\d+)\]\s=\s(\d+)')
mem1 = {}
mem2 = {}
with open('Day14/input.txt', 'r') as file:
    for line in file:
        if line.startswith('mask'):
            mask = mask_pattern.search(line.strip()).group()
            # Part 2
            x_cnt = mask.count('X')
        else:
            [(addr, value)] = addr_pattern.findall(line.strip())
            # Part 1
            bin_value = "{0:036b}".format(int(value))
            masked_p1 = int(''.join([(mbit if mbit != 'X' else bin_value[i]) for i, mbit in enumerate(mask)]), 2)
            mem1[addr] = masked_p1
            # Part 2
            addr = "{0:036b}".format(int(addr))
            masked_addr = ''.join([(mbit if mbit != '0' else addr[i]) for i, mbit in enumerate(mask)])
            for i in range(2**x_cnt):
                replacement = [char for char in bin(i)[2:].zfill(x_cnt)]
                mem2[int(''.join([(a if a != 'X' else replacement.pop(0)) for a in masked_addr]), 2)] = int(value)
print("Part 1: The Sum of all masked values in memory is {}".format(sum(mem1.values())))
print("Part 2: The Sum of all masked values in memory is {}".format(sum(mem2.values())))