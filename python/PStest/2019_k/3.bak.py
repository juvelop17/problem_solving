# 잠겨있는 자물쇠는 격자 한 칸의 크기가 1 x 1인 N x N 크기의 정사각 격자 형태이고
# 특이한 모양의 열쇠는 M x M 크기인 정사각 격자 형태로 되어 있습니다.

# 자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있습니다.
# 열쇠는 회전과 이동이 가능하며
# 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다.
# 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만,
# 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며
# 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다.
# 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.

# 열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때,
# 열쇠로 자물쇠를 열수 있으면 true를, 열 수 없으면 false를 return 하도록 solution 함수를 완성해주세요.

# key는 M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열입니다.
# lock은 N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열입니다.
# M은 항상 N 이하입니다.
# key와 lock의 원소는 0 또는 1로 이루어져 있습니다.
# 0은 홈 부분, 1은 돌기 부분을 나타냅니다.



def solution(key, lock):
    answer = False

    M = len(key)
    N = len(lock)

    currKey = key
    targetPointList = findTargetPoint(lock)
    keyPoint = findKeyPoint(key)

    for i in range(4):
        currKey = rotateKey(currKey)
        keyPoint = rotateKeyPoint(keyPoint)

        for targetPoint in targetPointList:
            result = matchKeyLock(currKey,lock,keyPoint,targetPoint)
            # print('matchKeyLock result',result,targetPoint)

            if result:
                answer = True
                return answer

    return answer


def findTargetPoint(lock):
    targetPointList = []
    for i in range(3):
        for j in range(3):
            if lock[i][j] == 0:
                targetPointList.append([i,j])
    return targetPointList


def rotateKey(currKey):
    newKey = []
    newKey.append([currKey[2][0],currKey[1][0],currKey[0][0]])
    newKey.append([currKey[2][1],currKey[1][1],currKey[0][1]])
    newKey.append([currKey[2][2],currKey[1][2],currKey[0][2]])
    return newKey


def findKeyPoint(key):
    for i in range(3):
        for j in range(3):
            if key[i][j] == 1:
                return [i,j]


def rotateKeyPoint(keyPoint):
    li1 = [[0,0],[0,2],[2,2],[2,0]]
    if keyPoint in li1:
        if li1.index(keyPoint) == 3:
            newIndex = 0
        else:
            newIndex = li1.index(keyPoint) + 1
        return li1[newIndex]

    li2 = [[0,1],[1,2],[2,1],[1,0]]
    if keyPoint in li2:
        if li2.index(keyPoint) == 3:
            newIndex = 0
        else:
            newIndex = li2.index(keyPoint) + 1
        return li2[newIndex]

    return keyPoint # [1,1]


def matchKeyLock(currKey,lock,keyPoint,targetPoint):
    isMatch = True
    newKey = [[0,0,0],[0,0,0],[0,0,0]]

    diff = [targetPoint[0]-keyPoint[0],targetPoint[1]-keyPoint[1]]
    for i in range(3):
        for j in range(3):
            new_i = i+diff[0]
            new_j = j+diff[1]
            if 0 <= new_i <= 2 and 0 <= new_j <= 2:
                newKey[new_i][new_j] = currKey[i][j]
    # print('newKey',currKey, newKey)

    for i in range(3):
        for j in range(3):
            if newKey[i][j] + lock[i][j] != 1:
                isMatch = False

    return isMatch


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))


# print(rotateKey([[1,2,3],[4,5,6],[7,8,9]]))
print(solution([[0,0,0],[1,0,1],[0,0,0]],[[1,1,1],[1,1,1],[0,1,0]]))









