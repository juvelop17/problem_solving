import time

ptime = time.time_ns()

# import sys
# sys.stdin = open('input.txt','r')


#####################################################

v = [[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]]

# v = [[0,0,1],[2,2,1],[0,0,0]]



cnt_list = [0,0,0]

di = [-1,1,0,0]
dj = [0,0,-1,1]

def print_map(mp):
    for i in range(len(mp)):
        for j in range(len(mp)):
            print(mp[i][j], end=' ')
        print()
    print()

def check_range(i, j, n):
    return i >= 0 and i < n and j >= 0 and j < n

def bfs(v, visited, i, j, num):
    que = []
    que.append((i, j))
    while que:
        ci, cj = que.pop() # pop(0)이랑 시간음복잡도 차이 있
        visited[ci][cj] = True

        for d in range(4):
            ni = ci + di[d]
            nj = cj + dj[d]
            if check_range(ni, nj, len(v)) and v[ni][nj] == num and not visited[ni][nj]:
                que.append((ni, nj))

def solution(v):
    answer = []

    # print_map(v)
    # print_map(visited)

    visited = [[False for _ in range(len(v))] for _ in range(len(v))]

    for i in range(len(v)):
        for j in range(len(v)):
            num = v[i][j]
            if visited[i][j] == False:
                bfs(v,visited,i,j,num)
                cnt_list[num] += 1
                # print_map(visited)

    answer = cnt_list
    return answer



print(solution(v))

#####################################################

print('time',time.time_ns()-ptime)

