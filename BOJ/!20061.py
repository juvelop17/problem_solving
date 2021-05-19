


import sys
import time

ptime = time.time_ns()

sys.stdin = open('input.txt', 'r')


#####################################################

def solution(N, blocks):


    
    return

t = int(input())
for tt in range(t):
    N = int(input())
    blocks = []
    for _ in range(N):
        blocks.append(list(map(int, input().split())))
    print(solution(N, blocks))

#####################################################



print('time', (time.time_ns() - ptime)/10**6,'ms')




