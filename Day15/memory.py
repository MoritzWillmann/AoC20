def memory1(init_vals, i_desired):
    last_seen = {}
    for i, val in enumerate(init_vals):
        last_seen[val] = i
    
    prev = val
    for i in range(len(init_vals), i_desired):
        if prev in last_seen.keys():
            curr = i - last_seen[prev] - 1
        else:
            curr = 0
        last_seen[prev] = i-1
        prev = curr
    return curr

input = [5, 2, 8, 16, 18, 0 , 1]
print("Part 1: {}, Part 2: {}".format(memory1(input, 2020), memory1(input, 30000000)))