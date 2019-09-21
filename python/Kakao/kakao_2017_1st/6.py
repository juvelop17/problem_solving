import copy

di = [1, -1, 1, -1]
dj = [1, 1, -1, -1]

def solution(m, n, board):
    answer = 0

    for i in range(m):
        board[i] = "/".join(board[i]).split('/')

    is_updated = True
    while is_updated:
        is_updated = False
        removeBlockList = copy.deepcopy(board)
        # print_board(board)
        # print_board(removeBlockList)

        for i in range(m):
            for j in range(n):
                if board[i][j] != ' ':
                    checkBlockType(m, n, board, removeBlockList, board[i][j], i, j)
                if removeBlockList[i][j] == '1':
                    is_updated = True

        if is_updated:
            for i in range(m):
                for j in range(n):
                    if removeBlockList[i][j] == '1':
                        board[i][j] = '@'  # 없어지는 공간

            for j in range(n):
                _str = ''
                for i in range(m):
                    if board[i][j] != '@':
                        _str += board[i][j]
                    board[i][j] = ' '
                for i in range(1,len(_str)+1):
                    board[-i][j] = _str[-i]

    cnt = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == ' ':
                cnt += 1

    answer = cnt
    return answer




def checkBlockType(m, n, board, removeBlockList, char_type, current_i, current_j):
    for i in range(4):
        node_i = current_i + di[i]
        node_j = current_j + dj[i]

        if (node_i < 0 or node_i >= m or node_j < 0 or node_j >= n):
            continue

        if (char_type == board[node_i][current_j] and
                char_type == board[current_i][node_j] and
                char_type == board[node_i][node_j]):
            removeBlockList[current_i][current_j] = '1'
            removeBlockList[node_i][current_j] = '1'
            removeBlockList[current_i][node_j] = '1'
            removeBlockList[node_i][node_j] = '1'


# def print_board(board):
#     for i in range(m):
#         print(board[i])


# m, n = map(int, input().strip().split(' '))
# m, n = 4, 5
# board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

#

solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])
