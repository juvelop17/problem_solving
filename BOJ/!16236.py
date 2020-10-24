import sys
import time
import heapq

prev_time = time.time_ns()
# sys.stdin = open('input1.txt','r')
read = sys.stdin.readline

# 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다.
# 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.
# 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.

# 아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.
#
# 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
# 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기,
# 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.


def solution():
    shark_ij = findShark()
    cnt = 0
    food_cnt = 0
    size = 2
    is_update = True
    while is_update:
        node = find(shark_ij[0],shark_ij[1],size)
        if node == None:
            break

        node_i = node[0]
        node_j = node[1]

        base_map[shark_ij[0]][shark_ij[1]] = 0
        shark_ij = [node_i,node_j]
        base_map[shark_ij[0]][shark_ij[1]] = 9

        node_cnt = node[2]
        cnt += node_cnt

        food_cnt += 1
        if food_cnt == size:
            if size < 8:
                size += 1
            food_cnt = 0

        # print(cnt)
        # printMap()
    return cnt


def find(i,j,size):
    memory_map = [[0 for _ in range(N)] for _ in range(N)]
    memory_map[i][j] = 1
    que = []
    heapq.heappush(que,(0,i,j))
    while que:
        node = heapq.heappop(que)
        node_cnt = node[0]
        node_i = node[1]
        node_j = node[2]

        if 0 < base_map[node_i][node_j] < size:
            return [node_i,node_j,node_cnt]

        for d in range(4):
            new_i = node_i + di[d]
            new_j = node_j + dj[d]
            if 0 <= new_i < N and 0 <= new_j < N and memory_map[new_i][new_j] == 0 and base_map[new_i][new_j] <= size:
                memory_map[new_i][new_j] = 1
                heapq.heappush(que, (node_cnt+1,new_i,new_j))


def findShark():
    for i in range(N):
        for j in range(N):
            if base_map[i][j] == 9:
                return [i,j]

def printMap():
    for i in range(N):
        for j in range(N):
            print(base_map[i][j],end='')
        print()
    print()



di = [-1,0,0,1]
dj = [0,-1,1,0]

N = int(read().strip())
base_map = [list(map(int,read().strip().split())) for _ in range(N)]

print(solution())
# print('time',time.time_ns()-prev_time)









