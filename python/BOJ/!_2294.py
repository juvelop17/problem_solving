import sys
import time


start_time = time.time_ns()
sys.stdin = open('input.txt', 'r')

n,k = map(int,sys.stdin.readline().strip().split())

coin_list = []
for i in range(n):
    coin_list.append(int(sys.stdin.readline()))

coin_memory = [[-1 for _ in range(n)] for _ in range(len(coin_list))]

def countCoin(c,status):
    res = countCoin(c+1,0)
    if


end_time = time.time_ns()
print('time',end_time-start_time)






