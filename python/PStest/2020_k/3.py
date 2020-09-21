

def printMatrix(mat):
    for mi in mat:
        for mj in mi:
            print(mj, end=' ')
        print()
    print()

def rotateKey(key):
    new_key = [[0 for _ in range(len(key))] for _ in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):
            new_key[i][len(key)-1-j] = key[j][i]
    return new_key

def addKeyLock(key, lock):
    res = False
    len_padding = len(lock)+len(key)*2-2

    for i in range(len(lock)+len(key)-1):
        for j in range(len(lock)+len(key)-1):
            this_case = True
            padding_key = [[0 for _ in range(len_padding)] for _ in range(len_padding)]

            for k in range(len(key)):
                for l in range(len(key)):
                    padding_key[i+k][j+l] += key[k][l]
            # print('padding_key1')
            # printMatrix(padding_key)

            for k in range(len(lock)):
                for l in range(len(lock)):
                    padding_key[len(key) - 1 + k][len(key) - 1 + l] += lock[k][l]
            # print('padding_key2')
            # printMatrix(padding_key)

            for k in range(len(lock)):
                for l in range(len(lock)):
                    if padding_key[len(key) - 1 + k][len(key) - 1 + l] != 1:
                        this_case = False

            if this_case:
                res = True

    return res

def solution(key, lock):
    answer = False

    for r in range(4):
        key = rotateKey(key)
        if (addKeyLock(key,lock)):
            answer = True

    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# key = [[0, 0, 0], [0, 0, 1], [0, 1, 0]]
# lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(key, lock)
print(solution(key, lock))



