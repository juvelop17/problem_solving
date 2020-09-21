import sys
import time


prev_time = time.time_ns()
# sys.stdin = open('input1.txt','r')


di = [-1,1,0,0]
dj = [0,0,-1,1]

def solution():
    res = True

    head = [0,0]
    length = 1
    cur_dir = 'r'
    _map[0][0] = 1

    sum_cnt = 0
    for node in L_list:
        sec = node[0]
        dir = node[1]

        while sum_cnt < sec:
            sum_cnt += 1
            head, length, res = move(head, length, cur_dir)
            # print(sum_cnt)
            # printMap()

            if res == False:
                return sum_cnt

        if cur_dir == 'u':
            if dir == 'L': # 왼
                cur_dir = 'l'
            elif dir == 'D': # 오
                cur_dir = 'r'
        elif cur_dir == 'd':
            if dir == 'L': # 왼
                cur_dir = 'r'
            elif dir == 'D': # 오
                cur_dir = 'l'
        elif cur_dir == 'l':
            if dir == 'L': # 왼
                cur_dir = 'd'
            elif dir == 'D': # 오
                cur_dir = 'u'
        elif cur_dir == 'r':
            if dir == 'L': # 왼
                cur_dir = 'u'
            elif dir == 'D': # 오
                cur_dir = 'd'

    while res:
        sum_cnt += 1
        head, length, res = move(head, length, cur_dir)
        # print(sum_cnt)
        # printMap()

    return sum_cnt


def move(head,length,cur_dir):
    isEat = False
    res = False

    if cur_dir == 'u':
        dir = 0
    elif cur_dir == 'd':
        dir = 1
    elif cur_dir == 'l':
        dir = 2
    else:
        dir = 3

    new_pos = [head[0] + di[dir], head[1] + dj[dir]]
    if not checkStatus(new_pos[0], new_pos[1]):
        return head, length, res
    new_head = [new_pos[0], new_pos[1]]
    _map[new_head[0]][new_head[1]] = 1

    if new_head in K_list:
        isEat = True
        K_list.remove(new_head)
        length += 1

    curr_pos = [head[0], head[1]]
    if length >= 2:
        cnt = 1
        while(cnt <= length):
            cnt += 1
            prev_pos = [curr_pos[0], curr_pos[1]]
            for i in range(4):
                new_pos = [prev_pos[0]+di[i],prev_pos[1]+dj[i]]
                if checkRange(new_pos[0],new_pos[1]) and _map[new_pos[0]][new_pos[1]] == cnt:
                    curr_pos = [new_pos[0],new_pos[1]]
                    break

            _map[prev_pos[0]][prev_pos[1]] = cnt

    if isEat:
        _map[curr_pos[0]][curr_pos[1]] = length
    else:
        _map[curr_pos[0]][curr_pos[1]] = 0

    res = True
    return new_head, length, res


def checkStatus(i,j):
    if checkRange(i,j):
        if _map[i][j] == 0:
            return True
    return False

def checkRange(i,j):
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
    pos = list(map(int, sys.stdin.readline().strip().split()))
    K_list.append([pos[0] - 1, pos[1] - 1])

L = int(sys.stdin.readline().strip())
L_list = []
for _ in range(L):
    l = sys.stdin.readline().strip().split()
    L_list.append([int(l[0]), l[1]])

_map = [[0 for _ in range(N)] for _ in range(N)]
print(solution())










