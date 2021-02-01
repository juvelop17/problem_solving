import time

ptime = time.time_ns()

import sys

sys.stdin = open('input.txt', 'r')


#####################################################

def solution():
    return


t = int(input())
for tt in range(t):
    print(solution())

#####################################################

print('time', time.time_ns() - ptime)

