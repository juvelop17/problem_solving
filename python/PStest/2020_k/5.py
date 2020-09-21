


def removeCheck(mp, x, y, a):
    if a == 0: # 기둥 제거
        if mp[x][y+1][0]: # 위쪽 기둥 체크
            if not (mp[x-1][y+1][1] or mp[x][y+1][1]):
                return False
        if mp[x][y+1][1]: # 우상보 체크
            if (not (mp[x-1][y+1][1] and mp[x+1][y+1][1])) and not mp[x+1][y][0]:
                return False
        if mp[x-1][y+1][1]: # 좌상보 체크
            if (not (mp[x-2][y+1][1] and mp[x+1][y+1][1])) and not mp[x+1][y][0]:
                return False
    else: # 보 제거
        mp[x][y][a]

    return True




def solution(n, build_frame):
    answer = [[]]

    mp = [[[False, False] for _ in range(n)] for _ in range(n)]

    for build in build_frame:
        x, y, a, b = build
        if b == 0: # 삭제
            if removeCheck(mp, x, y, a):
                mp[x][y][a] = False
        else:
            if buildCheck(mp, x, y, a):
                mp[x][y][a] = True






    return answer





n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]


print(solution(n, build_frame))



