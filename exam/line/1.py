def solution(student, k):
    total = 0
    li = ''.join([str(i) for i in student]).split('1')
    print(li)
    for i in range(len(li) - k):
        cur = (len(li[i]) + 1) * (len(li[i+k]) + 1)
        print(cur)
        total += cur

    return total

if __name__ == '__main__':
    # student = [0,1,0,0]
    # k = 1

    # student = [0, 1, 0, 0, 1, 1, 0]
    # k = 2

    # student = [0, 1, 0]
    # k = 2

    student = [0, 1, 0, 0, 1, 1, 0,1]
    k = 3

    print(solution(student,k))


