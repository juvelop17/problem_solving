
import sys
import time

ptime = time.time_ns()

sys.stdin = open('boggle.in', 'r')
sys.stdout = open('boggle.res', 'w')


#####################################################

di = [-1,-1,-1,0,1,1,1,0]
dj = [-1,0,1,1,1,0,-1,-1]

def checkRange(i, j):
    return i >= 0 and i < 5 and j >= 0 and j < 5

def find(board, fail_board, word, ci, cj, cidx):
    # print('ci, cj, cidx',ci, cj, cidx)
    if cidx == len(word) - 1:
        return True
    for d in range(8):
        ni = ci + di[d]
        nj = cj + dj[d]
        nidx = cidx + 1
        if checkRange(ni, nj) and word[nidx] == board[ni][nj] and fail_board[nidx][ni][nj] == 0:
            if find(board, fail_board, word, ni, nj, nidx):
                return True
    fail_board[cidx][ci][cj] = 1
    return False

def solution(board, word_list):
    for word in word_list:
        starting_point = []
        for i in range(5):
            for j in range(5):
                if board[i][j] == word[0]:
                    starting_point.append((i, j))
        res = False
        for point in starting_point:
            fail_board = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(10)]
            res = find(board, fail_board, word, *point, 0)
            if res:
                break
        if res:
            print(word, "YES")
        else:
            print(word, "NO")
    return

t = int(input())
for tt in range(t):
    board = []
    for _ in range(5):
        board.append(list(input()))
    n = int(input())
    word_list = []
    for _ in range(n):
        word_list.append(input().strip())
    solution(board, word_list)

#####################################################










