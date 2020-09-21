import sys
import time


prev_time = time.time()
# sys.stdin = open('input1.txt','r')
read = sys.stdin.readline

def solution():
    global n
    res = [0 for _ in range(n)]

    for i in range(1, n + 1):
        if res[i-1] != 0:
            continue
        cnt = 1
        num = p_list[i - 1]
        num_list = []
        num_list.append(num)
        for _ in range(n):
            if i == num:
                break
            num = p_list[num - 1]
            num_list.append(num)
            cnt += 1

        for nl in num_list:
            res[nl-1] = cnt

    return res

q = int(read().strip())
for i in range(q):
    n = int(read().strip())
    p_list = list(map(int,read().strip().split()))
    for j in solution():
        print(j,end=' ')
    print()
# print('time',time.time()-prev_time)

