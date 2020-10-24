import time
import sys

prev_time = time.time_ns()
sys.stdin = open('input.txt','r')
read = sys.stdin.readline

# 윗 면은 흰색, 아랫 면은 노란색, 앞 면은 빨간색, 뒷 면은 오렌지색, 왼쪽 면은 초록색, 오른쪽 면은 파란색
# 입력
# U: 윗 면, D: 아랫 면, F: 앞 면, B: 뒷 면, L: 왼쪽 면, R: 오른쪽 면
# +인 경우에는 시계 방향 (그 면을 바라봤을 때가 기준), -인 경우에는 반시계 방향
# 출력
# 흰색은 w, 노란색은 y, 빨간색은 r, 오렌지색은 o, 초록색은 g, 파란색은 b

# U 시계 : F L B R
# D 시계 : 역순
# F 시계 : U R D L
# B 시계 : 역순
# R 시계 : U B D F
# L 시계 : 역순

def solution():

    for tc in T:
        num = tc[0]
        method = tc[1]
        for i in range(num):
            sel = method[i][0]
            rot = method[i][1]


def rotate(sel,rot):
    if sel == 'U':
        temp = [F[0][:],L[0][:],B[0][:],R[0][:]]
        if rot == '+':
            F[0] = temp[3]
            L[0] = temp[0]
            B[0] = temp[1]
            R[0] = temp[2]
        if rot == '-':
            F[0] = temp[1]
            L[0] = temp[2]
            B[0] = temp[3]
            R[0] = temp[0]
    elif sel == 'D':
        temp = [F[2][:], L[2][:], B[2][:], R[2][:]]
        if rot == '+':
            F[2] = temp[1]
            L[2] = temp[2]
            B[2] = temp[3]
            R[2] = temp[0]
        if rot == '-':
            F[2] = temp[3]
            L[2] = temp[0]
            B[2] = temp[1]
            R[2] = temp[2]
    elif sel == 'F':
        temp = [U[0][:], [R[2][0],R[1][0],R[0][0]], D[0][:], [L[0][2],L[1][2],L[2][2]]]
        if rot == '+':
            U[0][0] = temp[3][0]
            U[0][1] = temp[3][1]
            U[0][2] = temp[3][2]
            R[2][0] = temp[0][0]
            R[1][0] = temp[0][1]
            R[0][0] = temp[0][2]
            D[0][0] = temp[1][0]
            D[0][1] = temp[1][1]
            D[0][2] = temp[1][2]
            L[0][0] = temp[2][0]
            L[1][0] = temp[2][1]
            L[2][0] = temp[2][2]
        if rot == '-':
            U[0][0] = temp[1][0]
            U[0][1] = temp[1][1]
            U[0][2] = temp[1][2]
            R[2][0] = temp[2][0]
            R[1][0] = temp[2][1]
            R[0][0] = temp[2][2]
            D[0][0] = temp[3][0]
            D[0][1] = temp[3][1]
            D[0][2] = temp[3][2]
            L[0][0] = temp[0][0]
            L[1][0] = temp[0][1]
            L[2][0] = temp[0][2]
    elif sel == 'B':
        temp = [U[2][:], [R[0][2],R[1][2],R[2][2]], D[0][:], [L[2][0],L[1][0],L[0][0]]]
        if rot == '+':
            U[0][0] = temp[1][0]
            U[0][1] = temp[1][1]
            U[0][2] = temp[1][2]
            R[0][0] = temp[2][0]
            R[1][0] = temp[2][1]
            R[2][0] = temp[2][2]
            D[0][0] = temp[3][0]
            D[0][1] = temp[3][1]
            D[0][2] = temp[3][2]
            L[2][0] = temp[0][0]
            L[1][0] = temp[0][1]
            L[0][0] = temp[0][2]
        if rot == '-':
            U[0][0] = temp[3][0]
            U[0][1] = temp[3][1]
            U[0][2] = temp[3][2]
            R[0][0] = temp[0][0]
            R[1][0] = temp[0][1]
            R[2][0] = temp[0][2]
            D[0][0] = temp[1][0]
            D[0][1] = temp[1][1]
            D[0][2] = temp[1][2]
            L[2][0] = temp[2][0]
            L[1][0] = temp[2][1]
            L[0][0] = temp[2][2]
    elif sel == 'R':
        temp = [[U[0][0],U[1][0],U[2][0], [B[0][0],B[1][0],B[2][0]], D[0][:], [F[2][0],F[1][0],F[0][0]]]
        if rot == '+':
            U[0][0] = temp[1][0]
            U[0][1] = temp[1][1]
            U[0][2] = temp[1][2]
            B[0][0] = temp[2][0]
            B[1][0] = temp[2][1]
            B[2][0] = temp[2][2]
            D[0][0] = temp[3][0]
            D[0][1] = temp[3][1]
            D[0][2] = temp[3][2]
            F[2][0] = temp[0][0]
            F[1][0] = temp[0][1]
            F[0][0] = temp[0][2]
        if rot == '-':
            U[0][0] = temp[3][0]
            U[0][1] = temp[3][1]
            U[0][2] = temp[3][2]
            R[0][0] = temp[0][0]
            R[1][0] = temp[0][1]
            R[2][0] = temp[0][2]
            D[0][0] = temp[1][0]
            D[0][1] = temp[1][1]
            D[0][2] = temp[1][2]
            L[2][0] = temp[2][0]
            L[1][0] = temp[2][1]
            L[0][0] = temp[2][2]


N = int(read().strip())
T = []
for _ in range(N):
    T.append([int(read().strip()),read().strip().split()])
# print(T)

U = [['w' for _ in range(3) ] for _ in range(3)]
D = [['y' for _ in range(3) ] for _ in range(3)]
F = [['r' for _ in range(3) ] for _ in range(3)]
B = [['o' for _ in range(3) ] for _ in range(3)]
L = [['g' for _ in range(3) ] for _ in range(3)]
R = [['b' for _ in range(3) ] for _ in range(3)]

print(solution())
print('time',time.time_ns()-prev_time)


