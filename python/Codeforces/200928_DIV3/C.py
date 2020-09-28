
import sys
sys.stdin = open('input.txt','r')
read = sys.stdin.readline


import math

def solution(n):
    # num = 1
    # min_cnt = n // num - 1
    # while num <= math.sqrt(n):
    #     num += 1
    #     val = num - 1 + n // num - 1
    #     if n % num != 0:
    #         val += 1
    #     if min_cnt > val:
    #         min_cnt = val

    num = int(math.sqrt(n))
    cnt = num - 1 + n // num - 1
    if n % num != 0:
        cnt += 1

    return cnt

t = int(read())
for _ in range(t):
    print(solution(int(read())))





