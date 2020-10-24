#!/bin/python3

import math
import os
import random
import re
import sys
import time

result_lists = []
index_possible_num = []
cnt = 0

# Complete the arrangements function below.
def arrangements(n):
    global cnt
    global index_possible_num

    answer = 0

    # index 별 가능한 숫자 리스트
    index_possible_num = [[] for _ in range(n + 1)]  # index 0은 사용안함
    for i in range(1, n + 1):
        index_possible_num[i] = []
        for j in range(1, n + 1):
            if i % j == 0 or j % i == 0:
                index_possible_num[i].append(j)
    # print(index_possible_num)

    # recursive로 구현
    cur_list = [-1 for _ in range(n + 1)]
    recur(n, 1, cur_list)

    # print_result_list(n)
    # answer = len(result_lists)
    answer = cnt

    return answer

def recur(n, cur_index, cur_list):
    global cnt
    global index_possible_num

    # print(id(cur_list), cur_list, cur_index)
    temp_index_possible_num = list(set(index_possible_num[cur_index]) - set(cur_list[:cur_index]))

    # print("index_possible_num[cur_index]", index_possible_num[cur_index])
    # print("temp_index_possible_num", temp_index_possible_num)

    for num in temp_index_possible_num:
        cur_list[cur_index] = num
        if (cur_index < n):
            recur(n, cur_index + 1, cur_list)
        else:
            cnt += 1


    return


def print_result_list(n):
    for li in result_lists:
        print(li)


if __name__ == '__main__':
    start_time = time.time()
    res = arrangements(19)
    print("--- %s seconds ---" % (time.time() - start_time))

    # n = int(input().strip())
    # res = arrangements(n)
    print(res)
