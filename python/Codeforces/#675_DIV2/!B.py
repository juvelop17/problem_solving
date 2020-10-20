
import sys
sys.stdin = open('input.txt','r')


t = int(input())

for _ in range(t):
    n, m = map(int,input().split())
    mat = []
    for _ in range(n):
        mat.append(list(map(int,input().split())))
    # print(mat)

    total = 0
    for i in mat:
        for j in i:
            total += j
    # print(total, n*m)
    # print(total / (n*m))

    avr = total/(n*m)
    if avr != int(avr):
        cnt1 = 0
        cnt2 = 0
        for i in mat:
            for j in i:
                cnt1 += abs(int(avr) - j)
                cnt2 += abs(int(avr)+1 - j)
        print(min(cnt1,cnt2))
    else:
        cnt = 0
        for i in mat:
            for j in i:
                cnt += abs(int(avr)-j)
        print(cnt)

