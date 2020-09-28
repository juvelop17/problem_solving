
import sys
import math
sys.stdin = open('input.txt','r')
read = sys.stdin.readline


def solution(n, x):
    if n <= 2:
        return 1
    return math.ceil((n-2) / x) + 1

t = int(read())
for _ in range(t):
    print(solution(*list(map(int,read().split()))))










