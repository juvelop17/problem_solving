import time

prev_time = time.time_ns()

def solution(boxes):
    answer = -1

    # print(boxes)
    # for b in boxes:
    #     b.sort()
    # boxes.sort()

    bucket = []
    for b in boxes:
        bucket.append(b[0])
        bucket.append(b[1])
    bucket.sort()
    # print(bucket)

    box_cnt = 0
    next_bucket = []
    while 1 < len(bucket):
        if bucket[0] == bucket[1]:
            box_cnt += 1
            bucket.pop(0)
            bucket.pop(0)
        else:
            next_bucket.append(bucket.pop(0))
        # print(bucket, next_bucket)
    if len(bucket) != 0:
        next_bucket.append(bucket.pop(0))
    # print(box_cnt, bucket, next_bucket)

    answer = int(len(next_bucket)/2)

    return answer

# boxes = [[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]
# boxes = [[1, 2], [3, 4], [5, 6]]
# boxes = [[1, 2], [2, 3], [3, 1]]
# boxes = [[4, 1], [1, 1], [6, 2]]
boxes = [[1, 1], [1, 1], [6, 1]]
print(solution(boxes))

print('time', time.time_ns()-prev_time)
