import heapq
# def binary_search(li, target):
#     if len(li) == 0:
#         return 0
#
#     start = 0
#     end = len(li) - 1
#     while start <= end:
#         mid = int((start + end) / 2)
#         if li[mid] == target:
#             return mid
#         elif li[mid] > target:
#             end = mid - 1
#         elif li[mid] < target:
#             start = mid + 1
#
#     return mid


def optimal(rank):
    answer = []

    sort_list = []
    heap_sort = []
    for i in rank:
        sort_list.append(i)
        sort_list.sort(reverse=True) # 부하 발생?

        # 순위 매기기
        answer.append(sort_list.index(i) + 1)
        print(sort_list)

    return answer

N = int(input().strip())

rank = []
for i in range(N):
    rank.append(int(input().strip()))

answer = optimal(rank)
for i in answer:
    print(i)
