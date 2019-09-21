import time

startTime = time.time()

def solution(M, N):
    answer = None

    prime_set = list()
    for i in range(2, N + 1):
        is_prime = False
        for j in range(2, i+1):
            if j == i:
                is_prime = True
            if i % j == 0:
                break
        if is_prime:
            prime_set.append(i)


    # for i in range(1, M):
    #     prime_set.discard(i)

    for i in prime_set:
        if i < M:
            try:
                prime_set.remove(i)
            except:
                pass

    answer = prime_set

    return answer

# M, N = input().strip().split(' ')
# M = int(M)
# N = int(N)
#
# answer = solution(M, N)
# # print(type(sorted(answer)))
# for i in sorted(answer):
#     print(i)

answer = solution(1, 10000)
# print(type(sorted(answer)))
for i in sorted(answer):
    print(i)

endTime = time.time() - startTime
print('Time',endTime)
