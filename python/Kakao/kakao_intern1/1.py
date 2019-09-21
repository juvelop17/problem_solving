#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'calculateAmount' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#


def calculateAmount(prices):
    # Write your code here
    answer = 0

    d = []
    cost = []
    min_list = []

    min_list.append(100000000)
    d.append(0)
    cost.append(prices[0])

    for i in range(1, len(prices)):
        min_val = min(min_list[i - 1], prices[i - 1])
        min_list.append(min_val)
        d.append(min_val)

        if d[i] < prices[i]:
            cost.append(prices[i] - d[i])
        else:
            cost.append(0)

    for _c in cost:
        answer += _c

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    prices_count = int(input().strip())

    prices = []

    for _ in range(prices_count):
        prices_item = int(input().strip())
        prices.append(prices_item)

    result = calculateAmount(prices)

    fptr.write(str(result) + '\n')

    fptr.close()
