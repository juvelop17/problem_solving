import sys
import time

ptime = time.time_ns()

sys.stdin = open('picnic.in', 'r')
sys.stdout = open('picnic.res', 'w')


#####################################################

def find(friends, sel):
    n = len(sel)
    ci = -1
    for i in range(n):
        if sel[i] == 0:
            ci = i
            break
    if ci == -1:
        return 1

    cnt = 0
    for ni in friends[ci]:
        if sel[ni] == 0:
            sel[ci] = sel[ni] = 1
            cnt += find(friends, sel)
            sel[ci] = sel[ni] = 0
    return cnt

def solution(n, m, relations):
    friends = [[] for _ in range(n)]
    for r in relations:
        friends[r[0]].append(r[1])
        friends[r[1]].append(r[0])

    sel = [0 for _ in range(n)]
    return find(friends, sel)

t = int(input())
for tt in range(t):
    n, m = map(int, input().split())
    r = list(map(int, input().split()))
    relations = []
    for i in range(0,len(r),2):
        relations.append((r[i],r[i+1]))
    print(solution(n, m, relations))

#####################################################


# print('time', time.time_ns() - ptime)

