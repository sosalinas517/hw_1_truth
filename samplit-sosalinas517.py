#The script must:
#1. Accept a single filename as a command-line argument.
#2. Read the file line by line.
#3. Output each line with a 1% probability (i.e., random.random() < 0.01).
#4. Preserve the original line order.
#5. Print the sampled lines to standard output.

import random

for line in open("nobel-prize-laureates.csv"):
    if random.random() < 0.01:
        print(line, end='')

