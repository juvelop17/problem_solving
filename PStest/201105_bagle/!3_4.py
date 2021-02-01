import time

ptime = time.time_ns()

# import sys
# sys.stdin = open('input.txt','r')


#####################################################

prob = []

n = 10
colors = [1,1,2,2,2,3,3,3,2,2]
ans = 38
prob.append([n,colors,ans])

n = 1
colors = [1]
ans = 1
prob.append([n,colors,ans])

n = 2
colors = [2,2]
ans = 4
prob.append([n,colors,ans])

n = 2
colors = [1,2]
ans = 2
prob.append([n,colors,ans])

n = 5
colors = [1,2,2,2,1]
ans = 13
prob.append([n,colors,ans])

n = 5
colors = [1,2,1,2,1]
ans = 11
prob.append([n,colors,ans])

n = 5
colors = [1,2,3,2,1]
ans = 9
prob.append([n,colors,ans])

n = 6
colors = [1,2,2,2,3,1]
ans = 14
prob.append([n,colors,ans])

n = 7
colors = [1,2,2,2,3,3,1]
ans = 17
prob.append([n,colors,ans])

n = 7
colors = [1,1,2,2,2,3,3]
ans = 17
prob.append([n,colors,ans])

n = 6
colors = [1,1,2,2,3,3]
ans = 12
prob.append([n,colors,ans])

n = 6
colors = [1,1,2,2,3,3]
ans = 12
prob.append([n,colors,ans])

n = 6
colors = [1,1,2,1,2,2]
ans = 14
prob.append([n,colors,ans])

n = 6
colors = [2,2,2,1,2,1]
ans = 18
prob.append([n,colors,ans])

n = 7
colors = [2,2,1,2,1,2,1]
ans = 19
prob.append([n,colors,ans])

n = 14
colors = [2,2,1,2,1,2,1,3,3,3,3,3,3,3]
ans = 68
prob.append([n,colors,ans])

n = 0 # 자동 계산
colors = [2,2,1,1,2,2,1,1]
ans = 24
prob.append([n,colors,ans])

n = 0 # 자동 계산
colors = [1,1,2,2,2,3,3,3,2,2,3,3]
ans = 42
prob.append([n,colors,ans])

n = 0 # 자동 계산
colors = [1,2,3,4,1,4,3,2,1] # 실제 답 17
ans = 17
prob.append([n,colors,ans])

def dfs(cmp):
    if len(cmp) == 0:
        return 0

    color_idx = {}
    color_cnt = {}

    max_cnt = 0
    max_color = -1
    for i in range(len(cmp)):
        col, cnt = cmp[i]
        if col not in color_cnt:
            color_cnt[col] = 0
            color_idx[col] = []
        color_cnt[col] += cnt
        color_idx[col].append(i)
        if max_cnt < color_cnt[col]:
            max_color = col
            max_cnt = color_cnt[col]

    # print('max_color, max_cnt',max_color, max_cnt)

    score = 0

    # 안쪽 블록 계산
    max_idx = color_idx[max_color]
    for i in range(len(max_idx)-1):
        start = max_idx[i] + 1
        end = max_idx[i+1]
        nmp = cmp[start:end]
        score += dfs(nmp)

    # 가장 많은 블록 계산
    score += max_cnt**2

    # 바깥 블록 계산
    nmp = cmp[:max_idx[0]] + cmp[max_idx[-1] + 1:]
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





for p in prob:
    n, colors, ans = p
    result = solution(len(colors), colors)
    print('n, colors, ans, result',n, colors, ans, result)


#####################################################

print('time',time.time_ns()-ptime)

