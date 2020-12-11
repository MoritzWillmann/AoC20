import re
def main():
    pattern = re.compile(r'([a-z]{3})\s([\+-]\d+)')
    with open('Day8/input.txt', 'r') as inpt:
        lines = inpt.readlines()
        #check swapping no or each instruction
        for swap_i in range(-1, len(lines)):
            i = 0
            loop = False
            visited = []
            accumulator = 0
            while not loop and i < len(lines):
                visited.append(i)
                [(instruction, value)] = pattern.findall(lines[i])
                #swap instruction at index swap_i
                if i == swap_i:
                    if instruction == "jmp":
                        instruction = "nop"
                        swp = ["jmp", "nop"]
                    elif instruction == "nop":
                        instruction = "jmp"
                        swp = ["nop", "jmp"]
                #execute instruction
                if instruction == "acc":
                    accumulator += int(value)
                    i += 1
                elif instruction == "jmp":
                    i += int(value)
                elif instruction == "nop":
                    i += 1
                else:
                    #return error when unknown key
                    print("unknown key")
                    return 10
                #check if loop    
                if i in visited:
                    #save accumulator for part1
                    if swap_i == -1:
                        part1 = accumulator
                    loop = True
            #if swap at swap_i yields no loop break loop
            if not loop:
                break
    print("Part1: {}, Part 2: {} with {} swapped for {} in instruction {}".format(part1, accumulator, swp[0], swp[1], swap_i))

if __name__ == '__main__':
    main()

