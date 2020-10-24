
import sys
import time


prev_time = time.time_ns()
# sys.stdin = open('input1.txt','r')
read = sys.stdin.readline

def solution():
    for curve in curve_list:
        x = curve[0]
        y = curve[1]
        d = curve[2]
        g = curve[3]
        pick = [[x,y],[x+dx[d],y+dy[d]]]
        makeCurve(0,g,pick)
        for p in pick:
            res.append(p)
    for p in res:
        arr[p[0]][p[1]] = 1

    cnt = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j]+arr[i][j+1]+arr[i+1][j]+arr[i+1][j+1] == 4:
                cnt += 1

    return cnt

def makeCurve(n,g,pick):
    if n == g:
        return

    end_point = pick[-1]
    start_point = pick[0]
    for i in range(len(pick)-2,-1,-1):
        new_x = -(pick[i][1] - end_point[1]) + end_point[0]
        new_y = (pick[i][0] - end_point[0]) + end_point[1]
        pick.append([new_x,new_y])

    makeCurve(n+1,g,pick)



dy = [0,-1,0,1]
dx = [1,0,-1,0]

N = int(read().strip())
curve_list = [list(map(int,read().strip().split())) for _ in range(N)]
arr = [[0 for _ in range(101)] for _ in range(101)]
res = []

print(solution())
# print('time',time.time_ns()-prev_time)

