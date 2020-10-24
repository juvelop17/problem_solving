import sys
import time


prev_time = time.time_ns()
sys.stdin = open('input.txt','r')
read = sys.stdin.readline

def solution():
    is_succ = True
    total_cnt = -1
    while is_succ:
        total_cnt += 1
        is_succ = False
        memory_map = [[0 for _ in range(N)] for _ in range(N)]

        pick_list = []
        cnt = 0
        for i in range(N):
            for j in range(N):
                if memory_map[i][j] == 0:
                    cnt += 1
                    pick = []
                    explore(memory_map, i, j, cnt, pick)
                    pick_list.append(pick)
        # printMap(memory_map)

        for pi in pick_list:
            sum = 0
            for p in pi:
                sum+=country_map[p[0]][p[1]]
            sum //= len(pi)
            for p in pi:
                country_map[p[0]][p[1]] = sum

        # printMap(country_map)
        if cnt != N*N:
            is_succ = True

    return total_cnt


def explore(memory_map,i,j,n,pick):
    memory_map[i][j] = n
    pick.append([i,j])

    for d in range(4):
        new_i = i+di[d]
        new_j = j+dj[d]
        if checkRange(new_i,new_j) and checkLR(i,j,new_i,new_j) and memory_map[new_i][new_j] == 0:
            explore(memory_map,new_i,new_j,n,pick)


def checkRange(i,j):
    return i>=0 and i<N and j>=0 and j<N


def checkLR(i,j,new_i,new_j):
    return L <= abs(country_map[i][j] - country_map[new_i][new_j]) <= R


def printMap(memory_map):
    for i in range(N):
        for j in range(N):
            print(memory_map[i][j],end=' ')
        print()
    print()


di=[-1,1,0,0]
dj=[0,0,-1,1]

N,L,R = map(int,read().strip().split())
country_map = [list(map(int,read().strip().split())) for _ in range(N)]


print(solution())
# print('time',time.time_ns()-prev_time)

