import sys
# import time


# prev_time = time.time()
# sys.stdin = open('input1.txt','r')
read = sys.stdin.readline

def solution():
    f = set()

    if len(st) == 1:
        f.add(st[0])
    else:
        if st[0] != st[1]:
            f.add(st[0])
        if st[-2] != st[-1]:
            f.add(st[-1])

    prev = st[0]
    i = 1
    cnt = 1
    while i < len(st):
        curr = st[i]
        if prev != curr:
            if cnt % 2 == 1 :
                f.add(prev)
            else:
                prev = curr
            cnt = 1
        else:
            cnt += 1
            if i == len(st)-1 and cnt % 2 == 1:
                f.add(prev)
        prev = curr
        i+=1

    return sorted(f)


q = int(read().strip())
for i in range(q):
    st = read().strip()
    sol = solution()
    for s in sol:
        print(s,end='')
    print()
# print('time',time.time()-prev_time)

