

from copy import deepcopy

di = [-1,1,0,0]
dj = [0,0,-1,1]


def resetVisited():
    return [[False for _ in range(4)] for _ in range(4)]

def checkRange(i,j):
    if i < 0 or i >= 4 or j < 0 or j >= 4:
        return False
    return True

def printBoard(board,curi,curj):
    for i in range(4):
        for j in range(4):
            if curi == i and curj == j:
                print('.', end=' ')
            else:
                print(board[i][j], end=' ')
        print()
    print()

def checkFinish(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                return False
    return True

def DFS(board, visited , i, j, cnt, card_num):
    global min_cnt
    print('card_num', card_num, 'cnt', cnt)
    printBoard(board,i,j)
    visited[i][j] = True

    if cnt > min_cnt:
        return

    if card_num == 0 and board[i][j] != 0: # 처음 카드 선택
        new_board = deepcopy(board)
        new_card = new_board[i][j]
        new_board[i][j] = 0
        visited = resetVisited()
        DFS(new_board,visited,i,j,cnt+1,new_card)

    if card_num > 0 and card_num == board[i][j]: # 두번째 카드 선택
        new_board = deepcopy(board)
        new_board[i][j] = 0
        new_card = 0
        if checkFinish(new_board):
            if min_cnt > cnt + 1:
                min_cnt = cnt + 1
            return min_cnt
        visited = resetVisited()
        return DFS(new_board,visited, i, j, cnt + 1, new_card)

    # 이동
    for num in range(4): # 한칸 이동
        new_i = i + di[num]
        new_j = j + dj[num]
        if checkRange(new_i,new_j) and visited[new_i][new_j] == False:
            DFS(board,visited, new_i, new_j, cnt+1, card_num)

    # 컨트롤 이동
    for num in range(4):
        new_i = i
        new_j = j
        distance = 1
        while checkRange(new_i,new_j) and board[new_i][new_j] == 0:
            new_i = new_i + di[num]
            new_j = new_j + dj[num]

        if not checkRange(new_i,new_j):
            new_i = new_i - di[num]
            new_j = new_j - dj[num]

        if visited[new_i][new_j] == False:
            DFS(board,visited, new_i, new_j, cnt + 2, card_num)


def solution(board, r, c):
    global min_cnt
    answer = 0
    visited = resetVisited()

    resetVisited()
    min_cnt = 10000000
    DFS(deepcopy(board),visited,r,c,0,0)
    answer = min_cnt

    return answer


board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0


# board = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
# r = 0
# c = 1


print(solution(board,r,c))
