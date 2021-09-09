def solution(s):
    res = s
    for i in range(1, len(s)//2 + 1):
        news = ''
        cnt = 0
        idx = -1
        j = 0
        while j < len(s):
            if s[j:j+i] == s[j+i:j+i*2]:
                cnt += 1
            else:
                if cnt > 0:
                    news += str(cnt+1)
                news += s[j:j+i]
                cnt = 0
            j += i
        # print(news)
        if len(res) > len(news):
            res = news
    return len(res)


if __name__ == '__main__':
    # s = "aabbaccc"
    s = "abcabcabcabcdededededede"
    # s = "xababcdcdababcdcd"

    print(solution(s))
