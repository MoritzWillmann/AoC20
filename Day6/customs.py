def main():
    count1 = 0
    count2 = 0
    collect = ""
    collect2 = []
    with open('Day6/input.txt', 'r') as ipnt:
        for line in ipnt:
            if line == "\n":
                count1 += len(set(collect))
                collect = ""
                count2 += len(set(collect2[0]).intersection(*collect2))
                collect2 = []
            else:
                collect += line.strip()
                collect2.append(line.strip())
    count1 += len(set(collect))
    count2 += len(set(collect2[0]).intersection(*collect2))
    print("Any: {} All 2: {}".format(count1, count2))

if __name__ == "__main__":
    main()
