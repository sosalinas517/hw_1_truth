
import random
import sys
filename = sys.argv[1]

for line in open(filename):
    if random.random() < 0.01:
        print(line, end='')
        print("Hi :P)")