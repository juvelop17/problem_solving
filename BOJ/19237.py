

import time
import sys
sys.stdin = open("input.txt",'r')

ptime = time.time_ns()

#################################################################

N, M, k = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)] # 상어 존재 여부

sharks = [[-1,-1,-1] for _ in range(M)] # i, j, dir
for i in range(N):
    for j in range(N):
        if mp[i][j] != 0:
            sharks[mp[i][j]-1][0] = i
            sharks[mp[i][j]-1][1] = j
scant_mp = [[[-1,-1] for _ in range(N)] for _ in range(N)] # shark_num, remain # 상어 냄새 흔적
shark_dir = list(map(int, input().split())) # 위 아래 왼 오
for i, dir in enumerate(shark_dir):
    sharks[i][2] = dir-1

move_priority = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]
for move in move_priority:
    for m in move:
        for i in range(4):
            m[i] -= 1

di = [-1,1,0,0]
dj = [0,0,-1,1]

def checkRange(i,j):
    return i >= 0 and i < N and j >= 0 and j < N

def spread(sharks, scant_mp):
    for idx, shark in enumerate(sharks):
        if shark == [-1,-1,-1]:
            continue
        ci, cj, cdir = shark
        scant_mp[ci][cj] = [idx, k]

def move(sharks, scant_mp):
    new_mp = [[0 for _ in range(N)] for _ in range(N)]
    for idx, shark in enumerate(sharks):
        ci, cj, cdir = shark

        # 빈칸 선택
        is_blank = False
        for d in range(4):
            ndir = move_priority[idx][cdir][d]
            ni = ci + di[ndir]
            nj = cj + dj[ndir]
            if checkRange(ni,nj) and scant_mp[ni][nj][0] == -1:
                is_blank = True
                if new_mp[ni][nj] != 0: # 상어가 이미 존재하는 경우
                    sharks[idx] = [-1, -1, -1]
                    break
                new_mp[ni][nj] = idx + 1
                sharks[idx] = [ni, nj, ndir]
                break

        # 자신흔적칸 선택
        if not is_blank:
            for d in range(4):
                ndir = move_priority[idx][cdir][d]
                ni = ci + di[ndir]
                nj = cj + dj[ndir]
                if checkRange(ni, nj) and scant_mp[ni][nj][0] == idx:
                    new_mp[ni][nj] = idx + 1
                    sharks[idx] = [ni, nj, ndir]
                    break

    return new_mp

def reduce(scant_mp):
    for i in range(N):
        for j in range(N):
            if scant_mp[i][j][0] != -1:
                scant_mp[i][j][1] -= 1
                if scant_mp[i][j][1] == 0:
                    scant_mp[i][j] = [-1,-1]

def solution(sharks, mp, scant_mp):
    tcnt = 0

    while tcnt <= 1000:
        is_finish = True
        for i in range(N):
            for j in range(N):
                if mp[i][j] > 1:
                    is_finish = False
        if is_finish:
            return tcnt

        tcnt += 1

        # 냄새 뿌리기
        spread(sharks, scant_mp)

        # 이동
        mp = move(sharks, scant_mp)

        # 냄새 줄이기
        reduce(scant_mp)

        # printMap(mp)
        # printMap(scant_mp)

    return -1

def printMap(mp):
    for i in range(N):
        for j in range(N):
            print(str(mp[i][j]).center(10),end='|')
        print()
    print()

print(solution(sharks,mp,scant_mp))






#################################################################


print('time',time.time_ns()-ptime)

