
import time
ptime = time.time_ns()



def printMap(mp, n):
    for i in range(len(mp)):
        print(n-i,end=' ')
        for k in range(2):
            # print(k, end=' ')
            if k == 1:
                print('  ',end='')
            for j in range(len(mp)):
                if mp[i][j][k] and k == 0:
                    print('|',end=' ')
                elif mp[i][j][k] and k == 1:
                    print('--', end='')
                else:
                    print('  ',end='')
            print()
    print('  ', end='')
    for i in range(len(mp)):
        print(i, end=' ')
    print()


def checkRange(x,y,n):
    return x >= 0 and x <= n and y >= 0 and y <= n

def checkMap(mp, n):
    for i in range(len(mp)):
        for j in range(len(mp)):
            for k in range(2):
                if mp[i][j][k]:
                    if k == 0:  # 기둥
                        if i == n:  # 바닥일경우
                            continue
                        elif checkRange(i + 1, j, n) and mp[i + 1][j][0]:  # 아래 기둥 존재
                            continue
                        elif checkRange(i, j, n) and mp[i][j][1]:  # 오른쪽 아래 보 존재
                            continue
                        elif checkRange(i, j - 1, n) and mp[i][j - 1][1]:  # 왼쪽 아래 보 존재
                            continue
                        return False
                    elif k == 1:
                        if checkRange(i + 1, j, n) and mp[i + 1][j][0]:  # 아래 기둥 존재
                            continue
                        elif checkRange(i + 1, j + 1, n) and mp[i + 1][j + 1][0]:  # 오른쪽 아래 기둥 존재
                            continue
                        elif checkRange(i, j - 1, n) and checkRange(i, j + 1, n) and mp[i][j - 1][1] and mp[i][j + 1][1]:  # 양 옆에 보 존재
                            continue
                        return False

    return True


# 구조물 : 좌표 오른쪽
# 기둥 : 좌표 위쪽
def solution(n, build_frame):
    answer = []

    # 0: 기둥, 1: 보
    mp = [[[False, False] for _ in range(n+1)] for _ in range(n+1)]

    for build in build_frame:
        y, x, a, b = build # x, y, 종류, 설치/삭제
        x = n - x # 좌표계 수정

        # print('build',build)
        if b == 0: # 삭제
            mp[x][y][a] = False
            if not checkMap(mp, n):
                mp[x][y][a] = True
        else: # 생성
            mp[x][y][a] = True
            if not checkMap(mp, n):
                mp[x][y][a] = False
        # printMap(mp, n)

    # 구조물 리스트 추가
    # 좌표계 복구

    for j in range(n+1):
        for i in range(n,-1,-1):
            for k in range(2):
                if mp[i][j][k]:
                    answer.append([j,n-i,k])

    return answer





n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1],[4,2,1,1]]
# build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]


print(solution(n, build_frame))



print('time',time.time_ns()-ptime)


