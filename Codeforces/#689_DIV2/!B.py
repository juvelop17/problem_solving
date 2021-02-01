import time

ptime = time.time_ns()

import sys

sys.stdin = open('input.txt', 'r')


#####################################################


def check_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m

def count_spruce(x, y, mp):
    level = 1
    while True:
        sw = True
        for i in range(level):
            if not check_range(x+level-1, y-i) or mp[x+level-1][y-i] == '.':
                sw = False
            if not check_range(x+level-1, y+i) or mp[x+level-1][y+i] == '.':
                sw = False
        if sw == False:
            break
        level += 1

    return level - 1


def solution(n, m, mp):
    cnt = 0
    for x in range(n):
        for y in range(m):
            if mp[x][y] == '*':
                cnt += count_spruce(x,y,mp)

    return cnt

t = int(input())
for tt in range(t):
    n, m = map(int, input().split())
    mp = []
    for _ in range(n):
        mp.append(list(input()))
    print(solution(n, m, mp))

#####################################################

print('time', time.time_ns() - ptime)

