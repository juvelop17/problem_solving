









import time

ptime = time.time_ns()

import sys
sys.stdin = open('input.txt','r')


#####################################################

N, L = map(int, input().split())
mp = []
for _ in range(N):
    mp.append(tuple(map(int,input().split())))
mp.extend(zip(*mp))

def checkSlope(start, end, slope):
    if start < 0 or end >= len(slope):
        return False

    for i in range(start,end+1):
        if slope[i]:
            return False
        slope[i] = True
    return True

def checkRoad(road):
    slope = [False for _ in range(len(road))]
    idx = 0
    cur_h = -1

    while True:
        if idx == N - 1:
            break

        if abs(road[idx] - road[idx + 1]) > 1:
            return False
        elif abs(road[idx] - road[idx + 1]) == 1:
            if road[idx] > road[idx + 1]:
                start = idx + 1
                end = idx + L
            else:
                start = idx - L + 1
                end = idx

            if checkSlope(start,end,slope):
                for i in range(start,end+1):
                    if road[i] != road[start]:
                        return False
            else:
                return False
        else:
            pass

        idx += 1

    return True

def solution():
    cnt = 0
    for road in mp:
        if checkRoad(road):
            cnt += 1
    return cnt

print(solution())






#####################################################

print('time',time.time_ns()-ptime)

