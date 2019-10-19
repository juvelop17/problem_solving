import sys
import time


prev_time = time.time_ns()
# sys.stdin = open('input.txt','r')
read = sys.stdin.readline

di = [1,-1,0,0]
dj = [0,0,1,-1]

def solution():
    global memory_map

    max_val = 0

    for a in range(N*M):
        i1 = a // M
        j1 = a % M

        if _map[i1][j1] != 0:
            continue

        for b in range(a+1,N*M):
            i2 = b // M
            j2 = b % M

            if _map[i2][j2] != 0:
                continue

            for c in range(b+1,N*M):
                i3 = c // M
                j3 = c % M

                if _map[i3][j3] != 0:
                    continue

                # print(i1,j1,i2,j2,i3,j3)
                memory_map = [_map[row][:] for row in range(N)]
                memory_map[i1][j1] = 2
                memory_map[i2][j2] = 2
                memory_map[i3][j3] = 2

                for p in virus_list:
                    explore(p[0], p[1])
                max_val = max(max_val, getScore(memory_map))

    return max_val


def explore(i,j):
    global memory_map

    que = []
    que.append([i,j])

    while len(que) > 0:
        node = que.pop(0)
        node_i = node[0]
        node_j = node[1]

        for d in range(4):
            new_i = node_i+di[d]
            new_j = node_j+dj[d]
            if checkRange(new_i,new_j) and memory_map[new_i][new_j] == 0:
                que.append([new_i,new_j])
                memory_map[new_i][new_j] = 1

    return


def getScore(memory_map):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if _map[i][j] == 0 and memory_map[i][j] == 0:
                cnt += 1
    return cnt


def checkRange(i,j):
    return i >= 0 and i < N and j >= 0 and j < M


def printMap(__map):
    for i in range(N):
        for j in range(M):
            print(__map[i][j],end='')
        print()
    print()



N, M = map(int,read().strip().split())
_map = []
for _ in range(N):
    _map.append(list(map(int,read().strip().split())))

virus_list = []
for i in range(N):
    for j in range(M):
        if _map[i][j] == 2:
            virus_list.append([i,j])

memory_map = []


# print(virus_list)
print(solution())
# print('time',time.time_ns()-prev_time)


