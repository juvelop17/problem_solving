

def solution(N, map):
    print(N)
    print(map)

f = open("2383_sample_input.txt", "r")
T = int(f.readline().strip())
N = int(f.readline().strip())

# T = int(input())
# N = int(input())

for tc in range(T):
    map_list = [[] for _ in range(N)]

    for i in range(N):
        _l = f.readline().strip().split(' ')
        map_list[i] = list(map(int, _l))

    solution(N, map_list)

f.close()












