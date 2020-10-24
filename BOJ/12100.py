
import time

prev_time = time.time_ns()



import copy
import sys
# sys.stdin = open('input.txt','r')
read = sys.stdin.readline


N = int(read().strip())
mp = [list(map(int,read().strip().split())) for _ in range(N)]
# print(mp)


def printMap(mp):
    print('printMap')
    for i in range(len(mp)):
        for j in range(len(mp)):
            print(mp[i][j], end=' ')
        print()

def getMaxNum(mp):
    max = -1
    for i in range(len(mp)):
        for j in range(len(mp)):
            if mp[i][j] > max:
                max = mp[i][j]
    return max


# 북 동 남 서
def tilting(mp, dir):
    di = [[]]
    dj = [[]]
    if dir == 0:
        di = [[d for d in range(len(mp))] for _ in range(len(mp))]
        dj = [[d for _ in range(len(mp))] for d in range(len(mp))]
    elif dir == 1:
        di = [[d for _ in range(len(mp))] for d in range(len(mp))]
        dj = [[d for d in range(len(mp) - 1, -1, -1)] for _ in range(len(mp))]
    elif dir == 2:
        di = [[d for d in range(len(mp) - 1, -1, -1)] for _ in range(len(mp))]
        dj = [[d for _ in range(len(mp))] for d in range(len(mp))]
    elif dir == 3:
        di = [[d for _ in range(len(mp))] for d in range(len(mp))]
        dj = [[d for d in range(len(mp))] for _ in range(len(mp))]

    new_mp = [[0 for _ in range(len(mp))] for _ in range(len(mp))]
    li = [[]] * len(mp)
    # print('li',li)
    for i in range(len(mp)):
        new_li = []
        for j in range(len(mp)):
            if mp[di[i][j]][dj[i][j]] != 0:
                new_li.append(mp[di[i][j]][dj[i][j]])
        new_li += [0]
        add_li = []
        prev_num = 0

        idx = 0
        while idx+1 < len(new_li):
            if new_li[idx] == new_li[idx+1]:
                add_li.append(new_li[idx] * 2)
                idx += 2
            else:
                add_li.append(new_li[idx])
                idx += 1
        while len(add_li) < len(mp):
            add_li.append(0)
        # print('add_li', add_li)
        li[i] = add_li

    for i in range(len(mp)):
        for j in range(len(mp)):
            new_mp[di[i][j]][dj[i][j]] = li[i][j]

    return new_mp

def solution(mp):
    max_num = 0
    que = [[copy.deepcopy(mp),0]]
    while que:
        cur_mp, cnt = que.pop()
        # print('cur_mp',cur_mp,'cnt',cnt)
        if cnt == 5:
            max_num = max(getMaxNum(cur_mp), max_num)
            continue
        # print('max_num',max_num)

        for i in range(4):
            new_mp = tilting(copy.deepcopy(cur_mp), i)
            # printMap(new_mp)
            que.append([new_mp, cnt + 1])
    return max_num


print(solution(mp))
# printMap(tilting(tilting(mp,3),3))





print('time',time.time_ns()-prev_time)




