import time

ptime = time.time_ns()

import sys
sys.stdin = open('input.txt','r')

#####################################################


N, M = map(int, input().split())
r, c, d = map(int, input().split())

mp = []
for _ in range(N):
    mp.append(list(map(int, input().split())))
visited = [[0 for _ in range(M)] for _ in range(N)]

di = [-1,0,1,0]
dj = [0,1,0,-1]

def checkRange(i,j):
    return i >= 0 and i < N and j >= 0 and j < M

def dfs(i,j,dir):
    # print('i,j,dir',i,j,dir)
    isClean = False
    for k in range(dir+3, dir-1, -1):
        ni = i + di[k%4]
        nj = j + dj[k%4]

        if not checkRange(ni, nj):
            continue

        if mp[ni][nj] == 0 and visited[ni][nj] == 0: # 벽, 청소한 공간이거나 방문한 공간 아닐경우
            isClean = True
            mp[ni][nj] = 2
            visited[ni][nj] = 1
            dfs(ni, nj, k%4)
            break

    if not isClean:
        ni = i - di[dir]
        nj = j - dj[dir]
        if mp[ni][nj] == 1:
            return
        dfs(ni, nj, dir)


def cal():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if mp[i][j] == 2:
                cnt += 1
    return cnt

def solution():
    i, j = r, c
    mp[i][j] = 2
    visited[i][j] = 1
    dfs(i,j,d)

    # print(mp)

    return cal()



print(solution())









#####################################################

print('time',time.time_ns()-ptime)

