def memory1(init_vals, i_desired):
    vals = [0] * i_desired
    vals[0:len(init_vals)] = init_vals

    last_seen = {}
    for i, val in enumerate(init_vals):
        last_seen[val] = i
    
    for i in range(len(init_vals), i_desired):
        if vals[i-1] in last_seen.keys():
            vals[i] = i - last_seen[vals[i-1]] - 1
        else:
            vals[i] = 0
        last_seen[vals[i-1]] = i-1
    return vals[-1]

input = [5, 2, 8, 16, 18, 0 , 1]
print("Part 1: {}, Part 2: {}".format(memory1(input, 2020), memory1(input, 30000000)))