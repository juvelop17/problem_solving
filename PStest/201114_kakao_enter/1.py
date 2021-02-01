#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'splitIntoTwo' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#



def splitIntoTwo(arr):
    # Write your code here
    lsum = 0
    rsum = sum(arr)
    cnt = 0
    for cur in range(len(arr)-1):
        lsum += arr[cur]
        rsum -= arr[cur]
        if lsum > rsum:
           cnt += 1

    return cnt

# arr = [10, -5, 6]
arr = [-3, -2, 10, 20, -30]

print(splitIntoTwo(arr))






