



# 유니온 파인드
nparent = {}
eparent = {}
idxDict = {}


def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(parent, x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    parent[x] = y


def check(nicks, emails, i, j):
    if (nicks[i] == nicks[j] and emails[i] == emails[j]):
        return True

    iidx = 0
    jidx = 0
    idx = 0

    while (idx + iidx < len(nicks[i]) and idx + jidx < len(nicks[j])):
        if (nicks[i][idx + iidx] != nicks[j][idx + jidx]):
            if (len(nicks[i]) > len(nicks[j])):
                iidx += 1
                jidx += 0
            elif (len(nicks[i]) < len(nicks[j])):
                iidx += 0
                jidx += 1
            else:
                iidx += 1
                jidx += 1
            if iidx + jidx > 2:
                return False
            continue
        idx += 1

    while (idx + iidx < len(emails[i]) and idx + jidx < len(emails[j])):
        if (emails[i][idx + iidx] != emails[j][idx + jidx]):
            if (len(emails[i]) > len(emails[j])):
                iidx += 1
                jidx += 0
            elif (len(emails[i]) < len(emails[j])):
                iidx += 0
                jidx += 1
            else:
                iidx += 1
                jidx += 1
            if iidx + jidx > 2:
                return False
            continue
        idx += 1

    return True

def solution(nicks, emails):
    answer = -1
    n = len(nicks)
    
    # # 유니온 파인드 초기화
    # for i in range(n):
    #     nparent[nicks[i]] = nicks[i]
    #     idxDict[nicks[i]] = i
    # for i in range(n):
    #     eparent[emails[i]] = emails[i]
    #     idxDict[emails[i]] = i

    for i in range(n):
        for j in range(i+1,n):
            if check(nicks, emails, i, j):
                print(i, j)


    return answer


if __name__ == '__main__':
    nicks = ["imhero111", "moneyman", "hero111", "imher1111", "hro111", "mmoneyman", "moneymannnn"]
    emails = ["superman5@abcd.com", "batman432@korea.co.kr", "superman@abcd.com", "supertman5@abcd.com", "superman@erty.net", "batman42@korea.co.kr", "batman432@usa.com"]
    solution(nicks, emails)

