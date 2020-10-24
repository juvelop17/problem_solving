import time

ptime = time.time_ns()

import sys

sys.stdin = open('input.txt', 'r')

#####################################################


N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
comm = [list(map(int, input().split())) for _ in range(T)]

di = [-1,1,0,0]
dj = [0,0,-1,1]

def rotate(board, num, d, k):
    r = k%M
    if d == 0:
        board[num] = board[num][M-r:] + board[num][0:M-r]
    else:
        board[num] = board[num][r:] + board[num][:r]

def remove(board):
    remove_list = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            for d in range(4):
                ni = (i + di[d])
                nj = (j + dj[d]) % M
                if ni < 0 or ni >= N:
                    continue
                if board[i][j] == board[ni][nj]:
                    remove_list[i][j] = True

    isRemain = False
    for i in range(N):
        for j in range(M):
            if remove_list[i][j]:
                board[i][j] = -1
                isRemain = True

    if not isRemain:
        sum_list = [[0,0] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if board[i][j] != -1:
                    sum_list[i][0] += board[i][j]
                    sum_list[i][1] += 1

        avg_list = [s[0]/s[1] for s in sum_list]
        for i in range(N):
            for j in range(M):
                if board[i][j] > avg_list[i]:
                    board[i][j] -= 1
                elif board[i][j] < avg_list[i]:
                    board[i][j] += 1

def cal(board):
    res = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] != -1:
                res += board[i][j]
    return res

def solution(board, comm):
    for com in comm:
        x, d, k = com # x: 배수 d: 시계, 반시계 k: 회전 수
        print(board)
        for num in range(1,N+1):
            if num % x == 0:
                rotate(board,num-1,d,k)

        remove(board)
    return cal(board)







print(solution(board,comm))








#####################################################

print('time', time.time_ns() - ptime)

