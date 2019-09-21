# S : 1제곱
# D : 2제곱
# T : 3제곱
# '*' : (현재 + 이전) *2
# '#' : 현재 * (-1)
# '*' 중첩가능
# '* #' 중첩가능


def solution(dartResult):
    answer = 0

    score = [0 for _ in range(3)]
    i = 0
    j = 0
    while i < 3:
        if dartResult[j] == '1' and dartResult[j + 1] == '0':
            score[i] = 10
            j += 2
        else:
            score[i] = int(dartResult[j])
            j += 1

        if dartResult[j] == 'S':
            score[i] = score[i] ** 1
        elif dartResult[j] == 'D':
            score[i] = score[i] ** 2
        elif dartResult[j] == 'T':
            score[i] = score[i] ** 3
        j += 1

        if j < len(dartResult) and dartResult[j] in ['*', '#']:
            if dartResult[j] == '*':
                if i > 0:
                    score[i-1] *= 2
                    score[i] *= 2
                else:
                    score[i] *= 2
            else:
                score[i] *= -1
            j += 1

        i += 1

    for i in range(3):
        answer += score[i]

    return answer

def debug_print(val):
    print(val)


print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))



