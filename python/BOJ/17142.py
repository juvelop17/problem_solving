
import time

ptime = time.time_ns()

import sys
sys.stdin = open('input.txt','r')


#####################################################

N, M = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)]

def combinations(arr, r):
    res = []
    for i in range(len(arr)):
        if r == 1:
            res.append([arr[i]])
        else:
            for comb in combinations(arr[i+1:], r-1):
                res.append([arr[i]] + comb)
    return res

def printMap(mp):
    for i in range(N):
        for j in range(N):
            print(mp[i][j], end='\t')
        print()
    print()

def checkRange(i,j):
    return i >= 0 and i < N and j >= 0 and j < N

def solution(mp):
    time_min = 10**9

    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    virus_list = []
    for i in range(N):
        for j in range(N):
            if mp[i][j] == 2:
                virus_list.append((i, j))

    for comb in combinations(virus_list,M):
        # print('comb',comb)

        time_mp = [[-1 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if mp[i][j] == 1:
                    time_mp[i][j] = '-'

        que = []
        for virus in comb:
            que.append([*virus,0])

        while que:
            node = que.pop(0)
            i, j, time = node
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if not checkRange(ni,nj) or time_mp[ni][nj] != -1:
                    continue
                time_mp[ni][nj] = time+1
                que.append([ni, nj, time+1])

        for virus in virus_list:
            time_mp[virus[0]][virus[1]] = '*'
        for virus in comb:
            time_mp[virus[0]][virus[1]] = 0
        # printMap(time_mp)

        mx = 0
        isSuccess = True
        for i in range(N):
            for j in range(N):
                if time_mp[i][j] == -1:
                    isSuccess = False
                if time_mp[i][j] != '-' and time_mp[i][j] != '*'and mx < time_mp[i][j]:
                    mx = time_mp[i][j]
        if not isSuccess:
            continue
        if mx < time_min:
            time_min = mx

        # print('time_min,mx',time_min,mx)

    if time_min == 10**9:
        return -1

    return time_min


print(solution(mp))







#####################################################

print('time',time.time_ns()-ptime)

