import sys
import time

# #### Top Down #####
# start_time = time.time_ns()
# sys.stdin = open('input1.txt', 'r')
#
# n,k = map(int,sys.stdin.readline().strip().split())
#
# coin_list = []
# for i in range(n):
#     coin_list.append(int(sys.stdin.readline()))
#
# coin_memory = [-1 for _ in range(k+1)]
#
# def countCoin(curr,goal):
#     if coin_memory[goal-curr] != -1:
#         return coin_memory[goal-curr]
#
#     if curr > goal:
#         return 100000
#     if curr == goal:
#         return 0
#
#     min_list = [countCoin(curr+coin_list[i],goal) for i in range(len(coin_list))]
#     min_val = min(min_list)
#     coin_memory[goal - curr] = min_val + 1
#
#     return min_val + 1
#
# print(countCoin(0,k))
#
# end_time = time.time_ns()
# print('time',end_time-start_time)


### Bottom Up ###

start_time = time.time_ns()
sys.stdin = open('input.txt', 'r')

n,k = map(int,sys.stdin.readline().strip().split())

coin_list = []
for i in range(n):
    coin_list.append(int(sys.stdin.readline()))

coin_memory = [-1 for _ in range(k+1)]
coin_memory[0] = 0

def countCoin(goal):
    for g in range(1,goal+1):
        min_list = []

        for i in range(len(coin_list)):
            if g-coin_list[i] >= 0 and coin_memory[g-coin_list[i]] != -1:
                min_list.append(coin_memory[g-coin_list[i]])

        if len(min_list)==0:
            coin_memory[g] = -1
        else:
            coin_memory[g] = min(min_list)+1
    print(coin_memory)

    return coin_memory[goal]

print(countCoin(k))

end_time = time.time_ns()
# print('time',end_time-start_time)





