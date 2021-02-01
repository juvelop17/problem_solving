import time

ptime = time.time_ns()

import sys

sys.stdin = open('input.txt', 'r')


#####################################################

def solution(n, c0, c1, h, bstr):
    # print('n, c0, c1, h, bstr', n, c0, c1, h, bstr)

    cnt0 = 0
    for b in bstr:
        if b == '1':
            cnt0 += 1

    cnt1 = 0
    for b in bstr:
        if b == '0':
            cnt1 += 1

    return min(len(bstr) * c0 + cnt0 * h, len(bstr) * c1 + cnt1 * h, cnt0 * c1 + cnt1 * c0)


t = int(input())
for tt in range(t):
    n, c0, c1, h = map(int, input().split())
    bstr = input()
    print(solution(n, c0, c1, h, bstr))

#####################################################

print('time', time.time_ns() - ptime)

