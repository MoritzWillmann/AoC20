import numpy as np

def main():
    count1 = 0
    valid = np.zeros(7, dtype=bool)
    with open('./input.txt', 'r') as ipnt:
        for i, line in enumerate(ipnt):
            if line == "\n":
                if all(flag for flag in valid):
                    count1 += 1
                valid = np.zeros(7, dtype=bool)
            else:
                line = line.strip().split(' ')
                for j, entry in enumerate(line):
                    [key, value] = entry.split(':')
                    if key=="byr" and (1920 <= int(value) <= 2002):
                        valid[0] = True
                    elif key=="iyr" and (2010 <= int(value) <= 2020):
                        valid[1] = True
                    elif key=="eyr" and (2020 <= int(value) <= 2030):
                        valid[2] = True
                    elif key=="hgt" and ((value[-2:] == "cm" and (150 <= int(value[:-2]) <= 193)) or (value[-2:] == "in" and (59 <= int(value[:-2]) <= 76))):
                        valid[3] = True
                    elif key=="hcl" and len(value)==7 and value[0] == "#" and (char in "0123456789abcdef" for char in value[1:]):
                        valid[4] = True
                    elif key=="ecl" and value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                        valid[5] = True
                    elif key=="pid" and len(value)==9:
                        valid[6] = True

            print(line)
            print(valid)
    if all(flag for flag in valid):
        count1+=1
    print("Number of valid passports: {}\n".format(count1))

if __name__ == "__main__":
    main()
