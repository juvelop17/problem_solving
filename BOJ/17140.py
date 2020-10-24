
import time

ptime = time.time_ns()

import sys
sys.stdin = open('input.txt','r')


#####################################################

r, c, k = map(int,input().split())
A = [list(map(int, input().split())) for _ in range(3)]

def checkRange(A, i, j):
    return i >= 0 and i < len(A) and j >= 0 and j < len(A[0])

def solution(A):
    tcnt = 0
    while tcnt <= 100:
        if checkRange(A, r-1,c-1) and A[r-1][c-1] == k:
            return tcnt
        tcnt += 1

        if len(A) >= len(A[0]): # R 연산
            for i in range(len(A)):
                dict_num = {}
                for num in A[i]:
                    if num not in dict_num:
                        dict_num[num] = 0
                    dict_num[num] += 1

                sort_list = []
                for num, cnt in dict_num.items():
                    sort_list.append((cnt,num)) # (빈도, 숫자)
                sort_list.sort()

                new_li = []
                for cnt, num in sort_list:
                    if num == 0:
                        continue
                    new_li.append(num)
                    new_li.append(cnt)
                if len(new_li) > 100:
                    new_li = new_li[:100]
                A[i] = new_li

            max_len = max(map(len,A))
            for i in range(len(A)):
                if len(A[i]) < max_len:
                    A[i] += [0] * (max_len - len(A[i]))

        else: # C 연산
            col_A = list(zip(*A))

            for i in range(len(col_A)):
                dict_num = {}
                for num in col_A[i]:
                    if num not in dict_num:
                        dict_num[num] = 0
                    dict_num[num] += 1

                sort_list = []
                for num, cnt in dict_num.items():
                    sort_list.append((cnt, num))  # (빈도, 숫자)
                sort_list.sort()

                new_li = []
                for cnt, num in sort_list:
                    if num == 0:
                        continue
                    new_li.append(num)
                    new_li.append(cnt)
                if len(new_li) > 100:
                    new_li = new_li[:100]
                col_A[i] = new_li

            max_len = max(map(len, col_A))
            for i in range(len(col_A)):
                if len(col_A[i]) < max_len:
                    col_A[i] += [0] * (max_len - len(col_A[i]))
            A = list(zip(*col_A))
        # print(A)

    return -1

print(solution(A))




#####################################################

print('time',time.time_ns()-ptime)

