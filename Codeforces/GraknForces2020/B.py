


import sys
sys.stdin = open('input.txt','r')



def solution(n, k, a):
    res = 1
    if k == 1:
        for i in range(1,n):
            if a[i] != a[0]:
                return -1
        return 1

    cnt = 1
    cur = a[0]
    for index in range(1,n):
        if cur == a[index]:
            continue
        if cnt == k:
            res += 1
            cnt = 1
        cnt += 1
        cur = a[index]
    return res


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    print(solution(n, k, a))




