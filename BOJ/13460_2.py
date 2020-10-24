# 구슬 탈출 2

import time

prev_time = time.time_ns()



import sys
# sys.stdin = open('input.txt', 'r')


read = sys.stdin.readline

ri, rj = -1, -1
bi, bj = -1, -1
hi, hj = -1, -1
mp = []
visited = []


def printMap(ball_pos):
    ri, rj, bi, bj = ball_pos
    for i in range(len(mp)):
        for j in range(len(mp[0])):
            if i == ri and j == rj:
                print('R', end=' ')
            elif i == bi and j == bj:
                print('B', end=' ')
            else:
                print(mp[i][j], end=' ')
        print()


# dir : 북, 동, 남, 서
def tilting(dir, ball_pos):
    result = False
    ri, rj, bi, bj = ball_pos
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    new_bi = bi
    new_bj = bj
    bcnt = 0
    while mp[new_bi][new_bj] != '#':
        if mp[new_bi][new_bj] == 'O':
            return -1
        new_bi += di[dir]
        new_bj += dj[dir]
        bcnt += 1
    new_bi -= di[dir]
    new_bj -= dj[dir]

    new_ri = ri
    new_rj = rj
    rcnt = 0
    while mp[new_ri][new_rj] != '#':
        if mp[new_ri][new_rj] == 'O':
            return 1
        new_ri += di[dir]
        new_rj += dj[dir]
        rcnt += 1
    new_ri -= di[dir]
    new_rj -= dj[dir]

    if new_ri == new_bi and new_rj == new_bj:
        if bcnt > rcnt:
            new_bi -= di[dir]
            new_bj -= dj[dir]
        else:
            new_ri -= di[dir]
            new_rj -= dj[dir]

    ball_pos[:] = [new_ri, new_rj, new_bi, new_bj]
    return 0


def DFS(dir, ball_pos, cnt):
    res = 11
    # print('ball_pos', ball_pos, 'cnt', cnt)
    # printMap(ball_pos)

    for i in range(4):
        new_ball_pos = ball_pos[:]
        tilting_res = tilting(i, new_ball_pos)
        if tilting_res == -1:
            continue
        elif tilting_res == 1:
            return cnt + 1

        new_ri, new_rj, new_bi, new_bj = new_ball_pos
        if visited[new_ri][new_rj][new_bi][new_bj] <= cnt + 1:
            continue
        visited[new_ri][new_rj][new_bi][new_bj] = cnt + 1

        DFS_res = DFS(i, new_ball_pos, cnt + 1)
        if DFS_res != -1:
            # print('goal!', DFS_res)
            res = min(res, DFS_res)
    return res


def solution(N, M):
    ball_pos = [ri, rj, bi, bj]
    res = DFS(0, ball_pos, 0)
    if res == 11:
        return -1
    return res


N, M = map(int, read().split())
for i in range(N):
    li = list(read().strip())
    for j in range(M):
        if li[j] == 'R':
            ri, rj = i, j
            li[j] = '.'
        elif li[j] == 'B':
            bi, bj = i, j
            li[j] = '.'
        elif li[j] == 'O':
            hi, hj = i, j
    mp.append(li)
visited = [[[[11 for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
print(solution(N, M))



print('time', time.time_ns() - prev_time)
