
def getMinPrime(l):
    li = [1] * (l + 1)
    m = int(l ** 0.5)
    for i in range(2, m + 1):
        if li[i] == 1:
            if l % i == 0:
                return i
            for j in range(i+i, len(li), i):
                li[j] = 0
    # print(li)
    return 1


def dfs(li):
    num = getMinPrime(len(li))
    if num == 1:
        return li
    splitList = [[] for _ in range(num)]
    for i in range(num):
        for j in range(int(len(li)/num)):
            splitList[i].append(li[i + j * num])
    # print(splitList)

    res = []
    for r in splitList:
        res.extend(dfs(r))

    return res

def solution(n):
    li = [i for i in range(1, n+1)]
    answer = dfs(li)

    return answer


if __name__ == '__main__':
    # n = 12

    # n = 18

    n = 1000
    print(solution(n))

    # print(getPrimeList(10))
    # print(getMinPrime(2))