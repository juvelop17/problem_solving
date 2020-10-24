import sys

# sys.stdin = open('input1.txt','r')

# def solution(li,n):
#     if li[n] != -1:
#         return li[n]
#
#     if n == 1:
#         return 0
#
#     cnt_list = []
#     if n % 3 == 0:
#         cnt_list.append(solution(li,n//3))
#     if n % 2 == 0:
#         cnt_list.append(solution(li,n//2))
#     cnt_list.append(solution(li, n-1))
#
#     res = 1 + min(cnt_list)
#     li[n] = res
#
#     return res
#
# n = int(sys.stdin.readline())
# li = [-1 for _ in range(n+1)]
#
# print(solution(li,n))


def solution(li,n):

    if li[n] != -1:
        return li[n]

    if n == 1:
        return 0

    cnt_list = []
    if n % 3 == 0:
        cnt_list.append(solution(li,n//3))
    if n % 2 == 0:
        cnt_list.append(solution(li,n//2))
    cnt_list.append(solution(li, n-1))

    res = 1 + min(cnt_list)
    li[n] = res

    return res

n = int(sys.stdin.readline())
li = [-1 for _ in range(10**6+1)]

for i in range(1,10**6+1):
    solution(li,i)

print(solution(li,n))



