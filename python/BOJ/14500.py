import sys
import time

prev_time = time.time_ns()
# sys.stdin = open('input.txt','r')
read = sys.stdin.readline


def solution():
    tetro1 = [[[1, 1, 1, 1]],[[1],[1],[1],[1]]]  # 회전
    tetro2 = [[1, 1], [1, 1]]
    tetro3 = [[[1, 1], [1, 0], [1, 0]], [[1, 1], [0, 1], [0, 1]],
              [[1, 0], [1, 0], [1, 1]], [[0, 1], [0, 1], [1, 1]],
              [[1, 0], [1, 1], [1, 0]], [[0, 1], [1, 1], [0, 1]],
              [[1, 0], [1, 1], [0, 1]], [[0, 1], [1, 1], [1, 0]]]
    tetro4 = [[[1, 1, 1], [0, 0, 1]],[[1, 1, 1], [1, 0, 0]],
              [[0, 0, 1], [1, 1, 1]],[[1, 0, 0], [1, 1, 1]],
              [[1, 1, 1], [0, 1, 0]],[[0, 1, 0], [1, 1, 1]],
              [[0, 1, 1], [1, 1, 0]],[[1, 1, 0], [0, 1, 1]]]

    maxScore = []
    for t in tetro1:
        maxScore.append(getMaxScore(t))
    maxScore.append(getMaxScore(tetro2))
    for t in tetro3:
        maxScore.append(getMaxScore(t))
    for t in tetro4:
        maxScore.append(getMaxScore(t))

    return (max(maxScore))


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


def checkStatus(i, j):
    return i >= 0 and i < N and j >= 0 and j < M


def printTetro(tetro):
    len_r = len(tetro)
    len_c = len(tetro[0])
    for i in range(len_r):
        for j in range(len_c):
            print(tetro[i][j], end='')
        print()
    print()


N, M = map(int, read().strip().split())
_map = []
for _ in range(N):
    _map.append(list(map(int, read().strip().split())))

print(solution())

# print('time',time.time_ns()-prev_time)









