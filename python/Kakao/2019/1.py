# 문자가 반복되지 않아 한번만 나타난 경우 1은 생략함
# 압축할 문자열 s가 매개변수로 주어질 때,
# 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여
# 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록
# solution 함수를 완성해주세요.

def solution(s):
    answer = 0

    # print('s:',s)
    resultStrList = []

    if len(s) == 1:
        return 1
    for step in range(1,len(s)//2+1):
        currStr = ''
        prevStr = ''
        resultStr = ''
        cnt = 1
        # print('step:',step)
        for index in range(0,len(s),step):
            currStr = s[index:index+step]
            if currStr == prevStr:
                cnt +=1
            else:
                if cnt != 1:
                    resultStr += str(cnt) + prevStr
                else:
                    resultStr += prevStr
                prevStr = currStr
                cnt = 1

        if cnt != 1:
            resultStr += str(cnt) + prevStr
        else:
            resultStr += currStr
        # print(resultStr)
        resultStrList.append(resultStr)

    minStr = resultStrList[0]
    for r in resultStrList:
        if len(r) < len(minStr):
            minStr = r

    answer = len(minStr)

    return answer




print(solution("a"))
print(solution("aaa"))
# print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))
