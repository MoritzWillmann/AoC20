def main():
    count1 = 0
    count3 = 0
    count5 = 0
    count7 = 0
    count2 = 0
    with open('Day3/input.txt', 'r') as inpt:
        for i, line in enumerate(inpt):
            line = line.strip()
            if line[(i)%len(line)] == "#":
                count1 += 1
            if line[(3*i)%len(line)] == "#":
                count3 += 1
            if line[(5*i)%len(line)] == "#":
                count5 += 1
            if line[(7*i)%len(line)] == "#":
                count7 += 1
            if not i%2 and line[int(i/2)%len(line)] == "#":
                count2 += 1
    print("Number of Trees:\n count1: {}\n count3: {}\n count5: {}\n count7: {}\n count2: {}\n mult: {}".format(count1, count3, count5, count7, count2, count1*count3*count5*count7*count2))
if __name__ == "__main__":
    main()
