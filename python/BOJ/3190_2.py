

import time

prev_time = time.time_ns()


import sys
sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline




def solution(mp,K_pos,L_pos):
    # 북 동 남 서
    di = [-1,0,1,0]
    dj = [0,1,0,-1]

    time_cnt = 0
    status = True
    cur_dir = 1
    snake_dir = [1]
    cur_head = [1,1] # x,y
    cur_tail = [1,1]
    while status:
        time_cnt += 1
        new_head = [cur_head[0]+di[cur_dir],cur_head[1]+dj[cur_dir]]

        if not checkRange(new_head, len(mp)-1) : # 장외
            break

        # if mp[new_head[0]][new_head[1]] == 0: # 전진
        #     mp[new_head[0]][new_head[1]] = 1
        #     mp[cur_tail[0]][cur_tail[1]] = 0
        # elif mp[new_head[0]][new_head[1]] == 1: # 충돌
        #     break
        # elif mp[new_head[0]][new_head[1]] == 2: # 사과
        #     mp[new_head[0]][new_head[1]] = 1

        if mp[new_head[0]][new_head[1]] == 1: # 충돌
            break
        if mp[new_head[0]][new_head[1]] == 0: # 전진
            mp[cur_tail[0]][cur_tail[1]] = 0
            tail_dir = snake_dir.pop(0)
            cur_tail = [cur_tail[0] + di[tail_dir], cur_tail[1] + dj[tail_dir]]
        mp[new_head[0]][new_head[1]] = 1
        cur_head = new_head

        if len(L_pos):
            cur_L = L_pos[0]
            if cur_L[0] == time_cnt:
                L_pos.pop(0)
                if cur_L[1] == 'L':
                    cur_dir = (cur_dir - 1) % 4
                elif cur_L[1] == 'D':
                    cur_dir = (cur_dir + 1) % 4
        snake_dir.append(cur_dir)

        # print('time_cnt',time_cnt)
        # print('new_head',new_head)
        # print('cur_dir',cur_dir)
        # print('cur_tail',cur_tail)
        # print('snake_dir',snake_dir)
        # printMap(mp)

    return time_cnt


def checkRange(pos, N):
    return pos[0] <= N and pos[0] > 0 and pos[1] <= N and pos[1] > 0

def printMap(mp):
    for i in range(1,len(mp)):
        for j in range(1,len(mp)):
            print(mp[i][j], end=' ')
        print()


N = int(read().strip())
K = int(read().strip())
K_pos = [list(map(int, read().split())) for _ in range(K)]
L = int(read().strip())
L_pos = []
for _ in range(L):
    tmp = read().split()
    L_pos.append([int(tmp[0]),tmp[1]])


# 0행, 0열은 사용안함
# 1 : 몸체
# 2 : 사과
mp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for apple in K_pos:
    mp[apple[0]][apple[1]] = 2
mp[1][1] = 1

print(solution(mp,K_pos,L_pos))












