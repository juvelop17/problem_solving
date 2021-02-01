import time

ptime = time.time_ns()

# import sys
# sys.stdin = open('input.txt','r')


#####################################################



n = 10
colors = [1,1,2,2,2,3,3,3,2,2]


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


max_score = -1

def dfs(cmp, sel, cscore):
    global max_score
    # print('cmp, sel, cscore',cmp, sel, cscore)

    nscore = cscore + cmp[sel][1] ** 2
    if nscore > max_score:
        max_score = nscore

    if sel > 0 and sel < len(cmp) - 1 and cmp[sel-1][0] == cmp[sel+1][0]:
        nmp = cmp[:sel] + cmp[sel + 2:]
        nmp[sel-1] = (cmp[sel-1][0],cmp[sel-1][1] + cmp[sel+1][1])
    else:
        nmp = cmp[:sel] + cmp[sel + 1:]
    # print('nmp',nmp)

    for i in range(len(nmp)):
        dfs(nmp, i, nscore)

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

    for sel in range(len(cmp)):
        dfs(cmp, sel, 0)
    # print(max_score)

    answer = max_score
    return answer




print(solution(n, colors))


#####################################################

print('time',time.time_ns()-ptime)

