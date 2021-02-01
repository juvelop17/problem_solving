import time

ptime = time.time_ns()

import sys

sys.stdin = open('input.txt', 'r')


#####################################################

# primes = []
# l = 400
# a = [False, False] + [True] * (l - 1)
# for i in range(2,l+1):
#     if a[i]:
#         primes.append(i)
#         for j in range(i, l + 1, i):
#             a[j] = False

import math



def solution(n):
    # print('n',n)
    exp = math.ceil(math.log(n, 2))
    # print('exp',exp)

    for i in range(2**exp,2**exp+n):
        if 2 * i <= 4 * n:
            print(2*i, end=' ')
        else:
            print(2**exp * 2 - (2 * i - 4 * n), end=' ')

    print()
    return

t = int(input())
for tt in range(t):
    n = int(input())
    solution(n)

#####################################################

print('time', time.time_ns() - ptime)

