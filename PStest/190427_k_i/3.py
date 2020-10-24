#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'firstOccurrence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING x
#

def firstOccurrence(s, x):
    # Write your code here
    print(s, x)
    start_index = -1
    s_len = len(s)
    x_len = len(x)

    s_index = 0

    is_find = False
    while s_index < s_len and is_find == False:
        x_index = 0
        start_index = s_index
        while x_index < x_len:
            if x[x_index] == '*':
                s_index += 1
                x_index += 1
            elif s[s_index] == x[x_index]:
                s_index += 1
                x_index += 1
            elif s[s_index] != x[x_index]:
                s_index += 1
                break

        if x_index == x_len:
            is_find = True

    if is_find:
        answer = start_index
    else:
        answer = -1

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    x = input()

    result = firstOccurrence(s, x)

    fptr.write(str(result) + '\n')

    fptr.close()
