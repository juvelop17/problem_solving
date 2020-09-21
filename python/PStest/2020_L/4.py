


# 바라보는 방향
# 북, 동, 남, 서
next_di = [-1,0,1,0]
next_dj = [0,1,0,-1]

left_hand_i = [0,-1,0,1]
left_hand_j = [-1,0,1,0]

def printMap(m, cur_i, cur_j):
    for i in range(len(m)):
        for j in range(len(m)):
            if i == cur_i and j == cur_j:
                print('.', end=' ')
            else:
                print(m[i][j], end=' ')
        print()
    print()

def dfs(maze, cur_i, cur_j, dir, cnt):
    res_cnt = 0
    # print('cur_i, cur_j, dir, cnt : ',cur_i, cur_j, dir, cnt)
    # printMap(maze,cur_i,cur_j)
    if cur_i == len(maze)-2 and cur_j == len(maze)-2: # padding 영향
        return cnt

    # 1. 왼손 파악 : 왼손에 벽이 있는지 파악한다.
    #    - 벽일 경우 2번
    #    - 아닐 경우 왼쪽으로 회전
    # 2. 앞쪽 파악 :
    #    - 앞쪽이 뚫려있으면 앞으로간다.
    #    - 앞쪽이 막히면 왼손을 본다.
    #       - 왼손이 막혀 있을 경우 오른쪽 회전

    new_dir = dir
    new_cnt = cnt
    new_i = cur_i
    new_j = cur_j
    if maze[cur_i+left_hand_i[new_dir]][cur_j+left_hand_j[new_dir]] == 0:
        new_dir = (new_dir-1) % 4

    if maze[cur_i+next_di[new_dir]][cur_j+next_dj[new_dir]] == 0:
        new_cnt += 1
        new_i += next_di[new_dir]
        new_j += next_dj[new_dir]
    else:
        new_dir = (new_dir+1) % 4

    return dfs(maze,new_i,new_j,new_dir,new_cnt)

def solution(maze):
    answer = 0

    # 1 padding
    new_maze = [[1 for _ in range(len(maze)+2)] for _ in range(len(maze)+2)]
    for i in range(len(maze)):
        for j in range(len(maze)):
            new_maze[i+1][j+1] = maze[i][j]
    answer = dfs(new_maze,1,1,0,0)

    return answer


# maze = [[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]
# maze =[[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]
# maze =[[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]]
maze =[[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]

print(solution(maze))

