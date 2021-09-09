

def reverse(p):
    s = ''
    for i in range(len(p)):
        if p[i] == '(':
            s += ')'
        else:
            s += '('
    return s

def correct(p):
    depth = 0
    for ch in p:
        if ch == '(':
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return True

def solution(p):
    if len(p) == 0:
        return ''
    s = 0
    depth = 0
    u = ''
    v = ''
    for i in range(len(p)):
        if p[i] == '(':
            depth += 1
        else:
            depth -= 1
        if depth == 0:
            u = p[s:i+1]
            v = p[i+1:]
            break

    if correct(u):
        return u + solution(v)

    return '(' + solution(v) + ')' + reverse(u[1:-1])


if __name__ == '__main__':
    # p = "(()())()"
    # p = ")("
    p = "()))((()"

    print(solution(p))







