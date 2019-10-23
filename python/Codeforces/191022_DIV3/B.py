import sys
import time


prev_time = time.time()
sys.stdin = open('input.txt','r')
read = sys.stdin.readline

def solution():
    res = []
    for i in range(1,n+1):
        res.append(getCnt(i,p_list[i-1]))
    return res


def getCnt(i,num):
    if i == num:
        return 1

    return getCnt(i,p_list[num-1]) + 1



q = int(read().strip())
for i in range(q):
    n = int(read().strip())
    p_list = list(map(int,read().strip().split()))
    for j in solution():
        print(j,end=' ')
    print()
print('time',time.time()-prev_time)

