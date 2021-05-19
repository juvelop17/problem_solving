import sys
import time

ptime = time.time_ns()

sys.stdin = open('input.txt', 'r')


#####################################################

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def move(board, visit, red, blue, dir, cnt):
    if cnt > 10:
        return 11
    # print(red, blue, dir, cnt)

    dred, dblue = 0, 0 # 이동거리
    sred, sblue = False, False # 성공여부

    while True:
        blue[0] += di[dir]
        blue[1] += dj[dir]
        dblue += 1
        if board[blue[0]][blue[1]] == 'O':
            sblue = True
        if board[blue[0]][blue[1]] == '#':
            blue[0] -= di[dir]
            blue[1] -= dj[dir]
            dblue -= 1
            break

    if sblue:
        return 10 ** 9

    while True:
        red[0] += di[dir]
        red[1] += dj[dir]
        dred += 1
        if board[red[0]][red[1]] == 'O':
            sred = True
        if board[red[0]][red[1]] == '#':
            red[0] -= di[dir]
            red[1] -= dj[dir]
            dred -= 1
            break

    if sred:
        return cnt

    if red[0] == blue[0] and red[1] == blue[1]:
        if dred < dblue:
            blue[0] -= di[dir]
            blue[1] -= dj[dir]
        else:
            red[0] -= di[dir]
            red[1] -= dj[dir]

    if visit[red[0]][red[1]][blue[0]][blue[1]] <= cnt:
        return 11
    visit[red[0]][red[1]][blue[0]][blue[1]] = cnt

    min_cnt = 11
    for d in range(4):
        min_cnt = min(min_cnt, move(board, visit, red[:], blue[:], d, cnt + 1))

    return min_cnt


def solution(N, M, board):
    visit = [[[[11 for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
    red = [-1, -1]
    blue = [-1, -1]

    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                red = [i, j]
                board[i][j] = '.'
            if board[i][j] == 'B':
                blue = [i, j]
                board[i][j] = '.'

    visit[red[0]][red[1]][blue[0]][blue[1]] = 0

    min_cnt = 11
    for d in range(4):
        min_cnt = min(min_cnt, move(board, visit, red[:], blue[:], d, 1))

    if min_cnt > 10:
        return -1
    return min_cnt

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input().strip()))

print(solution(N, M, board))

#####################################################



print('time', (time.time_ns() - ptime)/10**6,'ms')
