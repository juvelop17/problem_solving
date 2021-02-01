import time

ptime = time.time_ns()

# import sys
# sys.stdin = open('input.txt','r')


#####################################################

w = 100000000
h = 999999999

import math

def solution(w, h):
    answer = 1

    ratio = h/w
    # print(ratio)
    # print(1/ratio)

    cnt = 0
    if ratio < 1:
        cnt = math.ceil(1/ratio) * h
    else:
        cnt = math.ceil(ratio) * w

    print(cnt)
    answer = h * w - cnt

    return answer

print(solution(w, h))

#####################################################

print('time',time.time_ns()-ptime)

