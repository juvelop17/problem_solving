# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6

    unlight = set()
    cur = 0
    end = 0
    cnt = 0
    for a in A:
        # print('a,unlight,cur,end,cnt',a,unlight,cur,end,cnt)
        if end < a:
            for i in range(end+1,a):
                unlight.add(i)
            end = a
        else:
            unlight.remove(a)
        # print('a,unlight,cur,end,cnt',a,unlight,cur,end,cnt)

        if len(unlight) == 0:
            cur = end
            cnt += 1
        # print()
    # print(cnt)

    return cnt



A = [2,1,3,5,4]
# A = [2,3,4,1,5]
# A = [1,3,4,2,5]

print(solution(A))


