
import time

ptime = time.time_ns()

import sys
sys.stdin = open('input.txt','r')


#####################################################


R, C, T = map(int, input().split())
mp = [list(map(int,input().split())) for _ in range(R)]
purifier = [[i,j] for j in range(C) for i in range(R) if mp[i][j] == -1 ]

def printMap(mp):
    for i in range(R):
        for j in range(C):
            print(mp[i][j],end='\t')
        print()
    print()

def checkRange(i,j):
    return i >= 0 and i < R and j >= 0 and j < C

def checkChange(mp, new_mp):
    for i in range(R):
        for j in range(C):
            if mp[i][j] != new_mp[i][j]:
                return True
    return False

def diffusion(mp):
    new_mp = [[0 for _ in range(C)] for _ in range(R)]
    for i,j in purifier:
        new_mp[i][j] = -1

    dust_list = []
    for i in range(R):
        for j in range(C):
            if mp[i][j] != 0 and mp[i][j] != -1:
                dust_list.append([i,j])

    di = [-1,1,0,0]
    dj = [0,0,-1,1]
    while dust_list:
        dust = dust_list.pop(0)
        dui = dust[0]
        duj = dust[1]
        dcnt = 0

        new_mp[dui][duj] += mp[dui][duj]
        for d in range(4):
            ndui = dui + di[d]
            nduj = duj + dj[d]
            if checkRange(ndui,nduj) and mp[ndui][nduj] != -1:
                new_mp[ndui][nduj] += mp[dui][duj] // 5
                dcnt += 1
        if dcnt > 0:
            new_mp[dui][duj] -= mp[dui][duj] // 5 * dcnt
    # printMap(new_mp)

    return new_mp

def purification(mp):
    new_mp = [[mp[i][j] for j in range(C)] for i in range(R)]
    for i,j in purifier:
        new_mp[i][j] = -1

    # upper
    pi, pj = purifier[0]
    for i in range(pi-1,0,-1):
        new_mp[i][0] = mp[i-1][0]
    for j in range(0,C-1):
        new_mp[0][j] = mp[0][j+1]
    for i in range(pi):
        new_mp[i][C-1] = mp[i+1][C-1]
    for j in range(C-1,1,-1):
        new_mp[pi][j] = mp[pi][j-1]
    new_mp[pi][1] = 0

    # lower
    pi, pj = purifier[1]
    for i in range(pi+1,R-1):
        new_mp[i][0] = mp[i+1][0]
    for j in range(C-1):
        new_mp[R-1][j] = mp[R-1][j+1]
    for i in range(R-1,pi-1,-1):
        new_mp[i][C-1] = mp[i-1][C-1]
    for j in range(C-1,1,-1):
        new_mp[pi][j] = mp[pi][j-1]
    new_mp[pi][1] = 0

    return new_mp

def solution(mp):
    answer = -1
    for _ in range(T):
        # 확산
        mp = diffusion(mp)

        # 공기청정
        mp = purification(mp)

        # if not checkChange(mp, new_mp):
        #     break
        # printMap(mp)

    answer = sum(map(sum,mp)) + 2 # 공기 청정기 -1 2개

    return answer

print(solution(mp))




#####################################################

print('time',time.time_ns()-ptime)

