import sys
import time
import heapq

prev_time = time.time_ns()
# sys.stdin = open('input.txt','r')
read = sys.stdin.readline

# 가장 처음에 양분은 모든 칸에 5
#
# 봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다.
# 각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다.
# 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다.
# 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
#
# 여름에는 봄에 죽은 나무가 양분으로 변하게 된다.
# 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다.
# 소수점 아래는 버린다.
#
# 가을에는 나무가 번식한다.
# 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
# 어떤 칸 (r, c)와 인접한 칸은
# (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다.
# 상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.
#
# 겨울에는 S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다.
# 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.


def solution():
    cnt = 0
    while cnt < K:
        cnt += 1
        spring()
        summer()
        autumn()
        winter()

    # print(M_list)
    return len(M_list)


def spring():
    while M_list:
        m = M_list.pop()
        heapq.heappush(pque,(m[2],m))

    while pque:
        node = heapq.heappop(pque)[1]
        val = base_map[node[0]][node[1]] - node[2]
        if val < 0:
            dead.append(node)
        else:
            base_map[node[0]][node[1]] -= node[2]
            M_list.append([node[0],node[1],node[2]+1])

def summer():
    while dead:
        d = dead.pop()
        base_map[d[0]][d[1]] += d[2]


def autumn():
    for m in M_list:
        if m[2] % 5 == 0:
            for i in range(8):
                new_r = m[0] + dr[i]
                new_c = m[1] + dc[i]
                if 0<=new_r<N and 0<=new_c<N:
                    M_list.append([new_r,new_c,1])


def winter():
    for i in range(N):
        for j in range(N):
            base_map[i][j] += A[i][j]


dr = [-1,-1,-1,0,0,1,1,1]
dc = [-1,0,1,-1,1,-1,0,1]


N,M,K = map(int,read().strip().split())
A = [list(map(int,read().strip().split())) for _ in range(N)]
# M_list = [list(map(int,read().strip().split())) for _ in range(M)]
M_list = []
for _ in range(M):
    t = list(map(int,read().strip().split()))
    M_list.append([t[0]-1,t[1]-1,t[2]])

pque = []
dead = []

base_map = [[5 for _ in range(N)] for _ in range(N)]
memory_map = [[0 for _ in range(N)] for _ in range(N)]

print(solution())
# print('time',time.time_ns()-prev_time)

