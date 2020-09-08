# 가사에 사용된 모든 단어들이 담긴 배열 words와
# 찾고자 하는 키워드가 담긴 배열 queries가 주어질 때,
# 각 키워드 별로 매치된 단어가 몇 개인지 순서대로 배열에 담아 반환하도록
# solution 함수를 완성해 주세요.

# 가사 단어 제한사항
# words의 길이(가사 단어의 개수)는 2 이상 100,000 이하입니다.
# 각 가사 단어의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
# 전체 가사 단어 길이의 합은 2 이상 1,000,000 이하입니다.
# 가사에 동일 단어가 여러 번 나올 경우 중복을 제거하고 words에는 하나로만 제공됩니다.
# 각 가사 단어는 오직 알파벳 소문자로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정합니다.

# 검색 키워드 제한사항
# queries의 길이(검색 키워드 개수)는 2 이상 100,000 이하입니다.
# 각 검색 키워드의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
# 전체 검색 키워드 길이의 합은 2 이상 1,000,000 이하입니다.
# 검색 키워드는 중복될 수도 있습니다.
# 각 검색 키워드는 오직 알파벳 소문자와 와일드카드 문자인 '?' 로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정합니다.
# 검색 키워드는 와일드카드 문자인 '?'가 하나 이상 포함돼 있으며,
# '?'는 각 검색 키워드의 접두사 아니면 접미사 중 하나로만 주어집니다.
# 예를 들어 "??odo", "fro??", "?????"는 가능한 키워드입니다.
# 반면에 "frodo"('?'가 없음), "fr?do"('?'가 중간에 있음), "?ro??"('?'가 양쪽에 있음)는 불가능한 키워드입니다.


def solution(words, queries):
    answer = []

    for query in queries:
        cnt = 0
        for word in words:
            if checkWord(word,query):
                cnt += 1
        answer.append(cnt)

    return answer


def checkWord(word,query):
    queStart = 0
    queEnd = len(query)-1

    prevChar = None
    currChar = None
    for i in range(len(query)):
        currChar = query[i]
        if currChar == '?' and prevChar != '?':
            queStart = i
        if prevChar == '?' and currChar != '?':
            queEnd = i-1

        prevChar = currChar
    # print('question',word,query,queStart,queEnd)

    if queStart == 0:
        quesLen = queEnd - queStart + 1
        queryStr = query[queEnd + 1:]

        findIndex = word.find(queryStr,0)
        while findIndex != -1:
            # print('findIndex',findIndex,word[:findIndex],quesLen)
            if len(word[:findIndex]) - quesLen == 0:
                return True
            findIndex = word.find(queryStr,findIndex+1)
    else:
        quesLen = queEnd - queStart + 1
        queryStr = query[:queStart]

        findIndex = word.find(queryStr,0)
        while findIndex != -1:
            # print('findIndex',findIndex,word[findIndex+queStart:],quesLen)
            if len(word[findIndex+queStart:]) - quesLen == 0:
                return True
            findIndex = word.find(queryStr,findIndex+1)

    return False






print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))
# print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))

