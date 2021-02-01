
from collections import deque

def requestsServed(timestamp, top):
    # Write your code here



    deq = deque()
    top_idx = 0
    cnt = 0
    timestamp.sort()
    top.sort()
    # print(timestamp)
    # print(top)

    for time_idx in range(len(timestamp)):
        # print('1top_idx, time_idx, cnt, deq : ', top_idx, time_idx, cnt, deq)
        sw = False
        if timestamp[time_idx] <= top[top_idx]:
            deq.append(timestamp[time_idx])
            continue
        else:
            sw = True

        while top_idx < len(top) and timestamp[time_idx] >= top[top_idx]:
            for i in range(5):
                if deq:
                    deq.pop()
                    cnt += 1
            # print('1top_idx, time_idx, cnt, deq : ', top_idx, time_idx, cnt, deq)
            top_idx += 1

        if sw:
            deq.append(timestamp[time_idx])

        if top_idx == len(top):
            break

        # print()

    while top_idx < len(top):
        # print('2top_idx, time_idx, cnt, deq : ', top_idx, time_idx, cnt, deq)
        for i in range(5):
            if deq:
                deq.pop()
                cnt += 1
        top_idx += 1
        # print()

    # print('3top_idx, time_idx, cnt, deq : ', top_idx, time_idx, cnt, deq)

    return cnt




# 5
timestamp = [0,1,1,2,4,5]
top = [5]

# 9
# timestamp = [1,2,2,3,4,5,6,6,13,16]
# top = [10,15]

# 5
# timestamp = [2,2,4,8,11,28,30]
# top = [0,5,5,15]

# 17
# timestamp = [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# top = [6,6,6,6]

#
# timestamp = [1,2,2,2,2,2,2,2,2,2,2,2,2,2]
# top = [1,2,2]



# 6, 7, 9, 10, 11, 12, 14

test_cases =    [
    [[0,1,1,2,4,5], [5], 5],
    [[1,2,2,3,4,5,6,6,13,16], [10,15], 9],
    [[2,2,4,8,11,28,30], [0,5,5,15], 5],
    [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [6,6,6,6], 17],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [30], 5],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [20], 5],
    # tc6
    [[54, 52, 34, 42, 30, 25, 36, 29, 49, 23, 30, 29, 58, 21, 33, 6, 25, 16, 26, 38, 5, 24, 30, 21, 21, 13, 13, 50, 8, 8, 31, 23, 16, 59, 16, 39, 36, 17, 35, 2, 4], [20, 22, 28, 43, 57, 57], 30],
    # tc7
    [[2, 55, 55, 12, 30, 53, 50, 3, 28, 55, 23, 30, 38, 55, 4, 12, 18, 36, 33, 2, 25, 38, 33, 16, 33, 42, 25, 16, 59, 35, 8, 38, 18, 40, 53, 42, 23, 19, 53, 46], [34], 5],
    # tc9
    [[1, 1, 1, 1, 1, 1, 2], [1, 1], 6]
    ]


for tc in test_cases:
    timestamp, top, ans = tc
    res = requestsServed(timestamp, top)
    print(ans, res, ans == res)


