import sys
import time

prev_time = time.time_ns()
# sys.stdin = open('input.txt','r')
read = sys.stdin.readline


def solution():
    tetro1 = [[1, 1, 1, 1]] # 회전
    tetro2 = [[1, 1], [1, 1]]
    tetro3 = [[1, 0], [1, 0], [1, 1]] # 회전, 대칭
    tetro4 = [[1, 0], [1, 1], [0, 1]] # 회전, 대칭
    tetro5 = [[1, 1, 1], [0, 1, 0]] # 회전

    maxScore = []
    maxScore.append(getMaxScore(tetro1))
    maxScore.append(getMaxScore(rotateTetro(tetro1)))
    
    maxScore.append(getMaxScore(tetro2))
    
    maxScore.append(getMaxScore(tetro3))
    rot_tetro3 = rotateTetro(tetro3)
    maxScore.append(getMaxScore(rot_tetro3))
    rot_tetro3 = rotateTetro(tetro3)
    maxScore.append(getMaxScore(rot_tetro3))
    rot_tetro3 = rotateTetro(tetro3)
    maxScore.append(getMaxScore(rot_tetro3))
    
    sym_tetro3 = symTetro(tetro3)
    maxScore.append(getMaxScore(sym_tetro3))
    sym_rot_tetro3 = rotateTetro(tetro3)
    maxScore.append(getMaxScore(sym_rot_tetro3))
    sym_rot_tetro3 = rotateTetro(tetro3)
    maxScore.append(getMaxScore(sym_rot_tetro3))
    sym_rot_tetro3 = rotateTetro(tetro3)
    maxScore.append(getMaxScore(sym_rot_tetro3))

    maxScore.append(getMaxScore(tetro4))
    rot_tetro4 = rotateTetro(tetro4)
    maxScore.append(getMaxScore(rot_tetro4))
    rot_tetro4 = rotateTetro(tetro4)
    maxScore.append(getMaxScore(rot_tetro4))
    rot_tetro4 = rotateTetro(tetro4)
    maxScore.append(getMaxScore(rot_tetro4))

    sym_tetro4 = symTetro(tetro4)
    maxScore.append(getMaxScore(sym_tetro4))
    sym_rot_tetro4 = rotateTetro(tetro4)
    maxScore.append(getMaxScore(sym_rot_tetro4))
    sym_rot_tetro4 = rotateTetro(tetro4)
    maxScore.append(getMaxScore(sym_rot_tetro4))
    sym_rot_tetro4 = rotateTetro(tetro4)
    maxScore.append(getMaxScore(sym_rot_tetro4))
    
    maxScore.append(getMaxScore(tetro5))
    rot_tetro5 = rotateTetro(tetro5)
    maxScore.append(getMaxScore(rot_tetro5))
    rot_tetro5 = rotateTetro(tetro5)
    maxScore.append(getMaxScore(rot_tetro5))
    rot_tetro5 = rotateTetro(tetro5)
    maxScore.append(getMaxScore(rot_tetro5))
    
    return(max(maxScore))
    
    
    
def getMaxScore(tetro):
    len_r = len(tetro)
    len_c = len(tetro[0])

    max_sum = 0
    for i in range(N):
        for j in range(M):
            sum = 0
            if not checkStatus(i + len_r - 1, j + len_c - 1):
                continue
            for r in range(len_r):
                for c in range(len_c):
                    if tetro[r][c] == 1:
                        sum += _map[i + r][j + c]
            if sum > max_sum:
                max_sum = sum

    return max_sum


def checkStatus(i,j):
    return i >= 0 and i < N and j >= 0 and j < M


def rotateTetro(tetro):
    len_r = len(tetro)
    len_c = len(tetro[0])

    rot_tetro = []
    temp_tet = tetro[::-1]
    for j in range(len_c):
        temp = []
        for i in range(len_r):
            temp.append(temp_tet[i][j])
        rot_tetro.append(temp)

    return rot_tetro


def symTetro(tetro):
    len_r = len(tetro)

    sym_tetro = []
    for i in range(len_r):
        sym_tetro.append(tetro[i][::-1])

    return sym_tetro


def printTetro(tetro):
    len_r = len(tetro)
    len_c = len(tetro[0])
    for i in range(len_r):
        for j in range(len_c):
            print(tetro[i][j],end='')
        print()
    print()



N,M=map(int,read().strip().split())
_map = []
for _ in range(N):
    _map.append(list(map(int,read().strip().split())))

print(solution())

# print('time',time.time_ns()-prev_time)









