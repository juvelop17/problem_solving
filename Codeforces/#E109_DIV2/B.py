import sys
import time

ptime = time.time_ns()

sys.stdin = open('input.txt', 'r')


#####################################################

def solution(n, nums):
    start = 0
    end = len(nums)-1

    while start < len(nums):
        if nums[start] != start + 1:
            break
        start += 1

    while end >= 0:
        if nums[end] != end + 1:
            break
        end -= 1

    if nums[0] == len(nums) and nums[-1] == 1:
        return 3
    elif start == 0 and end == len(nums) - 1:
        return 2
    elif start < end:
        return 1
    elif start > end:
        return 0
    return -1

t = int(input())
for tt in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(solution(n, nums))

#####################################################


# 5 4 3 2 1
# 2 3 4 5 1


print('time', (time.time_ns() - ptime)/10**6,'ms')
