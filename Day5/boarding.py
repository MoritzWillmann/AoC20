import numpy as np

def main():
    seats = np.zeros((128, 8),dtype=int)
    with open('Day5/input.txt', 'r') as ipnt:
        for line in ipnt:
            line = line.strip().replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
            #row = np.array([int(char=="B") for char in line[:7]])
            #col = np.array([int(char=="R") for char in line[7:]])
            #row = np.dot(row, [64, 32, 16, 8, 4, 2, 1])
            #col = np.dot(col, [4, 2, 1])
            
            row = int(line[:7],2)
            col = int(line[7:], 2)
            seats[row, col] = 1
    
    occupied = np.dot(np.transpose(np.nonzero(seats)), [8, 1])
    seatid = [i for i,x in enumerate(np.diff(occupied)) if x == 2]
    print("Highest: {} Your Seat: {}".format(max(occupied), seatid[0] + min(occupied) + 1))

if __name__ == "__main__":
    main()
