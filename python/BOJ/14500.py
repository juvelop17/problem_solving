import time

ptime = time.time_ns()

import sys
sys.stdin = open('input.txt','r')




di = [-1,1,0,0]
dj = [0,0,-1,1]

N, M = map(int,input().split())
mp = [list(map(int,input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

max_result = -1
max_value = max(map(max,mp))

def printMap(mp):
    for i in range(N):
        for j in range(M):
            print(mp[i][j],end=' ')
        print()
    print()

def checkRange(i,j):
    return i >= 0 and i < N and j >= 0 and j < M

def dfs(i,j,k,sum):
    global max_result

    if k == 3:
        # print('return',sum)
        # print('i,j,k,sum', i, j, k, sum)
        # printMap(visited)
        if sum > max_result:
            max_result = sum
        return 1

    if (4 - k) * max_value + sum <= max_result:
        return

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if not checkRange(ni, nj) or visited[ni][nj]:
            continue
        if k == 1:
            visited[ni][nj] = 1
            sum += mp[ni][nj]
            dfs(i, j, k + 1, sum)
            sum -= mp[ni][nj]
            visited[ni][nj] = 0
        visited[ni][nj] = 1
        sum += mp[ni][nj]
        dfs(ni, nj, k + 1, sum)
        sum -= mp[ni][nj]
        visited[ni][nj] = 0

def solution():
    for i in range(0,N):
        for j in range(0,M):
            visited[i][j] = 1
            dfs(i,j,0,mp[i][j])
            visited[i][j] = 0

    return max_result


print(solution())




print('time',time.time_ns()-ptime)

