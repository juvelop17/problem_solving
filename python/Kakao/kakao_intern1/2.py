#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMinimumDifference' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY a
#  2. STRING_ARRAY b
#


def getMinimumDifference(a, b):
    # Write your code here
    print(a, b)
    n = max(len(a), len(b))

    result = [0 for _ in range(n)]

    for i in range(n):
        # 문자열 길이 비교
        if len(a) == 0 or len(b) == 0:
            result[i] = -1
        elif i >= len(a) or i >= len(b):
            result[i] = -1
        elif len(a[i]) != len(b[i]):
            result[i] = -1
        # sort로
        else:
            a_sort = sorted(a[i])
            b_sort = sorted(b[i])

            result[i] = get_diff_number(a_sort,b_sort)

    print(result)
    return result


def get_diff_number(a_sort, b_sort):
    i = j = 0
    cnt = 0
    n = len(a_sort)

    while(i < n):
        if j >= n:
            i += 1
            cnt += 1
        elif a_sort[i] == b_sort[j]:
            i += 1
            j += 1
        elif a_sort[i] > b_sort[j]:
            j += 1
        elif a_sort[i] < b_sort[j]:
            i += 1
            cnt += 1

    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = input()
        a.append(a_item)

    b_count = int(input().strip())

    b = []

    for _ in range(b_count):
        b_item = input()
        b.append(b_item)

    result = getMinimumDifference(a, b)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
