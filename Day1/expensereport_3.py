import os
import numpy as np

def main():
    num_lines = sum(1 for line in open('Day1/input.txt'))
    print("Number of Inputs: {}".format(num_lines))
    
    inputs = np.zeros(num_lines)
    with open('Day1/input.txt', 'r') as ipnt:
        for i, line in enumerate(ipnt):
            inputs[i] = int(line)
    for i, num1 in enumerate(inputs):
        for j, num2 in enumerate(inputs):
            for k, num3 in enumerate(inputs):
                if num1 + num2 + num3 == 2020:
                    print("{} + {} + {} = 2020, {} * {} * {} = {}".format(num1, num2, num3, num1, num2, num3, num1*num2*num3))
                    break


if __name__ == "__main__":
    main()
