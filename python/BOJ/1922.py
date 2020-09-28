
import sys
sys.stdin = open('input.txt','r')
read = sys.stdin.readline


class Edge:
    def __init__(self, u, v, w):
        self.u = u-1
        self.v = v-1
        self.w = w

    def __str__(self): # print 시 출력
        return 'u: {}, v: {}, w: {}'.format(self.u,self.v,self.w)


## Union find 활용
def find(a):
    if union_find_list[a] < 0:
        return a
    union_find_list[a] = find(union_find_list[a])
    return union_find_list[a]

def merge(a, b):
    # print('a, b:',a,b)
    # print('union_find_list',union_find_list)
    a = find(a)
    b = find(b)
    if a == b:
        return False
    union_find_list[b] = a
    return True
##

def solution():
    edges = []
    for edge_info in edge_infos:
        edges.append(Edge(*edge_info))

    edges.sort(key=lambda x:x.w) # class의 sorting key 설정
    # for edge in edges:
    #     print(edge)

    result = cnt = cur = 0
    while cnt < N-1:
        # print(edges[cur])
        if merge(edges[cur].u, edges[cur].v):
            result += edges[cur].w
            cnt += 1
        cur += 1

    return result


N = int(read())
M = int(read())
edge_infos = []
for _ in range(M):
    edge_infos.append(list(map(int,read().split())))

union_find_list = [-1 for _ in range(N)]

print(solution())
