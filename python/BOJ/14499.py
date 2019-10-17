import sys
import time

prev_time = time.time_ns()
# sys.stdin = open('input.txt','r')
read = sys.stdin.readline

di = [0,0,0,-1,1]
dj = [0,1,-1,0,0]

def solution():
    curr_pos = [x,y]
    dice = [0 for _ in range(6)]

    for c in comm:
        # if c == 1: # 동
        # elif c == 2: # 서
        # elif c == 3: # 북
        # elif c == 4: # 남

        new_pos = [curr_pos[0] + di[c], curr_pos[1] + dj[c]]
        if checkRange(new_pos[0], new_pos[1]):
            curr_pos = new_pos

            dice = rotateDice(dice, c)
            num = _map[new_pos[0]][new_pos[1]]
            if num == 0:
                _map[new_pos[0]][new_pos[1]] = dice[5]
            else:
                dice[5] = _map[new_pos[0]][new_pos[1]]
                _map[new_pos[0]][new_pos[1]] = 0

            print(dice[0]) # top


def rotateDice(dice, c):
    if c == 1:  # 동
        new_dice = [dice[3], dice[0], dice[2], dice[5], dice[4], dice[1]]
    elif c == 2:  # 서
        new_dice = [dice[1], dice[5], dice[2], dice[0], dice[4], dice[3]]
    elif c == 3:  # 북
        new_dice = [dice[2], dice[1], dice[5], dice[3], dice[0], dice[4]]
    else:  # 남
        new_dice = [dice[4], dice[1], dice[0], dice[3], dice[5], dice[2]]
    return new_dice



def checkRange(i,j):
    return i >= 0 and i < N and j >= 0 and j < M

N,M,x,y,K = map(int,read().split())
_map = []
for _ in range(N):
    _map.append(list(map(int,read().split())))

comm = list(map(int,read().split()))

solution()

# print('time',time.time_ns()-prev_time)