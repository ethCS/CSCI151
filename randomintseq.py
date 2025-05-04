import sys
import stdio
import random

m = int(sys.argv[1])
n = int(sys.argv[2])


num_str = ""

def rng(m, n, num_list):
    for i in range(n):
        rng = random.randint(0, m-1)
        if n - 1 == i:
            num_list += str(rng)
        else:
            num_list += str(rng) + ","
    return num_list


stdio.writeln(rng(m, n, num_str))