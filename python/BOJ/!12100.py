import sys
import time

sys.stdin = open('input.txt','r')
prev_time = time.time_ns()


di = [-1,1,0,0]
dj = [0,0,-1,1]

def solution(_map):


    cnt = 0
    que = []
    que.append([_map,cnt])

    while len(que) != 0:
        node = que.pop(0)
        node_map = node[0]
        node_cnt = node[1]

        que.append()


def move(dir, node_map):
    new_map = [[0 for _ in range(N)] for _ in range(N)]

    if dir == 'up':
        d = 0
        base_line = node_map[0]

        for i in range(N):
            line = []
            for j in range(N):
                if node_map[j][i] != 0:
                    line.append(node_map[j][i])

            for l in range(len(line)-1):
                curr_num = line[l]
                next_num = line[l+1]
                if curr_num == next_num:
                    line[l] *= 2
                    line[l + 1] = 0

            for j in range(N):
                if line[i] != 0:
                    line.append(node_map[j][i])








    elif dir == 'down':
        d = 1
    elif dir == 'left':
        d = 2
    elif dir == 'right':
        d = 3





def print_map(_map):
    for i in range(N):
        for j in range(N):
            print(_map[i][j],end='')
        print()
    print()


def checkStatus(i,j):
    return i < N and i >= 0 and j < N and j >= 0





_map = []
N = int(sys.stdin.readline().strip())
for _ in range(N):
    _map.append(list(map(int,sys.stdin.readline().strip().split())))


print(solution(_map))
print('time',time.time_ns()-prev_time)






