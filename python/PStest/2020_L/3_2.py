


def calnum(cnt, num_str):
    res_cnt = -1
    res_num = -1

    # print('cnt, num_str',cnt, num_str)
    if len(num_str) == 1:
        return cnt, int(num_str)

    res_list = []
    for ind in range(1,len(num_str)):
        num_str1 = num_str[:ind]
        num_str2 = num_str[ind:]
        if num_str2[0] == '0':
            continue
        new_num = int(num_str1) + int(num_str2)
        # print('new_num', new_num)
        cnt1, num1 = calnum(cnt+1, str(new_num))
        res_list.append([cnt1,num1])
    # print(res_list)

    res_list.sort()
    return res_list[0]

def solution(n):
    answer = []

    num_str = str(n)
    cnt, num = calnum(0, num_str)
    answer = [cnt, num]

    return answer


# n = 73425
# n = 10007
n = 9

print(solution(n))


