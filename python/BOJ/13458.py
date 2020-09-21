import sys
import time


prev_time = time.time_ns()
# sys.stdin = open('input1.txt','r')


def solution():
    sum_cnt = 0

    for a in A_list:
        remain = a

        # 감독
        remain -= B
        sum_cnt += 1
        if remain <= 0:
            continue

        # 부감독
        sum_cnt += remain // C
        if remain % C != 0:
            sum_cnt += 1

    return sum_cnt


N = int(sys.stdin.readline().strip())
A_list = list(map(int,sys.stdin.readline().strip().split()))
B, C = map(int,sys.stdin.readline().strip().split())


print(solution())


# print('time',time.time_ns()-prev_time)