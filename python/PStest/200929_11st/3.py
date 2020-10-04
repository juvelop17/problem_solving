

import time
ptime = time.time_ns()






# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # print('len(A)',len(A))
    answer = 0

    num_list = [] # 중복된 숫자들
    num_set = set()
    for a in A:
        if a not in num_set:
            num_set.add(a)
        else:
            num_list.append(a)
    num_list.sort()
    # print('num_list',num_list)

    new_list = [] # 없는 숫자들
    for i in range(1,len(A)+1):
        if i not in num_set:
            new_list.append(i)
    # print('new_list',new_list)

    for i in range(len(num_list)):
        answer += abs(num_list[i] - new_list[i])

    # print(answer)
    if answer > 1000000000:
        return -1

    return answer





# A = [1, 2, 1]
# A = [2, 1, 4, 4]
# A = [6, 2, 3, 5, 6, 3]
# A = [6, 2, 3, 5, 6, 3,6, 2, 3, 5, 6, 3,6, 2, 3, 5, 6, 3,6, 2, 3, 5, 6, 3]
A = [1 for _ in range(20000)]
print('answer', solution(A))

print('time',(time.time_ns()-ptime)/1000)










