

import sys
sys.stdin = open('input.txt','r')



def solution(n, l, a):

    a1 = a[:]
    a2 = [l - num for num in a[::-1]]
    print(a1, a2)
    v1 = 1
    v2 = 1
    t = 0
    l1 = 0
    l2 = 0
    i1 = 0
    i2 = 0
    while l1 + l2 < l:
        t1 = (a1[i1] - l1) / v1
        t2 = (a2[i2] - l2) / v2
        if t1 > t2:
            l2 = a2[i2]
            i2 += 1
            v2 += 1
            t = t2
        elif t1 < t2:
            l1 = a1[i1]
            i1 += 1
            v1 += 1
            t = t1
        else:
            l1 = a1[i1]
            i1 += 1
            v1 += 1
            l2 = a2[i2]
            i2 += 1
            v2 += 1
            t = t1
        if i1 == n or i2 == n:
            break
    print('i1,i2',i1,i2)
    print('t',t)

    res = (l-l1-l2) / (v1+v2) + t

    return round(res,6)





t = int(input())
for _ in range(t):
    n, l = map(int, input().split())
    a = list(map(int,input().split()))

    print(solution(n, l, a))




