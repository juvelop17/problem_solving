# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6

    candi = set()
    word_dict = {}
    for curlen in range(1, len(S)+1):
        for start in range(len(S)-curlen+1):
            curword = S[start:start+curlen]
            # print("start,curlen,curword",start,curlen,curword)
            if curword not in word_dict:
                word_dict[curword] = 0
                candi.add(curword)
            word_dict[curword] += 1
            if word_dict[curword] == 2:
                candi.remove(curword)

    # print(candi)
    minlen = 10*9
    for cand in candi:
        if len(cand) < minlen:
            minlen = len(cand)

    return minlen







S = "abaaba"
# S = "zyzyzyz"
# S = "aabbbabaaa"
# S = ""


print(solution(S))
