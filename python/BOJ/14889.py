import sys
import time

prev_time = time.time_ns()
sys.stdin = open('input.txt','r')
read = sys.stdin.readline


def solution():
    min_val = 10**8

    for a in res_comb:
        b = list(set(li)-set(a))
        sum_a = 0
        for i in a:
            for j in a:
                sum_a += S[i][j]

        sum_b = 0
        for i in b:
            for j in b:
                sum_b += S[i][j]

        min_val = min(min_val,abs(sum_a-sum_b))

    return min_val


def combination(start):
    if len(pick) == N/2:
        res_comb.append(pick[:])
        return

    for i in range(start,N):
        if memory_comb[i] == 0:
            pick.append(li[i])
            memory_comb[i] = 1
            combination(i+1)
            memory_comb[i] = 0
            pick.pop()

N = int(read().strip())
S = []
for _ in range(N):
    S.append(list(map(int,read().strip().split())))

S_memory = []
for i in range(N):
    S_memory.append([0 for _ in range(i)])
    for j in range(i,N):
        S_memory[i].append(S[i][j]+S[j][i])

pick=[]
memory_comb=[0 for _ in range(N)]
res_comb = []
li = [i for i in range(N)]
combination(0)

print(solution())
print('time',time.time_ns()-prev_time)

