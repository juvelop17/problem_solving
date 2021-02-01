import sys
import time

ptime = time.time_ns()

sys.stdin = open('boardcover.in', 'r')


#####################################################

dij = [((0,0),(0,1),(1,1)), ((0,0),(0,1),(1,0)), ((0,0),(1,0),(1,1)), ((0,0),(1,-1),(1,0))]

def display_board(h, w, board):
    for i in range(h):
        for j in range(w):
            print(board[i][j], end='')
        print()
    print()

def checkRange(h, w, i, j):
    return i >= 0 and i < h and j >= 0 and j < w

def find(h, w, board):
    # display_board(h,w,board)
    ci = cj = -1
    for i in range(h):
        for j in range(w):
            if board[i][j] == '.':
                ci = i
                cj = j
                break
        if cj != -1:
            break
    if ci == -1 and cj == -1:
        return 1

    cnt = 0
    if board[ci][cj] == '.':
        for d in range(4):
            ok = True
            for dd in range(3):
                ni = ci + dij[d][dd][0]
                nj = cj + dij[d][dd][1]
                # print('ci,cj,h,w,ni,nj')
                # print(ci,cj,h,w,ni,nj)
                if not checkRange(h,w,ni,nj) or board[ni][nj] != '.':
                    ok = False
            if ok:
                for dd in range(3):
                    ni = ci + dij[d][dd][0]
                    nj = cj + dij[d][dd][1]
                    board[ni][nj] = '#'
                cnt += find(h, w, board)
                for dd in range(3):
                    ni = ci + dij[d][dd][0]
                    nj = cj + dij[d][dd][1]
                    board[ni][nj] = '.'
    return cnt

def solution(h, w, board):
    # print(board)

    return find(h, w, board)

t = int(input())
for tt in range(t):
    h, w = map(int, input().split())
    board = []
    for _ in range(h):
        board.append(list(input().strip()))
    print(solution(h, w, board))

#####################################################



print('time', time.time_ns() - ptime)

