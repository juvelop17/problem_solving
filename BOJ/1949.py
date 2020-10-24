
import time
ptime = time.time_ns()





import sys

sys.setrecursionlimit(100000) # recursion limit 설정

sys.stdin = open('input.txt','r')
read = sys.stdin.readline



def dfs(index):
    visited[index] = True
    for node in tree[index]:
        if visited[node]:
            continue
        dfs(node)
        dp[index][0] += max(dp[node][0], dp[node][1])
        dp[index][1] += dp[node][0]

    dp[index][1] += viliges[index]

def solution(N,viliges,connection):
    answer = -1

    # print(viliges,connection)

    dfs(1)
    answer = max(dp[1][0],dp[1][1])
    # print(dp)

    return answer


N = int(read())
viliges = [0] + list(map(int,read().split()))
connection = []
for _ in range(N-1):
    connection.append(list(map(int,read().split())))

tree = [[] for _ in range(N+1)]
for con in connection:
    tree[con[0]].append(con[1])
    tree[con[1]].append(con[0])

dp = [[0 for _ in range(2)] for _ in range(N+1)]

visited = [False for _ in range(N+1)]




print(solution(N,viliges,connection))



print('time',time.time_ns()-ptime)


