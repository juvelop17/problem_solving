import sys
import time


prev_time = time.time()
sys.stdin = open('input.txt','r')
read = sys.stdin.readline

def solution():
    global n
    num_list = [3**i for i in range(10)]
    # print(num_list)

    th = 1
    for i in range(len(num_list)):
        if num_list[i] >= n:
            break
        th += 1
    print(num_list[th])

    return

q = int(read().strip())
for i in range(q):
    n = int(read().strip())
    print(solution())
# print('time',time.time()-prev_time)

