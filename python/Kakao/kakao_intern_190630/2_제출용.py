
import os
import sys

visited = []
tree_dict = {}
res_dict = {}

def search():
    n, q = map(int, sys.stdin.readline().strip().split(' '))

    ## 데이터 입력 ##
    for _ in range(n):
        emp = list(map(int, sys.stdin.readline().strip().split(' ')))
        emp_id = emp[0]
        boss_id = emp[1]
        res_num = emp[2]

        if boss_id not in tree_dict:
            tree_dict[boss_id] = []
        tree_dict[boss_id].append(emp_id)
        # print(tree_dict)

        if emp_id not in res_dict:
            res_dict[emp_id] = []
        for i in range(res_num):
            res_dict[emp_id].append(emp[i+3])
        # print(res_dict)


    ## DFS 처리 ##
    # for i in range(1,n+1):
    #     find_res(i)

    ## 쿼리 처리 ##
    for _ in range(q):
        query = list(map(int, sys.stdin.readline().strip().split(' ')))

        emp_id = query[0]
        res_id = query[1]

        find_res(emp_id)
        if res_id in res_dict[emp_id]:
            print('true')
        else:
            print('false')

        # if find_emp_res(emp_id,res_id):
        #     print('true')
        # else:
        #     print('false')

def find_res(emp_id):
    if emp_id in visited:
        # print('visited', emp_id)
        return res_dict[emp_id]

    if emp_id in tree_dict:
        emp_list = tree_dict[emp_id]
        for emp in emp_list:
            if emp in visited:
                res_dict[emp_id] = res_dict[emp_id] + res_dict[emp]
            else:
                res_dict[emp_id] = res_dict[emp_id] + find_res(emp)

    visited.append(emp_id)
    return res_dict[emp_id]

def find_emp_res(emp_id, res_id):
    if res_id in res_dict[emp_id]:
        return True

    if emp_id in tree_dict:
        emp_list = tree_dict[emp_id]
        for emp in emp_list:
            if find_emp_res(emp, res_id):
                return True

    return False




if __name__ == '__main__':
    search()


