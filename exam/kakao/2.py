

import math

def check(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def toNum(nstr, k):
    nsum = 0
    for i in range(len(nstr)):
        nsum += int(nstr[i]) * k**(len(nstr) - i - 1)
    return nsum

def digit(n, k):
    nstr = ''
    while n != 0:
        q = n % k
        nstr = str(q) + nstr
        n = n // k
    return nstr

def solution(n, k):
    nstr = digit(n, k)
    print(nstr)
    li = nstr.split('0')
    print(li)

    cnt = 0
    for l in li:
        if l != '' and check(int(l)):
            cnt += 1

    return cnt



if __name__ == '__main__':
    # n = 437674
    # k = 3

    # n = 110011
    # k = 10

    n = 1000000
    k = 3

    print(solution(n, k))






