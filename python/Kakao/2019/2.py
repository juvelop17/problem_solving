# 대부분 소스 코드 내 작성된 괄호가 개수는 맞지만 짝이 맞지 않은 형태로
# 작성되어 오류가 나는 것을 알게 되었습니다.
# 소스 코드에 작성된 모든 괄호를 뽑아서 올바른 순서대로 배치된
# 괄호 문자열을 알려주는 프로그램을 다음과 같이 개발하려고 합니다.



# '(' 와 ')' 로만 이루어진 문자열이 있을 경우, '(' 의 개수와 ')' 의 개수가 같다면
# 이를 균형잡힌 괄호 문자열이라고 부릅니다.
# 그리고 여기에 '('와 ')'의 괄호의 짝도 모두 맞을 경우에는
# 이를 올바른 괄호 문자열이라고 부릅니다.

# 예를 들어, "(()))("와 같은 문자열은 균형잡힌 괄호 문자열 이지만 올바른 괄호 문자열은 아닙니다.
# 반면에 "(())()"와 같은 문자열은 균형잡힌 괄호 문자열 이면서 동시에 올바른 괄호 문자열 입니다.
#
# '(' 와 ')' 로만 이루어진 문자열 w가 균형잡힌 괄호 문자열 이라면 다음과 같은 과정을 통해 올바른 괄호 문자열로 변환할 수 있습니다.

# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
# 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#   4-3. ')'를 다시 붙입니다.
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#   4-5. 생성된 문자열을 반환합니다.




def solution(p):
    answer = ''

    answer = bracketRecur(p)

    return answer

def bracketRecur(_str):
    _stack = []
    isGood = True
    cnt = 0

    u=''
    v=''
    resultStr = ''

    if _str == '':
        return ''

    for i in range(len(_str)):
        if _str[i] == '(':
            # _stack.append('(')
            u+='('
            cnt += 1
        else:
            u+=')'
            cnt -= 1

        if cnt == 0:
            v = _str[i+1:]
            break
        elif cnt < 0:
            isGood = False
    #
    # print('u',u)
    # print('v',v)
    # print('isGood',isGood)

    if isGood == True:
        resultStr += u + bracketRecur(v)
        return resultStr
    else:
        resultStr+='('
        resultStr+=bracketRecur(v)
        resultStr+=')'

        uNewStr = ''
        for c in u[1:-1]:
            if c == '(':
                uNewStr += ')'
            else:
                uNewStr += '('

        resultStr+=uNewStr

        return resultStr



# print(solution("(()())()"))
# print(solution(")("))
print(solution("()))((()"))




