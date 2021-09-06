def lowerBound(arr, target):
    l = 0
    r = len(arr)

    while l < r:
        pivot = (l + r) // 2
        if arr[pivot] >= target:
            r = pivot
        else:
            l = pivot + 1
    return r


def solution(info, query):
    answer = []

    col1 = ['cpp', 'java', 'python', '-']
    col2 = ['backend', 'frontend', '-']
    col3 = ['junior', 'senior', '-']
    col4 = ['chicken', 'pizza', '-']

    dt = {}
    for c1 in col1:
        for c2 in col2:
            for c3 in col3:
                for c4 in col4:
                    dt[(c1, c2, c3, c4)] = []

    for inf in info:
        li = inf.split(' ')
        for c1 in [li[0], '-']:
            for c2 in [li[1], '-']:
                for c3 in [li[2], '-']:
                    for c4 in [li[3], '-']:
                        dt[(c1, c2, c3, c4)].append(int(li[4]))

    for c in dt:
        dt[c].sort()

    for quer in query:
        li = quer.split(' and ')
        li = li[:3] + li[3].split(' ')
        li[4] = int(li[4])

        candi = dt[(li[0], li[1], li[2], li[3])]
        idx = lowerBound(candi, li[4])

        cnt = len(candi) - idx
        answer.append(cnt)

    return answer


if __name__ == '__main__':
    info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
            "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
             "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
             "- and - and - and chicken 100", "- and - and - and - 150"]

    print(solution(info, query))


