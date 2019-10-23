import sys
# import time


# prev_time = time.time()
# sys.stdin = open('input.txt','r')
read = sys.stdin.readline

def solution():
    li.sort()

    arr = []
    cnt = 0
    for i in range(n):
        new_num = li[i]

        is_added = False
        for j in range(len(arr)):
            comp_num = arr[j][-1]
            if abs(comp_num-new_num) != 1:
                arr[j].append(new_num)
                is_added = True
                break

        if is_added == False:
            arr.append([])
            arr[-1].append(new_num)
            cnt += 1
    return cnt


q = int(read().strip())
for i in range(q):
    n = int(read().strip())
    li = list(map(int,read().strip().split()))
    print(solution())
# print('time',time.time()-prev_time)

