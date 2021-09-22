from itertools import combinations_with_replacement

def solution(n, info):
    maxDiff = -1
    maxBoard = [-1]

    scoreList = [i for i in range(11)]
    for comb in combinations_with_replacement(scoreList, n):
        curBoard = [0 for _ in range(11)]
        for score in comb:
            curBoard[10-score] += 1
        # print(comb)
        # print(curBoard)

        liScore = 0
        apScore = 0
        for i in range(11):
            if curBoard[i] == info[i] and curBoard[i] == 0:
                continue
            if curBoard[i] > info[i]:
                liScore += 10 - i
            elif curBoard[i] <= info[i]:
                apScore += 10 - i

        if liScore > apScore and liScore - apScore > maxDiff:
            maxDiff = liScore - apScore
            maxBoard = curBoard
            # print(maxDiff, maxBoard)

    return maxBoard


if __name__ == '__main__':
    n = 5
    info = [2,1,1,1,0,0,0,0,0,0,0]

    print(solution(n, info))



