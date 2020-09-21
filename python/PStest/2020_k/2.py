
import sys
import time

sys.stdin = open('input2.txt','r')
read = sys.stdin.readline
prev_time = time.time_ns()

def reverseParenthesis(s):
    new_str = ''
    for c in s:
        if c == '(':
            new_str += ')'
        else:
            new_str += '('
    return new_str

def findParenthesis(p):
    result = ''
    cur_cnt = 0  # 양수 : (  //  음수 : )
    u = p[:]
    v = ''

    if p == '':
        return ''

    for i in range(len(p)):
        if p[i] == '(':
            cur_cnt += 1
        else:
            cur_cnt -= 1

        # print(i, ' ', cur_cnt)
        if cur_cnt == 0:
            u = p[:i+1]
            v = p[i+1:]
            break

    # print('u: ', u , '\tv: ', v)
    if u[0] == '(':
        result = u + findParenthesis(v)
    else:
        result = '(' + findParenthesis(v) + ')' + reverseParenthesis(u[1:-1])
    return result

def solution(p):
    return findParenthesis(p)


for _ in range(5):
    s = read().strip()
    print(s)
    print(solution(s))

print('time', time.time_ns()-prev_time)