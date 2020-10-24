import sys
import time


start_time = time.time_ns()
sys.stdin = open('input.txt', 'r')


# # return : 최대 reward
# def score(c, status):
#     # print(score_memory)
#     # if score_memory[status][c] != -1:
#     #     return score_memory[status][c]
#     if c == n:
#         return 0
#
#     res = score(c+1,0)
#     if status != 1:
#         res = max(res, score(c + 1, 1) + score_board[0][c])
#     if status != 2:
#         res = max(res, score(c + 1, 2) + score_board[1][c])
#
#     score_memory[status][c] = res
#     return res
#
# T = int(sys.stdin.readline())
#
# for i in range(T):
#     n = int(sys.stdin.readline())
#     l1 = list(map(int, sys.stdin.readline().strip().split()))
#     l2 = list(map(int, sys.stdin.readline().strip().split()))
#     score_board = [l1] + [l2]
#     score_memory = [[-1 for _ in range(n+1)] for __ in range(3)]
#     print(score(0, 0))
#     # print(score_memory)

###################################################################

# return : 최대 reward
def score(c, status):
    for i in range(0,n):
        score_memory[0][i+1]= max(score_memory[0][i],score_memory[1][i],score_memory[2][i])
        score_memory[1][i+1]= max(score_memory[0][i]+score_board[0][i],score_memory[2][i]+score_board[0][i])
        score_memory[2][i+1]= max(score_memory[0][i]+score_board[1][i],score_memory[1][i]+score_board[1][i])
    # print(score_memory)

    _max = -1
    for r in score_memory:
        _max_r = max(r)
        if _max_r > _max:
            _max = _max_r

    return _max


T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    l1 = list(map(int, sys.stdin.readline().strip().split()))
    l2 = list(map(int, sys.stdin.readline().strip().split()))
    score_board = [l1] + [l2]
    score_memory = [[0 for _ in range(n+1)] for __ in range(3)]
    print(score(0, 0))
    # print(score_memory)

# end_time = time.time_ns()
# print('time',end_time-start_time)