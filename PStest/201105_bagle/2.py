import time

ptime = time.time_ns()

# import sys
# sys.stdin = open('input.txt','r')


#####################################################

# N = 7
# relation = [[1,2],[2,5],[2,6],[1,3],[1,4],[3,7]]
# dirname = ["root","abcd","cs","hello","etc","hello","solution"]


N = 7
relation = [[1,2],[2,3],[3,4],[4,5],[1,6],[6,7]]
dirname = ["root","a","b","c","d","efghij","k"]



from collections import deque

def solution(N, relation, dirname):
    answer = 0

    edge = [[] for _ in range(N)]
    for r in relation:
        edge[r[0]-1].append(r[1])
    # print(edge)

    max_len = -1

    que = deque()
    cnum = 1
    clen = 0
    que.append((cnum, clen))
    while que:
        cnum, clen = que.popleft()
        # print('cnum, clen',cnum, clen)
        nlen = clen + len(dirname[cnum-1])
        if nlen > max_len:
            # print(nlen, max_len)
            max_len = nlen

        for nnum in edge[cnum-1]:
            que.append((nnum,nlen+1))
    # print('max_len',max_len)

    answer = max_len
    return answer


print(solution(N, relation, dirname))


#####################################################

print('time',time.time_ns()-ptime)

