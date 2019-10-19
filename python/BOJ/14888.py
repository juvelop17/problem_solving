import sys
import time

prev_time = time.time_ns()
# sys.stdin = open('input.txt', 'r')
read = sys.stdin.readline



def solution():
    que = []
    curr = 0
    curr_val = A[curr]
    curr_pl = pl
    curr_mi = mi
    curr_mul = mul
    curr_div = div

    max_val = -10**9
    min_val = 10**9
    res_print = [[],[]]
    que.append([curr, curr_val, [curr_pl, curr_mi, curr_mul, curr_div],[]])
    while len(que) > 0:
        node = que.pop(0)
        node_curr = node[0]
        node_val = node[1]
        node_pl = node[2][0]
        node_mi = node[2][1]
        node_mul = node[2][2]
        node_div = node[2][3]
        node_print = node[3]

        if node_curr == N-1:
            if max_val < node_val:
                max_val = node_val
                res_print[0] = node_print
            if min_val > node_val:
                min_val = node_val
                res_print[1] = node_print
            continue

        if node_pl > 0:
            que.append([node_curr + 1,
                        node_val + A[node_curr + 1],
                        [node_pl - 1, node_mi, node_mul, node_div],
                        node_print+[0]])
        if node_mi > 0:
            que.append([node_curr + 1,
                        node_val - A[node_curr + 1],
                        [node_pl, node_mi-1, node_mul, node_div],
                        node_print+[1]])
        if node_mul > 0:
            que.append([node_curr + 1,
                        node_val * A[node_curr + 1],
                        [node_pl, node_mi, node_mul-1, node_div],
                        node_print+[2]])
        if node_div > 0:
            if node_val >= 0:
                que.append([node_curr + 1,
                            node_val // A[node_curr + 1],
                            [node_pl, node_mi, node_mul, node_div-1],
                            node_print+[3]])
            else:
                que.append([node_curr + 1,
                            -node_val // A[node_curr + 1] *(-1),
                            [node_pl, node_mi, node_mul, node_div-1],
                            node_print+[3]])

    return max_val,min_val,res_print


N = int(read().strip())
A = list(map(int, read().strip().split()))
pl, mi, mul, div = map(int, read().strip().split())


res_max, res_min, res_print = solution()
print(res_max)
print(res_min)
# print(res_print)
# print('time', time.time_ns() - prev_time)

