


def calnum(cnt, num_str):
    res_cnt = -1
    res_num = -1

    print('cnt, num_str',cnt, num_str)
    if len(num_str) == 1:
        return cnt, int(num_str)

    ind = int(len(num_str)/2)
    new_num1 = int(num_str[:ind]) + int(num_str[ind:])
    cnt1, num1 = calnum(cnt+1, str(new_num1))
    print('cnt1, num1',cnt1, num1)

    res_cnt = cnt1
    res_num = num1

    return res_cnt, res_num

def solution(n):
    answer = []

    num_str = str(n)
    cnt, num = calnum(0, num_str)
    print(cnt, num)

    return answer


# n = 73425
# n = 10007
# n = 9
n = 10000

print(solution(n))


