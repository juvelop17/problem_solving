import sys
sys.stdin = open('input.txt','r')


import math
t = int(input())
for _ in range(t):
    a, b, c = map(int,input().split())
    print(a+b+c-1)

