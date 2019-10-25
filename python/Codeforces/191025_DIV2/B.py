import sys
# import time


# prev_time = time.time()
sys.stdin = open('input.txt','r')
read = sys.stdin.readline

def solution():
    zcnt, ocnt = getZeroOne()

    len_list =[]
    for i in range(n):
        len_list.append(len(pan[i]))
    len_list.sort()

    total = sum(len_list)
    cnt = 0
    i = 0
    while True:
        if i == len(len_list) or total < len_list[i]:
            break
        total -= len_list[i]
        if ocnt >= len_list[i]:
            ocnt -= len_list[i]
        else:
            ocnt = 0
        cnt += 1
        i += 1

    if total != 0 and ((total%2 == 0 and ocnt%2 == 0) or (total%2 == 1 and ocnt%2 == 1)):
        cnt += 1

    return cnt


def getZeroOne():
    zcnt = 0
    ocnt = 0
    for i in range(n):
        for p in pan[i]:
            if p == '0':
                zcnt += 1
            elif p == '1':
                ocnt += 1
    return zcnt, ocnt


q = int(read().strip())
for i in range(q):
    n = int(read().strip())
    pan = []
    for _ in range(n):
        pan.append(read().strip())
    print(solution())
# print('time',time.time()-prev_time)

