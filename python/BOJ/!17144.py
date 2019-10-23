import time
import sys
from collections import deque
import copy

prev_time = time.time_ns()
sys.stdin = open('input.txt','r')
read = sys.stdin.readline

def solution():
    find()


    spread()




def find():
    for i in range(R):
        for j in range(C):
            if A[i][j] == -1:
                purifier.append([i,j])
            elif A[i][j] > 0:
                dust.append([i,j])

def spread():
    global A

    # original_map = [A[r][:] for r in range(R)]
    memory_map = [A[r][:] for r in range(R)]

    new_dust = []
    for d in dust:
        val = A[d[0]][d[1]] // 5
        print(d, A[d[0]][d[1]], val)

        cnt = 0
        for a in range(4):
            new_i = d[0] + di[a]
            new_j = d[1] + dj[a]
            if checkRange(new_i,new_j) and [new_i,new_j] not in purifier:
                cnt+=1
                memory_map[new_i][new_j] += val
        memory_map[d[0]][d[1]] -= val*cnt
        printMap(memory_map)

    A = memory_map
    printMap(A)

    for d in new_dust:
        if d not in dust:
            dust.append(d)


def purify():
    purifier.sort()
    up = purifier[0]
    down = purifier[1]

    curr_i = up[0]
    curr_j = up[1]
    curr_val = 0
    for d in range(4):
        while True:
            next_i = curr_i + up_di[d]
            next_j = curr_j + up_dj[d]

            if not checkRange(next_i,next_j):
                break
            if
            next_val = A[next_i][next_j]
            A[next_i][next_j] = curr_val
            curr_val = next_val

            curr_i = next_i
            curr_j = next_j




def purifySpread():



def checkRange(i,j):
    return 0<=i<R and 0<=j<C


def printMap(memory_map):
    for i in range(R):
        for j in range(C):
            print(memory_map[i][j],end='\t')
        print()
    print()



di = [-1,1,0,0]
dj = [0,0,-1,1]

dust = []
purifier = []
R,C,T = map(int,read().strip().split())
A = [list(map(int,read().strip().split())) for _ in range(R)]


print(solution())
print('time',time.time_ns()-prev_time)

