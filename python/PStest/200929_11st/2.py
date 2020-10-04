# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    answer = []

    N = len(S)
    M = len(S[0])

    for i in range(M):
        char_list = []
        for index in range(N):
            char_list.append([S[index][i], index])
        char_list.sort()
        # print(char_list)
        for j in range(len(char_list)-1):
            if char_list[j][0] == char_list[j+1][0]:
                return [char_list[j][1], char_list[j+1][1], i]

    return answer


# S = ["abc","bca","dbe"]
# S = ["zzzz","ferz","zdsr","fgtd"]
# S = ["gr","sd","rg"]
# S = ["bdafg","ceagi"]
# S = ['a','a']
# S = ['a','b','c']
S = ['ac','bb','ca']

print(solution(S))




