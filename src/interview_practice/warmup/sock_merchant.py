#!/bin/python3

import math
import os
import random
import re
import sys

os.environ['OUTPUT_PATH'] = "result.txt"

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    """
    >>> sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
    3
    """
    count_dict = {}
    for i in ar:
        count_dict[i] = count_dict.get(i, 0) + 1
    
    sum_pairs = 0
    for count in count_dict.values():
        sum_pairs += count // 2
    
    return sum_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

    ##Tests:
    import doctest
    doctest.testmod()

