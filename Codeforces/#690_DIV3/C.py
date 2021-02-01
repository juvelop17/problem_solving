import sys
import time

ptime = time.time_ns()

sys.stdin = open('input.txt', 'r')


#####################################################

def find(cursum, curdigit, curnum):
    if cursum == 0:
        return curnum
    if curdigit == 0:
        return -1

    if cursum < curdigit:
        nextdigit = cursum
    else:
        nextdigit = curdigit - 1

    return find(cursum - nextdigit, nextdigit, curnum * 10 + nextdigit)

def solution(x):
    num = find(x, 10, 0)
    if num != -1:
        numstr = str(num)
        res = int(numstr[::-1])
    else:
        res = -1

    return res

t = int(input())
for tt in range(t):
    x = int(input())
    print(solution(x))

#####################################################



print('time', time.time_ns() - ptime)

