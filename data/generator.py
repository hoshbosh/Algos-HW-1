import random
import sys

# Validate the input, n needs to be an int
try:
    n = int(sys.argv[1])
except:
    print("Input needs to be an integer")
    quit()

# Initialize the array of arrays, each element is a hospital/student, and within that element is an array of its rankings
input = [[list(range(1, n+1))] for x in range(n*2)]

# Write to file
with open(f"n_{n}.in", "w") as f:
    f.write(f"{n}\n")
    for rankings in input:
        for curr in rankings:
            # Randomize entries
            random.shuffle(curr)
            line = ""
            for index, val in enumerate(curr):
                line += str(val)
                if index != len(curr)-1:
                    line += " "
            f.write(line + "\n")
