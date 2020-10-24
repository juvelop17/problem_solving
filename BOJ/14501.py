
import sys
import time


prev_time = time.time_ns()
# sys.stdin = open('input1.txt','r')
read = sys.stdin.readline

def solution():

    for i in range(N+1):
        for j in range(i):
            if profit[j][0] + j <= i:
                profit_memory[i] = max(profit_memory[i], profit_memory[j]+profit[j][1])
    # print(profit_memory)
    return max(profit_memory)


N = int(read().strip())
profit = []
profit_memory = [0 for _ in range(N+1)]
for _ in range(N):
    profit.append(list(map(int, read().strip().split())))

print(solution())
# print('time',time.time_ns()-prev_time)

