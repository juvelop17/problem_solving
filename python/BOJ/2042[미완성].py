#
#
# def change_list(b, c):
#     num_list[b - 1] = c
#
#
# def sum_list(b, c):
#     sum = 0
#     # for i in range(b-1,c):
#     #     sum += num_list[i]
#
#     print(sum)
#
# def sum(L, R, nodeNum, nodeL, nodeR):
#     if R < nodeL or nodeR < L:
#         print('선넘음')
#         return 0
#     if L <= nodeL and nodeR <= R: return arr[nodeNum]
#     mid = (nodeL + nodeR) / 2
#     return sum(L, R, nodeNum * 2, nodeL, mid) + sum(L, R, nodeNum * 2 + 1, mid + 1, nodeR)
#
# def update(index, data):
#     i +
#
#
# N, M, K = map(int, input().strip().split(' '))
#
# arr = [0] * (N+1)
#
# num_list = []
# for i in range(N):
#     num_list.append(int(input().strip()))
#
# for i in range(M + K):
#     a, b, c = map(int, input().strip().split(' '))
#     if a == 1:
#         change_list(b, c)
#     elif a == 2:
#         sum_list(b, c)
