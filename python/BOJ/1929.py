# import time
# startTime = time.time()

def solution(M, N):
    answer = None

    prime_list = {i for i in range(2, N+1)}

    for num in range(2, N+1):
        if num not in prime_list:
            continue
        # print(prime_list)
        # print(num)
        for j in range(2, int(N / num) + 1):
            try:
                prime_list.remove(num * j)
            except:
                pass

    for i in range(2, M):
        try:
            prime_list.remove(i)
        except:
            pass

    answer = prime_list

    return answer


M, N = input().strip().split(' ')
M = int(M)
N = int(N)

answer = solution(M, N)
# print(type(sorted(answer)))
for i in sorted(answer):
    print(i)

# endTime = time.time() - startTime
# print('Time', endTime)
