import sys
import time

ptime = time.time_ns()

sys.stdin = open('input.txt', 'r')


#####################################################

def convert(a,Ato,Bto,Cto):
    b = ''
    for ch in a:
        if ch == 'A':
            b += Ato
        elif ch == 'B':
            b += Bto
        elif ch == 'C':
            b += Cto
    return b

def verify(b):
    cnt = 0
    success = True
    for ch in b:
        if ch == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            success = False
            break
    if cnt != 0:
        success = False
    return success

def solution(a):
    res = []
    ans = False
    for ch1 in ('(',')'):
        for ch2 in ('(',')'):
            for ch3 in ('(',')'):
                res.append(convert(a,ch1,ch2,ch3))
    for b in res:
        if verify(b):
            ans = True
    return 'YES' if ans else 'NO'

t = int(input())
for tt in range(t):
    a = input().strip()
    print(solution(a))

#####################################################



print('time', (time.time_ns() - ptime)/10**6,'ms')
