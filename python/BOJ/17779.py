
import time

ptime = time.time_ns()

import sys
sys.stdin = open('input.txt','r')


#####################################################


N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

def printMap(mp):
    for i in range(N):
        for j in range(N):
            print(mp[i][j],end='\t')
        print()
    print()

def cal(A, nmp):
    set_sum = [0 for _ in range(6)]
    for i in range(N):
        for j in range(N):
            if nmp[i][j] == 1:
                set_sum[1] += A[i][j]
            elif nmp[i][j] == 2:
                set_sum[2] += A[i][j]
            elif nmp[i][j] == 3:
                set_sum[3] += A[i][j]
            elif nmp[i][j] == 4:
                set_sum[4] += A[i][j]
            elif nmp[i][j] == 5:
                set_sum[5] += A[i][j]
    return max(set_sum[1:]) - min(set_sum[1:])

def solution(A):
    min_diff = 10**9
    for x in range(N):
        for y in range(N):
            for d1 in range(1,N):
                for d2 in range(1,N):
                    if x + d1 + d2 >= N or y - d1 < 0 or y + d2 >= N:
                        continue
                    left = [(x,y)]
                    right = [(x,y)]
                    for d in range(1,d1+1):
                        left.append((x+d,y-d))
                    for d in range(1,d2+1):
                        right.append((x+d,y+d))
                    for d in range(1,d2+1):
                        left.append((x+d1+d,y-d1+d))
                    for d in range(1,d1+1):
                        right.append((x+d2+d,y+d2-d))
                    # print('x,y,d1,d2',x,y,d1,d2)
                    # print('left',left)
                    # print('right',right)

                    nmp = [[-1 for _ in range(N)] for _ in range(N)]
                    for idx in range(len(left)):
                        i,j_l = left[idx]
                        i,j_r = right[idx]
                        for j in range(j_l,j_r+1):
                            nmp[i][j] = 5

                    for i in range(x+d1):
                        for j in range(y+1):
                            if nmp[i][j] == -1:
                                nmp[i][j] = 1
                    for i in range(x+d2+1):
                        for j in range(y+1,N):
                            if nmp[i][j] == -1:
                                nmp[i][j] = 2
                    for i in range(x+d1,N):
                        for j in range(y-d1+d2):
                            if nmp[i][j] == -1:
                                nmp[i][j] = 3
                    for i in range(x+d2+1,N):
                        for j in range(y-d1+d2,N):
                            if nmp[i][j] == -1:
                                nmp[i][j] = 4

                    diff = cal(A,nmp)
                    if diff < min_diff:
                        min_diff = diff
                    # print('x,y',x,y)
                    # print('min_diff,diff',min_diff,diff)
                    # printMap(nmp)

    return min_diff

print(solution(A))









#####################################################

print('time',time.time_ns()-ptime)

