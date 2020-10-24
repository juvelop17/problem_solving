import time

ptime = time.time_ns()

import sys
sys.stdin = open('input.txt','r')



#####################################################


N = int(input())
A = list(map(int,input().split()))
plus, minus, mul, div = map(int, input().split())

max_num = -(10**10)
min_num = 10**10
oper_list = []
oper_dict = {'+': lambda x,y:x+y,
             '-': lambda x,y:x-y,
             '*': lambda x,y:x*y,
             '/': lambda x,y:int(x/y)}

def dfs(arr, plus, minus, mul, div):
    if plus + minus + mul + div == 0:
        oper_list.append(arr)
        return

    if plus > 0:
        dfs(arr + ['+'],plus - 1,minus,mul,div)
    if minus > 0:
        dfs(arr + ['-'], plus, minus - 1, mul, div)
    if mul > 0:
        dfs(arr + ['*'], plus, minus, mul - 1, div)
    if div > 0:
        dfs(arr + ['/'], plus, minus, mul, div - 1)

def cal():
    global max_num, min_num
    for opers in oper_list:
        # print('opers',opers)
        sum = A[0]
        for i in range(N-1):
            sum = oper_dict[opers[i]](sum,A[i+1])
        if sum > max_num:
            max_num = sum
        if sum < min_num:
            min_num = sum

def solution():
    dfs([],plus, minus, mul, div)
    cal()
    print(max_num)
    print(min_num)


solution()

#####################################################

print('time',time.time_ns()-ptime)

