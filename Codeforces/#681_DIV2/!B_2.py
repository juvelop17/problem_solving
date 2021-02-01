import time

ptime = time.time_ns()

import sys

sys.stdin = open('input.txt', 'r')


#####################################################


def solution(a, b, mp):
    # print(a, b, mp)
    idx = 0
    remain = 0
    sum = 0

    while idx < len(mp):
        # print('idx,sum',idx,sum)
        if mp[idx] == '1':
            if remain <= 0:
                sum += a
            elif remain < a:
                sum += a - remain
            remain = a
            idx += 1
        else:
            remain -= b
            idx += 1
    # print('sum',sum)
    print(sum)
    return

t = int(input())
for tt in range(t):
    a, b = map(int, input().split())
    mp = input()
    solution(a, b, mp)

#####################################################

print('time', time.time_ns() - ptime)

