import sys
import time


prev_time = time.time_ns()
sys.stdin = open('input.txt','r')






di = [-1,1,0,0]
dj = [0,0,-1,1]



def solution():
    head = [0,0]
    length = 1
    cur_dir = 'u'
    _map[0][0] = 1

    printMap()
    head = move(head, length, cur_dir)
    head = move(head, length, cur_dir)
    head = move(head, length, cur_dir)
    printMap()

    # for node in L_list:
    #     sec = node[0]
    #     dir = node[1]
    #
    #     cnt = 0
    #     while cnt < sec:
    #         move(head,length,cur_dir)
    #         cnt += 1


def move(head,length,cur_dir):
    if cur_dir == 'u':
        dir = 0
    elif cur_dir == 'd':
        dir = 1
    elif cur_dir == 'l':
        dir = 2
    else:
        dir = 3

    new_head = [head[0]+di[dir],head[1]+dj[dir]]
    _map[new_head[0]][new_head[1]] = 1

    curr_pos = [head[0],head[1]]
    if length >= 2:
        cnt = 1
        while(cnt <= length):
            cnt += 1
            prev_pos = [curr_pos[0], curr_pos[1]]
            for i in range(4):
                new_pos = [prev_pos[0]+di[i],prev_pos[1]+dj[i]]
                if _map[new_pos[0]][new_pos[1]] == cnt:
                    curr_pos = [new_pos[0],new_pos[1]]
                    break

            _map[prev_pos[0]][prev_pos[1]] = cnt

    _map[curr_pos[0]][curr_pos[1]] = 0

    return new_head


def checkStatus(i,j):
    return i >= 0 and i < N and j >= 0 and j < N


def printMap():
    for i in range(N):
        for j in range(N):
            print(_map[i][j],end='')
        print()
    print()


N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())
K_list = []
for _ in range(K):
    K_list.append(list(map(int, sys.stdin.readline().strip().split())))

L = int(sys.stdin.readline().strip())
L_list = []
for _ in range(K):
    l = sys.stdin.readline().strip().split()
    L_list.append([int(l[0]),l[1]])

_map = [[0 for _ in range(N)] for _ in range(N)]

print(solution())









