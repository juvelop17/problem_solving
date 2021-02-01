import time

ptime = time.time_ns()

import sys

sys.stdin = open('input.txt', 'r')


#####################################################

def solution(n,k,clist):
    total_day = 10**5
    color_candi = set()
    for i in clist:
        if i not in color_candi:
            color_candi.add(i)

    for cur_color in color_candi:
        i = 0
        cnt = 0
        while i < len(clist):
            if clist[i] == cur_color:
                i += 1
            else:
                i += k
                cnt += 1
        if cnt < total_day:
            total_day = cnt

    return total_day

t = int(input())
for tt in range(t):
    n, k = map(int,input().split())
    clist = list(map(int,input().split()))
    print(solution(n,k,clist))

#####################################################

print('time', time.time_ns() - ptime)

