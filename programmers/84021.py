# 퍼즐 조각 채우기






di = [-1,1,0,0]
dj = [0,0,-1,1]

def checkRange(i, j):
    global n
    return i >= 0 and i < n and j >= 0 and j < n


def part(table, i, j):
    shape = []
    shape.append([0, 0])
    table[i][j] = 0
    idx = 0
    while idx < len(shape):
        ci, cj = shape[idx]
        ci += i
        cj += j
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if checkRange(ni, nj) and table[ni][nj] == 1:
                shape.append([ni-i,nj-j])
                table[ni][nj] = 0
        idx += 1
    shape.sort()
    return shape


def fill(game_board, shapeList, i, j):
    target = []
    target.append([0, 0])
    game_board[i][j] = 1
    idx = 0
    while idx < len(target):
        ci, cj = target[idx]
        ci += i
        cj += j
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if checkRange(ni, nj) and game_board[ni][nj] == 0:
                target.append([ni-i,nj-j])
                game_board[ni][nj] = 1
        idx += 1
    target.sort()

    for shape in shapeList:
        if len(shape) != len(target):
            continue

        for idx in range(len(shape)):
            if shape[idx][0] != target[idx][0] or shape[idx][1] != target[idx][1]:
                break
            if idx == len(shape) - 1:
                shapeList.remove(shape)
                return len(target)

    for idx in range(len(target)):
        ci, cj = target[idx]
        ci += i
        cj += j
        game_board[ci][cj] = 0
    return 0


def rotate(game_board):
    global n

    newBoard = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            newBoard[j][n-1-i] = game_board[i][j]
    return newBoard



def solution(game_board, table):
    global n
    n = len(game_board)

    fillSum = 0

    shapeList = []
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                shape = part(table, i, j)
                shapeList.append(shape)

    # print(shapeList)
    # print(table)

    for _ in range(4):
        for i in range(n):
            for j in range(n):
                if game_board[i][j] == 0:
                    fillCnt = fill(game_board, shapeList, i, j)
                    fillSum += fillCnt
        game_board = rotate(game_board)
        # print(game_board)
        # print(shapeList)


    return fillSum




if __name__ == '__main__':
    game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
    table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]

    print(solution(game_board, table))

