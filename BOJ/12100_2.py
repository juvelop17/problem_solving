import sys
import time

ptime = time.time_ns()

sys.stdin = open('input.txt', 'r')


#####################################################

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end='\t')
        print()

def find_max_num(board):
    max_num = -1
    for i in range(N):
        for j in range(N):
            max_num = max(max_num, board[i][j])
    return max_num

def tilt_board(board, dir, cnt):
    if cnt == 5:
        global max_num
        max_num = max(max_num, find_max_num(board))
        return

    n = len(board)
    new_board = [[0 for _ in range(n)] for _ in range(n)]
    di = [[]]
    dj = [[]]
    if dir == 0:
        di = [[j for j in range(n)] for i in range(n)]
        dj = [[i for j in range(n)] for i in range(n)]
    elif dir == 1:
        di = [[i for j in range(n)] for i in range(n)]
        dj = [[j for j in range(n-1,-1,-1)] for i in range(n)]
    elif dir == 2:
        di = [[j for j in range(n-1,-1,-1)] for i in range(n)]
        dj = [[i for j in range(n)] for i in range(n)]
    elif dir == 3:
        di = [[i for j in range(n)] for i in range(n)]
        dj = [[j for j in range(n)] for i in range(n)]

    for i in range(n):
        nums = []
        new_nums = []

        for j in range(n):
            if board[di[i][j]][dj[i][j]] != 0:
                nums.append(board[di[i][j]][dj[i][j]])

        j = 0
        while j < len(nums):
            if j + 1 < len(nums) and nums[j] == nums[j+1]:
                new_nums.append(nums[j] * 2)
                j += 1
            else:
                new_nums.append(nums[j])
            j += 1

        new_nums += [0] * (n - len(new_nums))

        for j in range(n):
            new_board[di[i][j]][dj[i][j]] = new_nums[j]

    for d in range(4):
        tilt_board(new_board,d,cnt+1)

def solution(N, board):
    global max_num
    max_num= -1

    for d in range(4):
        tilt_board(board, d, 0)

    return max_num

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
print(solution(N, board))

#####################################################



print('time', (time.time_ns() - ptime)/10**6,'ms')





