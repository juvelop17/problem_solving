def solution(research, n, k):

    dic = [{} for _ in range(len(research))]
    for i in range(len(research)):
        for j in range(len(research[i])):
            cur = research[i][j]
            if cur not in dic[i]:
                dic[i][cur] = 0
            dic[i][cur] += 1
    # print(dic)

    issueList = {}

    for i in range(26):
        cur = chr(ord('a') + i)
        issueCnt = 0
        cnt = 0
        for j in range(n):
            cnt += dic[j][cur] if cur in dic[j] else 0
            if cnt >= 2 * n * k:
                issueCnt += 1
        # print(cur, cnt)
        for j in range(1, len(research) - n + 1):
            cnt -= dic[j-1][cur] if cur in dic[j-1] else 0
            cnt += dic[j+n-1][cur] if cur in dic[j+n-1] else 0
            # print(cur, cnt)
            if cnt >= 2 * n * k:
                issueCnt += 1
        issueList[cur] = issueCnt
    # print(issueList)

    maxCh = 'None'
    maxIssue = 0
    for k, v in issueList.items():
        if v > maxIssue or (v == maxIssue and k < maxCh):
            maxIssue = v
            maxCh = k

    return maxCh






if __name__ == '__main__':
    # research =["abaaaa","aaa","abaaaaaa","fzfffffffa"]
    # n =2
    # k =2

    # research = ["yxxy","xxyyy"]
    # n = 2
    # k = 1

    # research = ["yxxy","xxyyy","yz"]
    # n = 2
    # k = 1

    research = ["xy","xy"]
    n = 1
    k = 1

    print(solution(research, n, k))

