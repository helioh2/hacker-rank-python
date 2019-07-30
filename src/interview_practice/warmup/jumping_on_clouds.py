#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumping_on_clouds function below.
def jumping_on_clouds(c):
    """
    0 is safe, 1 must be avoided
    Maximum jump is 2
    The function must return the minimum jumps needed to get to the end
    >>> jumping_on_clouds([0, 0, 1, 0, 0, 1, 0])
    4
    >>> jumping_on_clouds([0, 1, 0, 0, 0, 1, 0])
    3
    """
    i = 0
    steps = 0
    while i < len(c)-1:
        if i+2 < len(c) and c[i+2] == 1:
            i += 1
        else:
            i += 2
        steps += 1
    return steps



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumping_on_clouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

    


