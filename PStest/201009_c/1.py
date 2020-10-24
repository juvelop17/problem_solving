





# N = 10
N = 14

def convert(n, base):
    T = "0123456789"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(N):
    max_sum = -1
    max_k = -1
    for i in range(2,10):
        num = convert(N,i)
        sum = 1
        for n in num:
            if n != '0':
                sum *= int(n)
        if max_sum <= sum:
            max_sum = sum
            max_k = i

    return [max_k, max_sum]

print(solution(N))












