import sys
import time

ptime = time.time_ns()

sys.stdin = open('input.txt', 'r')


#####################################################

from collections import deque

def solution(n, blist):
    deq = deque(blist)
    ans = []
    for i in range(len(blist)):
        if i % 2 == 0:
            ans.append(deq.popleft())
        else:
            ans.append(deq.pop())
    return ans

t = int(input())
for tt in range(t):
    n = int(input())
    blist = list(map(int, input().split()))
    for num in solution(n, blist):
        print(num, end=' ')
    print()

#####################################################



print('time', time.time_ns() - ptime)

