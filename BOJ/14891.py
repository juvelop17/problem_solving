import sys
import time

prev_time = time.time_ns()
# sys.stdin = open('input1.txt','r')
read = sys.stdin.readline

def solution():
    # printT()
    for k in K_list:
        k_t = k[0]-1
        k_rot = k[1]
        rotateT(k_t,k_rot)
        # print(k)
        # printT()

    return getScore()


def rotateT(k_t,k_rot):
    s = getStatus()

    que = []
    que.append([k_t,k_rot])
    while len(que) > 0:
        node = que.pop(0)
        node_t = node[0]
        node_rot = node[1]

        if node_rot == 1:
            t[node_t] = rotateRight(t[node_t])
        else:
            t[node_t] = rotateLeft(t[node_t])

        if node_t - 1 >= 0:
            if s[node_t - 1] == 0:
                s[node_t - 1] = -1
                que.append([node_t-1,node_rot*(-1)])
        if node_t < 3:
            if s[node_t] == 0:
                s[node_t] = -1
                que.append([node_t+1,node_rot*(-1)])


def rotateRight(t):
    return t[-1] + t[:7]


def rotateLeft(t):
    return t[1:] + t[0]


def getStatus():
    s = [0 for _ in range(3)]
    if t[0][2] == t[1][6]:
        s[0] = 1
    if t[1][2] == t[2][6]:
        s[1] = 1
    if t[2][2] == t[3][6]:
        s[2] = 1
    return s


def printT():
    print()
    for i in range(4):
        print(t[i])
    print()


def getScore():
    sum = 0
    for i in range(4):
        if t[i][0] == '1':
            sum += 2**i
    return sum


t = [read().strip() for _ in range(4)]
K = int(read().strip())
K_list = [list(map(int,read().strip().split())) for _ in range(K)]

print(solution())
# print('time',time.time_ns()-prev_time)

