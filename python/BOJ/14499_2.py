
import time

ptime = time.time_ns()




import sys

# sys.stdin = open('input.txt','r')
read = sys.stdin.readline

# 0 동 서 북 남
di = [0,0,0,-1,1]
dj = [0,1,-1,0,0]

def printDice(dice):
    print('\t'+str(dice[2]))
    print(str(dice[4])+'\t'+str(dice[1])+'\t'+str(dice[3]))
    print('\t'+str(dice[5]))
    print('\t'+str(dice[6]))

def printMap(mp):
    for i in range(len(mp)):
        for j in range(len(mp[0])):
            print(mp[i][j], end=' ')
        print()


def rotateDice(mp, dice, dir, new_pos):
    top_num = -1
    new_dice = dice[:]
    if dir == 1:
        i_li = [1,3,6,4]
        j_li = [4,1,3,6]
    elif dir == 2:
        i_li = [1,3,6,4]
        j_li = [3,6,4,1]
    elif dir == 3:
        i_li = [1,5,6,2]
        j_li = [5,6,2,1]
    elif dir == 4:
        i_li = [1,5,6,2]
        j_li = [2,1,5,6]

    for i, j in zip(i_li, j_li):
        new_dice[i] = dice[j]
    dice[:] = new_dice[:]

    if mp[new_pos[0]][new_pos[1]] == 0:
        mp[new_pos[0]][new_pos[1]] = dice[6]
    else:
        dice[6] = mp[new_pos[0]][new_pos[1]]
        mp[new_pos[0]][new_pos[1]] = 0

    top_num = dice[1]

    return top_num


def solution(x, y, mp, comm):
    cur_pos = [x, y]
    dice = [0 for _ in range(7)] # index 0은 안씀
    for com in comm: # 동 서 북 남
        new_pos = [cur_pos[0] + di[com], cur_pos[1] + dj[com]]
        if not checkRange(*new_pos,len(mp),len(mp[0])):
            continue

        #debug
        # print('cur_pos',cur_pos,'com',com)
        # printMap(mp)
        # print('dice',dice)
        # printDice(dice)

        cur_pos[:] = new_pos
        print(rotateDice(mp, dice, com, cur_pos))

    return


def checkRange(i, j, N, M):
    return 0 <= i and i < N and 0 <= j and j < M


N, M, x, y, K = map(int, read().split())
mp = [list(map(int, read().split())) for _ in range(N)]
comm = list(map(int, read().split()))

solution(x, y, mp, comm)







print('time',time.time_ns()-ptime)


