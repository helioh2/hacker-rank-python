#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the counting_valleys function below.
def counting_valleys(s):
    """
    >>> counting_valleys("UDDDUDUU")
    1
    >>> counting_valleys("DDUUUUDD")
    1
    >>> counting_valleys("DUDUDUDU")
    4
    >>> counting_valleys("DUUUUUDDDDDDUU")
    2
    """
    valleys_count = 0
    level = 0
    for c in s:
        if c == "D":
            level -= 1
        elif c == "U":
            level += 1
            if level == 0:
                valleys_count += 1
    return valleys_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = counting_valleys(s)

    fptr.write(str(result) + '\n')

    fptr.close()

    ##Tests:
    import doctest
    doctest.testmod()


