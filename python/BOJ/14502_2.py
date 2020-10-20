import time

ptime = time.time_ns()

import sys
sys.stdin = open('input.txt','r')

#####################################################

import copy

N, M = map(int, input().split())
mp = []
for _ in range(N):
    mp.append(list(map(int, input().split())))

def combinations(arr, r):
    res = []
    for i in range(len(arr) - r + 1):
        if r == 1:
            res.append([arr[i]])
        else:
            for comb in combinations(arr[i + 1:], r - 1):
                res.append([arr[i]] + comb)
    return res

di = [-1,1,0,0]
dj = [0,0,-1,1]

def dfs(mp, visited, i, j):
    visited[i][j] = 1
    mp[i][j] = 2
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if not checkRange(ni, nj):  # 범위 체크
            continue
        if visited[ni][nj] or mp[ni][nj] != 0: # 방문 체크, 공간 체크
            continue
        dfs(mp, visited, ni, nj)

def checkRange(i, j):
    return i >= 0 and i < N and j >= 0 and j < M

def count(mp):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if mp[i][j] == 0:
                cnt += 1
    return cnt

def cal():
    new_mp = copy.deepcopy(mp)
    visited = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if new_mp[i][j] == 2 and visited[i][j] == 0:
                dfs(new_mp, visited, i, j)
    # print(new_mp)
    return count(new_mp)

def solution():
    answer = -1

    empty_pos = []
    for i in range(N):
        for j in range(M):
            if mp[i][j] == 0:
                empty_pos.append((i,j))

    cands = combinations(empty_pos,3)
    for cand in cands:
        for pos in cand:
            mp[pos[0]][pos[1]] = 1
        answer = max(answer,cal())
        for pos in cand:
            mp[pos[0]][pos[1]] = 0
        # print('answer, cand', answer, cand)

    return answer

print(solution())






#####################################################

print('time',time.time_ns()-ptime)

