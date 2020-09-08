#


def solution(str1, str2):
    answer = 0

    str1_list = []
    str2_list = []

    for i in range(len(str1)-1):
        str_part = (str1[i]+str1[i+1]).lower()
        is_alphabet = True
        for i in range(len(str_part)):
            if str_part[i] < 'a' or  str_part[i] > 'z':
                is_alphabet = False
        if is_alphabet:
            str1_list.append(str_part)
    for i in range(len(str2)-1):
        str_part = (str2[i]+str2[i+1]).lower()
        is_alphabet = True
        for i in range(len(str_part)):
            if str_part[i] < 'a' or  str_part[i] > 'z':
                is_alphabet = False
        if is_alphabet:
            str2_list.append(str_part)

    print(str1_list)
    print(str2_list)

    if len(str1_list) == len(str2_list) == 0:
        return 1 * 65536

    equal_list = []
    index = 0
    while index < len(str1_list):
        ele = str1_list[index]
        if ele in str2_list:
            str1_list.remove(ele)
            str2_list.remove(ele)
            equal_list.append(ele)
        else:
            index += 1
    print('equal_list', equal_list)

    print('str1_list',str1_list)
    print('str2_list',str2_list)

    sum_list = list(equal_list)
    for ele in str1_list:
        sum_list.append(ele)
    for ele in str2_list:
        sum_list.append(ele)
    print('sum_list', sum_list)

    answer = int(len(equal_list) / len(sum_list) * 65536)

    return answer


print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))

