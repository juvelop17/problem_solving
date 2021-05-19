import sys
import time

ptime = time.time_ns()

sys.stdin = open('input.txt', 'r')


#####################################################

di = [0,1]
dj = [1,0]

def dfs(board, i, j, cnt, total):
    global max_total
    if cnt == 4:
        max_total = max(max_total, total)
        return

    for d in range(2):
        ni = i + di[d]
        nj = j + dj[d]

        if check_range(len(board), ni, nj):
            dfs(board, ni, nj, cnt + 1, total + board[ni][nj])

    if cnt == 2:
        ni1 = i + di[0]
        nj1 = j + dj[0]

        ni2 = i + di[1]
        nj2 = j + dj[1]

        if check_range(len(board),ni1,nj1) and check_range(len(board),ni2,nj2):
            dfs(board, ni, nj, cnt + 1, total + board[ni][nj])

def check_range(n, i, j):
    return 0 <= i and i < n and 0 <= j and j < n

def solution(N, M, board):
    global max_total
    max_total = 0

    for i in range(len(board)):
        for j in range(len(board)):
            if check_range(len(board), i, j):
                dfs(board, i, j, 1, board[i][j])

    return max_total

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
print(solution(N, M, board))

#####################################################



print('time', (time.time_ns() - ptime)/10**6,'ms')
