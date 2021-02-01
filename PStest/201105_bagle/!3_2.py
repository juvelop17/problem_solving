import time

ptime = time.time_ns()

# import sys
# sys.stdin = open('input.txt','r')


#####################################################



n = 10
colors = [1,1,2,2,2,3,3,3,2,2]

n = 6
colors = [1,2,2,2,3,1]


# n = 50
# colors = [1, 1, 2, 2, 2, 3, 3, 3, 2, 2,
#           1, 1, 2, 2, 2, 3, 3, 3, 2, 2,
#           1, 1, 2, 2, 2, 3, 3, 3, 2, 2,
#           1, 1, 2, 2, 2, 3, 3, 3, 2, 2,
#           1, 1, 2, 2, 2, 3, 3, 3, 2, 2]


# n = 200
# colors = [1, 1, 2, 2, 2, 3, 3, 3, 2, 2,
#           1, 1, 2, 2, 2, 3, 3, 3, 2, 2,
#           1, 1, 2, 2, 2, 3, 3, 3, 2, 2,
#           1, 1, 2, 2, 2, 3, 3, 3, 2, 2,
#           1, 1, 2, 2, 2, 3, 3, 3, 2, 2,
#           1, 1, 2, 2, 2, 3, 3, 3, 2, 2,
#           1, 1, 2, 2, 2, 3, 3, 3, 2, 2,
#           1, 1, 2, 2, 2, 3, 3, 3, 2, 2,
#           1, 1, 2, 2, 2, 3, 3, 3, 2, 2,
#           1, 1, 2, 2, 2, 3, 3, 3, 2, 2,
#           1, 1, 2, 2, 2, 3, 3, 3, 2, 2,
#           1, 1, 2, 2, 2, 3, 3, 3, 2, 2,
#           1, 1, 2, 2, 2, 3, 3, 3, 2, 2,
#           1, 1, 2, 2, 2, 3, 3, 3, 2, 2,
#           1, 1, 2, 2, 2, 3, 3, 3, 2, 2,
#           1, 1, 2, 2, 2, 3, 3, 3, 2, 2,
#           1, 1, 2, 2, 2, 3, 3, 3, 2, 2,
#           1, 1, 2, 2, 2, 3, 3, 3, 2, 2,
#           1, 1, 2, 2, 2, 3, 3, 3, 2, 2,
#           1, 1, 2, 2, 2, 3, 3, 3, 2, 2]


def dfs(cmp):
    if len(cmp) == 0:
        return 0

    num_cnt = {}
    max_cnt = 0
    max_color = -1
    for i in range(len(cmp)):
        col, cnt = cmp[i]
        if col not in num_cnt:
            num_cnt[col] = 0
        num_cnt[col] += cnt
        if max_cnt < num_cnt[col]:
            max_color = col
            max_cnt = num_cnt[col]

    print('max_color, max_cnt',max_color, max_cnt)

    score = max_cnt**2
    start = 0
    end = start
    while end < len(cmp):
        if cmp[end][0] == max_color:
            nmp = cmp[start:end]
            score += dfs(nmp)
            start = end + 1
        end += 1

        if end == len(cmp):
            nmp = cmp[start:end]
            score += dfs(nmp)

    return score


def solution(n, colors):
    answer = 0

    cmp = []
    i = 0
    numcnt = 1
    while i < n:
        if i == n - 1:
            cmp.append((colors[i],numcnt))
            break
        if colors[i] == colors[i+1]:
            numcnt += 1
        else:
            cmp.append((colors[i],numcnt))
            numcnt = 1
        i += 1
    # print(cmp)

    max_score = dfs(cmp)
    # print(max_score)

    answer = max_score
    return answer




print(solution(n, colors))


#####################################################

print('time',time.time_ns()-ptime)

