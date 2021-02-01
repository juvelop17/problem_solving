import time

ptime = time.time_ns()

import sys

sys.stdin = open('input.txt', 'r')


#####################################################


def solution(a, b, mp):
    idx = 0
    remain = a
    sum = 0
    activate = False
    # for i in range(len(mp)):
    #     if mp[i] == '1':
    #         idx = i
    #         break

    while idx < len(mp):
        print('idx,sum',idx,sum)
        if mp[idx] == '1':
            if activate:
                sum += a - remain
            idx += 1
            remain = a
            activate = False
        else:
            if remain <= 0:
                for i in range(idx,len(mp)):
                    if mp[i] == '1':
                        idx = i
                        sum += a
                        activate = True
                        break
            else:
                remain -= b
                idx += 1
    print('sum',sum)
    print()
    return

t = int(input())
for tt in range(t):
    a, b = map(int, input().split())
    mp = input()
    solution(a, b, mp)

#####################################################

print('time', time.time_ns() - ptime)

