def main():
    count1 = 0
    count2 = 0
    with open('Day2/input.txt', 'r') as ipnt:
        for i, line in enumerate(ipnt):
            [lims, letter, password] = line.strip().split(' ')
            lims = lims.split('-')
            letter =letter[0]
            #sledplace rules
            if password.count(letter) >= int(lims[0]) and password.count(letter) <= int(lims[1]):
                count1 += 1
            #official toboggan rules
            if ((password[int(lims[0])-1] == letter and not password[int(lims[1])-1] == letter) or 
                (not password[int(lims[0])-1] == letter and password[int(lims[1])-1] == letter)):
                count2 += 1
    print("Number of valid passwords:\n\tRule1: {}\n\tRule2: {}".format(count1, count2))

if __name__ == "__main__":
    main()
