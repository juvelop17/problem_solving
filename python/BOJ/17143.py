
import time

ptime = time.time_ns()

import sys
sys.stdin = open('input.txt','r')


#####################################################


R, C, M = map(int, input().split())
mp = [[0 for _ in range(C)] for _ in range(R)]
sharks = [list(map(int,input().split())) for _ in range(M)]
# s : 속력
# d : 위 아래 오 왼
# z : 크기
for shark in sharks:
    r, c, s, d, z = shark
    mp[r-1][c-1] = [s,d,z]

def printMap(mp):
    for i in range(R):
        for j in range(C):
            if mp[i][j] == 0:
                print(mp[i][j], end='\t\t\t')
            else:
                print(mp[i][j], end='\t')
        print()
    print()

def fishing(mp, col):
    for i in range(R):
        if mp[i][col] != 0:
            shark = mp[i][col]
            mp[i][col] = 0
            # print('size',shark[2])
            return shark[2]
    return 0

def move(mp):
    nmp = [[0 for _ in range(C)] for _ in range(R)]
    shark_list = []
    for i in range(R):
        for j in range(C):
            if mp[i][j] != 0:
                shark_list.append([i,j,*mp[i][j]])

    for shark in shark_list:
        # print(shark)
        i, j, s, d, z = shark

        if d < 3: # 위 아래
            r = s % ((R-1)*2)
            ni = i
            nj = j
            nd = d # 방향
            while r:
                # 벽에 붙었을 경우
                if ni == 0:
                    nd = 2
                elif ni == R-1:
                    nd = 1

                if nd == 1:
                    ni -= 1
                else:
                    ni += 1
                r -= 1
        else:   # 오 왼
            r = s % ((C - 1) * 2)
            ni = i
            nj = j
            nd = d  # 방향
            while r:
                # 벽에 붙었을 경우
                if nj == 0:
                    nd = 3
                elif nj == C - 1:
                    nd = 4

                if nd == 3:
                    nj += 1
                else:
                    nj -= 1
                r -= 1

        # print('ni,nj,nd',ni,nj,nd)
        if nmp[ni][nj] != 0:
            nmp[ni][nj] = nmp[ni][nj] if nmp[ni][nj][2] > z else [s,nd,z]
        else:
            nmp[ni][nj] = [s,nd,z]

    return nmp

def solution(mp):
    answer = 0
    col = 0
    # printMap(mp)
    while col < C:
        answer += fishing(mp, col) # 낚시
        mp = move(mp) # 상어 이동
        col += 1
        # printMap(mp)

    return answer


print(solution(mp))






#####################################################

print('time',time.time_ns()-ptime)

