



import sys
sys.stdin = open('input.txt','r')



t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))


    cur = -1
    res = [a[0]]
    for i in range(1,n-1):
        num = i % n - 1
        if res[num] != a[i]:
            res.append(a[i])
        elif res[num] != b[i]:
            res.append(b[i])
        elif res[num] != c[i]:
            res.append(c[i])

    if a[n-1] not in [res[0],res[-1]]:
        res.append(a[n-1])
    elif b[n-1] not in [res[0],res[-1]]:
        res.append(b[n-1])
    elif c[n-1] not in [res[0],res[-1]]:
        res.append(c[n-1])

    for r in res:
        print(r, end=' ')
    print()






