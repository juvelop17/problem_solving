import time

ptime = time.time_ns()

# import sys
# sys.stdin = open('input.txt','r')


#####################################################

# n = 6
# delivery = [[1,3,1],[3,5,0],[5,4,0],[2,5,0]]

n = 7
delivery = [[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]]


def solution(n, delivery):
    answer = ''

    num_list = [-1 for _ in range(n+1)]
    print(num_list)

    for deli in delivery:
        if deli[2] == 1:
            num_list[deli[0]] = 1
            num_list[deli[1]] = 1

    for deli in delivery:
        if deli[2] == 0:
            if num_list[deli[0]] == 1:
                num_list[deli[1]] = 0
            elif num_list[deli[1]] == 1:
                num_list[deli[0]] = 0

    print(num_list)

    for i in range(1,n+1):
        if num_list[i] == 1:
            answer += 'O'
        elif num_list[i] == 0:
            answer += 'X'
        elif num_list[i] == -1:
            answer += '?'

    return answer

print(solution(n, delivery))

#####################################################

print('time',time.time_ns()-ptime)

