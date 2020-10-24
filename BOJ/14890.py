import sys
import time


prev_time = time.time_ns()
# sys.stdin = open('input1.txt','r')
read = sys.stdin.readline

def solution():
    cnt = 0

    for i in range(2*N):
        memory_arr = [0 for _ in range(N)]
        if i < N:
            for j in range(1,N):
                curr_height = arr[i][j - 1]
                next_height = arr[i][j]

                if abs(curr_height-next_height) > 1:
                    break

                if curr_height < arr[i][j]:
                    is_poss = True
                    for l in range(1,L+1):
                        if not (j-l >= 0 and
                                curr_height == arr[i][j-l] and
                                memory_arr[j-l] == 0):
                            is_poss = False
                    if is_poss == False:
                        break
                    else:
                        for l in range(1, L + 1):
                            memory_arr[j-l] = 1

                if curr_height > arr[i][j]:
                    is_poss = True
                    for l in range(L):
                        if not (j+l < N and next_height == arr[i][j+l]):
                            is_poss = False
                    if is_poss == False:
                        break
                    else:
                        for l in range(L):
                            memory_arr[j+l] = 1

                if j == N-1:
                    cnt+=1

        else:
            new_i = i-N
            for j in range(1, N):
                curr_height = arr[j - 1][new_i]
                next_height = arr[j][new_i]

                if abs(curr_height - next_height) > 1:
                    break

                if curr_height < arr[j][new_i]:
                    is_poss = True
                    for l in range(1, L + 1):
                        if not (j - l >= 0 and
                                curr_height == arr[j - l][new_i] and
                                memory_arr[j - l] == 0):
                            is_poss = False
                    if is_poss == False:
                        break
                    else:
                        for l in range(1, L + 1):
                            memory_arr[j - l] = 1

                if curr_height > arr[j][new_i]:
                    is_poss = True
                    for l in range(L):
                        if not (j + l < N and next_height == arr[j + l][new_i]):
                            is_poss = False
                    if is_poss == False:
                        break
                    else:
                        for l in range(L):
                            memory_arr[j + l] = 1

                if j == N - 1:
                    cnt += 1


    return cnt

N, L = map(int,read().strip().split())
arr = [list(map(int,read().strip().split())) for _ in range(N)]
memory_arr = [[0 for _ in range(N)] for _ in range(N)]

print(solution())
# print('time',time.time_ns() - prev_time)







