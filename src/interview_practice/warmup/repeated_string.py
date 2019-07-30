#!/bin/python3

import math
import os
import random
import re
import sys
os.environ['OUTPUT_PATH'] = "result.txt"


# Complete the repeated_string function below.
def repeated_string(s, n):
    """
    Repeat string many times and find how many a's 
    there are in the first n characters
    >>> repeated_string("aba", 10)
    7
    >>> repeated_string("abcac", 10)
    4
    >>> repeated_string("a", 10)
    10
    >>> repeated_string("a", 1000000000000)
    1000000000000
    """
    count = 0
    if s == "a":
        return n
    count_a = s.count("a")
    length = len(s)
    full_repetitions = (n // length)
    count = full_repetitions * count_a
    # print(full_repetitions, count, length * full_repetitions)
    for i in range(n - length * full_repetitions):
        if s[i] == "a":
            count += 1 
    return count
    # for i in range(n):
    #     current = s[i%len(s)]
    #     # print(i, i%len(s), current)
    #     if current == "a":
    #         count += 1
    # return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeated_string(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

    ##Tests:
    # import doctest
    # doctest.testmod()
