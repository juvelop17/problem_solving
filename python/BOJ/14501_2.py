import time

ptime = time.time_ns()

import sys
sys.stdin = open('input.txt','r')

#####################################################

N = int(input())
schedule = []
for _ in range(N):
    schedule.append(list(map(int, input().split())))

max_result = -1
cnt = 0

def dfs(idx, total):
    global cnt
    cnt += 1
    print('idx, total, cnt',idx, total, cnt)

    global max_result
    if idx == N:
        if total > max_result:
            max_result = total
        return
    dfs(idx+1, total)
    if idx + schedule[idx][0] <= N:
        dfs(idx+schedule[idx][0],total+schedule[idx][1])

def solution():
    dfs(0, 0)

    return max_result

print(solution())








#####################################################

print('time',time.time_ns()-ptime)

