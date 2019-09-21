#!/bin/python3

import math
import os
import random
import re
import sys

result_lists = []

# Complete the arrangements function below.
def arrangements(n):
    answer = 0

    # index 별 가능한 숫자 리스트
    index_possible_num = [[] for _ in range(n + 1)]  # index 0은 사용안함
    for i in range(1, n + 1):
        index_possible_num[i] = []
        for j in range(1, n + 1):
            if i % j == 0 or j % i == 0:
                index_possible_num[i].append(j)
    print(index_possible_num)

    # recursive로 구현
    cur_list = [-1]
    recur(n, index_possible_num, 1, list(cur_list))

    # print_result_list(n)
    answer = len(result_lists)

    return answer

def recur(n, index_possible_num, cur_index, cur_list):
    print(id(cur_list), cur_list)

    if n < cur_index:
        result_lists.append(cur_list)
        return

    for num in index_possible_num[cur_index]:
        if num not in cur_list:
            li = list(cur_list)
            li.append(num)
            recur(n, index_possible_num, cur_index + 1, li)

    return

def print_result_list(n):
    for li in result_lists:
        print(li)


if __name__ == '__main__':
    res = arrangements(11)

    # n = int(input().strip())
    # res = arrangements(n)
    print(res)
