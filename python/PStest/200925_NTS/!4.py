
import time
pt = time.time_ns()



def setDP(tree,dp,visited,index):
    if index == -1:
        return 0
    if visited[index]:
        return dp[index]

    visited[index] = True
    dp[index] = setDP(tree,dp,visited,tree[index][0]) + setDP(tree,dp,visited,tree[index][1]) + 1

    return dp[index]

def find(dp, num):
    res = []
    for i in range(len(dp)):
        if dp[i] == num:
            res.append(i)
    return res

#
# def getTreeList(tree, li, index):
#     if index == -1:
#
#
# def compare(t1, t2, index_list):


def check(t1, t2):
    dp1 = [0 for _ in range(len(t1))]
    visited1 = [False for _ in range(len(t1))]
    res1 = setDP(t1,dp1,visited1,0)
    # print('res1',res1)

    dp2 = [0 for _ in range(len(t2))]
    visited2 = [False for _ in range(len(t1))]
    res2 = setDP(t2,dp2,visited2,0)
    # print('res2',res2)

    index_list = find(dp1, res2)
    # print(index_list)

    return len(index_list)
    # result_list = compare(t1,t2,index_list)


def solution(t1, t2):
    answer = -1

    answer = check(t1,t2)


    return answer



t1 = [[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
t2 = [[1,2],[-1,-1],[-1,-1]]

# t1 = [[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
# t2 = [[-1, 1], [-1, -1]]


print(solution(t1,t2))



print('time',time.time_ns()-pt)



