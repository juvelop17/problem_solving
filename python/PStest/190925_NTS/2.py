


import time
pt = time.time_ns()



dp = [0 for _ in range(50)]
visited = [False for _ in range(50)]


def dfs(N, index):
    if index == N:
        return 1
    if index > N:
        return 0
    if visited[index]:
        return dp[index]

    dp[index] = dfs(N, index+1) + dfs(N, index+2)
    visited[index] = True

    return dp[index]


def solution(N):
    answer = dfs(N,0)

    # print('answer',answer)

    return answer



# N = 1
# N = 2
# N = 3
N = 31
# N = 5

print(solution(N))



print('time',time.time_ns()-pt)





