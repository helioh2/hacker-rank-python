#!/bin/python3

import math
import os
import random
import re
import sys

def rotate_one_left(a):
    """
    >>> rotate_one_left([1, 2, 3, 4, 5])
    [2, 3, 4, 5, 1]
    """
    first = a[0]
    for i in range(1, len(a)):
        a[i-1] = a[i]
    a[len(a)-1] = first
    return a


# Complete the rot_left function below.
def rot_left(a, d):
    """
    >>> rot_left([1, 2, 3, 4, 5], 4)
    [5, 1, 2, 3, 4]
    >>> rot_left([1, 2, 3, 4, 5], 5)
    [1, 2, 3, 4, 5]
    >>> rot_left([1, 2, 3, 4, 5], 3)
    [4, 5, 1, 2, 3]
    >>> rot_left([41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51], 10)
    [77, 97, 58, 1, 86, 58, 26, 10, 86, 51, 41, 73, 89, 7, 10, 1, 59, 58, 84, 77]
    """
    n = len(a)
    d = (d-1)%n + 1  ## rd modulo reduction
    if (n%d == 0):  # dumber strategy when n and d are multiples (O(n*d))
        for _ in range(d):
            a = rotate_one_left(a)
        return a
    # else (optimized strategy when n and d are not multiples (most of the cases)) (O(n))
    first = a[0]
    origin = d%n
    while True:
        destiny = (origin-d) % n
        a[destiny] = a[origin]
        origin = (origin+d) % n
        if origin == 0:
            break
    a[n-d] = first
    return a

def rot_left_pythonic(a, d):
    """
    Always O(n), but uses dynamic list creating (not pure array)

    >>> rot_left_pythonic([1, 2, 3, 4, 5], 4)
    [5, 1, 2, 3, 4]
    >>> rot_left_pythonic([1, 2, 3, 4, 5], 5)
    [1, 2, 3, 4, 5]
    >>> rot_left_pythonic([1, 2, 3, 4, 5], 3)
    [4, 5, 1, 2, 3]
    >>> rot_left_pythonic([41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51], 10)
    [77, 97, 58, 1, 86, 58, 26, 10, 86, 51, 41, 73, 89, 7, 10, 1, 59, 58, 84, 77]
    """
    n = len(a)
    if (n == d):
        return a
    result = []
    i = d%n
    for _ in range(n):
        result.append(a[i])
        i = (i+1)%n
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rot_left(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
