import heapq
from collections import deque

def solution(ball, order):
    answer = []

    ball_heap = []
    ball_deque = deque(ball)
    # print(ball_deque)

    temp_list = []

    for i in range(len(order)):
        if ball_deque[0] == order[i]:
            answer.append(ball_deque.popleft())
        elif ball_deque[-1] == order[i]:
            answer.append(ball_deque.pop())
        else:
            heapq.heappush(ball_heap, [i, order[i]])
            # print(ball_heap)

        while len(ball_heap) > 0:
            index, ball_num = heapq.heappop(ball_heap)
            if ball[0] == order[i]:
                answer.append(ball_deque.popleft())
            elif ball[-1] == order[i]:
                answer.append(ball_deque.pop())
            else:
                temp_list.append([index, ball_num])
        while len(temp_list) > 0:
            heapq.heappush(ball_heap, temp_list.pop())

    return answer

# ball = [1, 2, 3, 4, 5, 6]
# order =[6, 2, 5, 1, 4, 3]
#
ball = [11, 2, 9, 13, 24]
order =[9, 2, 13, 24, 11]

print(solution(ball,order))

print()