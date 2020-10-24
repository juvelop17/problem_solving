# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    answer = -1

    total_cnt = 0
    acnt = 0
    if len(S) == 1:
        if S == 'a':
            return 1
        else:
            return 4

    if S[0] != 'a':
        total_cnt += 2
    for i in range(len(S)-1):
        if S[i] == 'a' and S[i+1] == 'a':
            acnt += 1
            if acnt == 2:
                return -1
        elif S[i] == 'a':
            if acnt == 0:
                total_cnt += 1
            acnt = 0
        elif S[i+1] == 'a':
            pass
        else:
            total_cnt += 2
    if S[-2] != 'a' and S[-1] == 'a':
        total_cnt += 1
    elif S[-1] != 'a':
        total_cnt += 2

    answer = total_cnt

    return answer



# S = 'aabab'
# S = 'dog'
# S = 'aa'
# S = 'baaaa'
# S = 'aaa'
# S = 'b'
# S = 'a'
# S = 'sas'
# S = 'ssa'
# S = 'ass'
# S = 'sa'
S = 'as'

print(solution(S))




