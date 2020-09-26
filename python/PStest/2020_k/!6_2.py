import time

ptime = time.time_ns()





def find(n, weak, dist, dist_index, dist_list):
    # print('dist_index', dist_index)
    # print('weak', weak)
    # print('dist_list', dist_list)
    # print()

    if len(weak) == 0:
        # print('finish',dist_list)
        # print()
        return len(dist_list)

    if dist_index == len(dist):
        return -1

    # dist_index 포함
    res = []
    # 시계방향
    for i in range(len(weak)):
        new_weak = []
        for j in range(len(weak)):
            if weak[i] + dist[dist_index] >= n:
                # weak[i] ~ n - 1, 0 ~ weak[i] + dist[dist_index] - n 빼고 포함
                if weak[i] + dist[dist_index] - n < weak[j] < weak[i]:
                    new_weak.append(weak[j])
            else:
                if weak[j] < weak[i] or weak[j] > weak[i] + dist[dist_index]:
                    new_weak.append(weak[j])

        r = find(n, new_weak, dist, dist_index + 1, dist_list + [dist_index])
        if r != -1:
            res.append(r)

    # print('res',res)
    res_min = -1
    if len(res):
        res_min = min(res)

    return res_min

def solution(n, weak, dist):
    answer = -1

    dist.sort(reverse=True)

    res = []
    for pcnt in range(1,len(dist)+1):
        cur_weak = weak[:]
        new_weak = []
        for dindex in range(pcnt):
            for i in range(len(cur_weak)):
                for j in range(len(cur_weak)):
                    if 




    for i in range(len(weak)):
        new_weak = []
        for j in range(len(weak)):
            if weak[i] + dist[dist_index] >= n:
                # weak[i] ~ n - 1, 0 ~ weak[i] + dist[dist_index] - n 빼고 포함
                if weak[i] + dist[dist_index] - n < weak[j] < weak[i]:
                    new_weak.append(weak[j])
            else:
                if weak[j] < weak[i] or weak[j] > weak[i] + dist[dist_index]:
                    new_weak.append(weak[j])

        r = find(n, new_weak, dist, dist_index + 1, dist_list + [dist_index])
        if r != -1:
            res.append(r)

    # print('res',res)
    res_min = -1
    if len(res):
        res_min = min(res)









    answer = find(n, weak, dist, 0, [])





    return answer







# n =12
# weak =[1, 5, 6, 10]
# dist =[1, 2, 3, 4]
n =12
weak =[1, 3, 4, 9, 10]
dist =[3, 5, 7]

print(solution(n, weak, dist))




print('time',time.time_ns()-ptime)

