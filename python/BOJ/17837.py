import time

ptime = time.time_ns()

import sys

sys.stdin = open('input.txt', 'r')

#####################################################


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
mals = [list(map(int, input().split())) for _ in range(K)]

di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]

def printMap(mp):
    for i in range(N):
        for j in range(N):
            print(mp[i][j], end='\t')
        print()
    print()

def checkRange(i, j):
    return i >= 0 and i < N and j >= 0 and j < N


def solution(board, mals):
    tcnt = 0
    mal_info = [[] for _ in range(K + 1)]
    mp = [[[] for _ in range(N)] for _ in range(N)]  # board : 색깔 판, mp : 말 판
    for idx, mal in enumerate(mals):
        r, c, dir = mal
        mp[r - 1][c - 1].append(idx + 1)  # dir : 우 좌 상 하
        mal_info[idx + 1] = [r-1,c-1,dir]

    while tcnt <= 1000:
        tcnt += 1
        for mal_num in range(1, K + 1):
            mi,mj,mdir = mal_info[mal_num]

            ni = mi + di[mdir]
            nj = mj + dj[mdir]
            if not checkRange(ni, nj) or board[ni][nj] == 2:  # 장외, 파란색
                ndir = mdir + 1  if mdir == 1 or mdir == 3 else mdir - 1
                ni = mi + di[ndir]
                nj = mj + dj[ndir]
                mal_info[mal_num][2] = ndir
                if not checkRange(ni, nj) or board[ni][nj] == 2:
                    continue

            idx = mp[mi][mj].index(mal_num)
            cur_list = mp[mi][mj][idx:]
            mp[mi][mj] = mp[mi][mj][:idx]

            if board[ni][nj] == 1:  # 빨간색
                cur_list = cur_list[::-1]

            mp[ni][nj].extend(cur_list)
            for cur in cur_list:
                mal_info[cur][:2] = [ni, nj]

            # print('mal_num',mal_num)
            # print('mal_info',mal_info)
            # printMap(mp)

            if len(mp[ni][nj]) >= 4:
                return tcnt

    if tcnt > 1000:
        return -1
    return tcnt


print(solution(board, mals))




#####################################################

print('time', time.time_ns() - ptime)

