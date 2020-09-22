

import time

prev_time = time.time_ns()




import sys

# sys.stdin = open('input.txt','r')
read = sys.stdin.readline



def solution(A, B, C):
    cnt = 0

    for a in A:
        num = a - B
        cnt += 1
        if num > 0:
            cnt += num // C
            if num % C != 0:
                cnt += 1
    return cnt

N = int(read().strip())
A = list(map(int,read().split()))
B, C = map(int, read().split())

# print(N, A, B, C)

print(solution(A,B,C))









