import sys
import time

ptime = time.time_ns()

sys.stdin = open('input.txt', 'r')


#####################################################

def paint(square, a, b, c, d, U, R, D, L):
    val = [U, R, D, L]
    for i,x in enumerate((a, b, c, d)):
        if x == 0:
            square[i][1] = val[i]
        elif x == 1:
            square[i][0] = 1
            square[i][1] = val[i] - 1
        elif x == 2:
            square[i][2] = 1
            square[i][1] = val[i] - 1
        elif x == 3:
            square[i][0] = 1
            square[i][1] = val[i] - 2
            square[i][2] = 1
    return square

def verify(n, square):
    res = True
    for i in range(4):
        if square[i][2] != square[(i+1) % 4][0]:
            res = False
        if square[i][1] < 0 or square[i][1] > n-2:
            res = False
    return res

def solution(n, U, R, D, L):
    # print(n, U, R, D, L)
    res = []
    ans = False

    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    square = [[0 for _ in range(3)] for _ in range(4)]
                    res.append(paint(square,a,b,c,d,U, R, D, L))

    for square in res:
        if verify(n, square):
            ans = True
            # print(square)

    return 'YES' if ans else 'NO'

t = int(input())
for tt in range(t):
    n, U, R, D, L = map(int, input().split())
    print(solution(n, U, R, D, L))

#####################################################



print('time', (time.time_ns() - ptime)/10**6,'ms')
