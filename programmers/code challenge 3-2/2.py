

def solution(n, left, right):
    answer = []

    for a in range(left, right + 1):
        i = a // n
        j = a - i * n
        answer.append(max(i + 1, j + 1))

    return answer



if __name__ == '__main__':
    n = 3
    left = 2
    right = 5

    print(solution(n, left, right))

