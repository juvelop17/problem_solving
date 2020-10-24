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
        sum_list = []
        cnt = 0
        for i in range(N):
            for j in range(N):
                if memory_map[i][j] == 0:
                    cnt += 1
                    pick = []
                    sum = explore(memory_map, i, j, cnt, pick)
                    pick_list.append(pick)
                    sum_list.append(sum)
        # printMap(memory_map)

        for i in range(len(pick_list)):
            val = sum_list[i]//len(pick_list[i])
            for pi in pick_list[i]:
                country_map[pi[0]][pi[1]] = val

        # printMap(country_map)
        if cnt != N*N:
            is_succ = True

    return total_cnt


def explore(memory_map,i,j,n,pick):
    que = []
    que.append([i, j])
    sum = 0
    while len(que) > 0:
        node = que.pop(0)
        node_i = node[0]
        node_j = node[1]
        memory_map[node_i][node_j] = n
        pick.append([node_i, node_j])
        sum+=country_map[node_i][node_j]

        for d in range(4):
            new_i = node_i+di[d]
            new_j = node_j+dj[d]
            if checkRange(new_i,new_j) and checkLR(node_i,node_j,new_i,new_j) and memory_map[new_i][new_j] == 0:
                memory_map[new_i][new_j] = n
                que.append([new_i, new_j])

    return sum


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
print('time',time.time_ns()-prev_time)

