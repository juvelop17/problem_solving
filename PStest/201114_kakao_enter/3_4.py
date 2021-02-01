


import math

MAX_SIZE = 10** 6
tree_list = [0] * (pow(2, math.ceil(math.log(MAX_SIZE, 2)) + 1))


def construct(node, start, end, space):
    if start == end:
        tree_list[node] = space[start]
        return tree_list[node]
    mid = int((start + end) / 2)
    tree_list[node] = min(construct(node * 2, start, mid, space), construct(node * 2 + 1, mid + 1, end, space))
    return tree_list[node]


def query(space, tree_list, node, start, end, i, j):
    if i > end or j < start:
        return -1
    if i <= start and end <= j:
        return tree_list[node]

    mid = int((start + end) / 2)
    lnum = query(space, tree_list, 2 * node, start, mid, i, j)
    rnum = query(space, tree_list, 2 * node + 1, mid + 1, end, i, j)
    if lnum == -1:
        return rnum
    elif rnum == -1:
        return lnum
    else:
        return min(lnum, rnum)


def segment(x, space):
    # print('x, space',x, space)
    construct(1, 0, len(space) - 1, space)
    # print(tree_list[:30])

    max_val = -1
    cur_min = min(space[:x])
    for i in range(1, len(space)):
        if cur_min >
        cur_min = space
        if cur_min > max_val :
            max_val = cur_min
        # print('i, val, min_val',i, val, max_val)

    return max_val


# Write your code here


test_cases = [
    [2, [8, 2, 4, 6], 4],
    [1, [1,2,3,1,2], 3],
    [2, [3,1,1,1], 1],
    [3, [2,5,4,6,8], 4],
    [35, [1] * 1000000, -1],
    [805, [1] * 1000000, -1],
    [561950, [1] * 1000000, -1]
]

for tc in test_cases:
    x, space, ans = tc
    res = segment(x, space)
    print(ans, res, ans == res)


# x, len(space)
# (35, 1000000)
# (805, 1000000)
# (561950, 1000000)




