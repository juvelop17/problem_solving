import time

prev_time = time.time_ns()

from itertools import combinations

def solution(orders, course):
    answer = []

    dict_list = [{} for _ in range(11)]

    for order in orders:
        part_order = []
        for i in range(1,len(order)+1):
            part_order.extend(combinations(order,i))
        # print(part_order)

        for part in part_order:
            # part_str = ''.join(set(part))
            part_str = ''.join(sorted(part))
            print(part_str)
            if part_str not in dict_list[len(part_str)]:
                dict_list[len(part_str)][part_str] = 0
            dict_list[len(part_str)][part_str] += 1
        # print(dict_list)

    for cour in course:
        sorted_order = sorted(dict_list[cour].items(), key=lambda x:x[1],reverse=True)
        # print('sorted_order', cour, sorted_order)

        if len(sorted_order) == 0:
            continue
        max_num = sorted_order[0][1]
        if max_num < 2:
            continue
        for order in sorted_order:
            # print(order)
            if max_num != order[1]:
                break
            answer.append(order[0])

    answer.sort()

    return answer


# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course = [2,3,4]

# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course = [2,3,5]

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

print(solution(orders, course))


print('time', time.time_ns()-prev_time)



