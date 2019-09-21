import copy

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def getLongistPath(N, K, map_height):
    # find highest
    highest_node = []
    max_height = 0
    for _i in range(N):
        for _j in range(N):
            if map_height[_i][_j] > max_height:
                max_height = map_height[_i][_j]
                highest_node.clear()
                highest_node.append((_i, _j))
            elif map_height[_i][_j] == max_height:
                highest_node.append((_i, _j))

    # print('max_height', max_height)
    # print('highest_node', highest_node)

    max_path = []
    for node in highest_node:
        max_path.append(findPath(N, K, map_height, [], node, []))

    print('max_path', max_path)
    max_num = 0
    for path in max_path:
        if len(path) > max_num:
            max_num = len(path)
    return max_num


def findPath(N, K, map_height, max_path, node, path):
    new_path = copy.deepcopy(path)
    new_path.append(node)

    if len(new_path) > len(max_path):
        # print('before max_path', max_path)
        max_path.clear()
        for _node in new_path:
            max_path.append(_node)
        # print('new max_path', max_path)

    for _a in range(4):
        next_node = (node[0] + di[_a], node[1] + dj[_a])
        if next_node[0] >= 0 and next_node[0] < N and next_node[1] >= 0 and next_node[1] < N:
            if map_height[node[0]][node[1]] > map_height[next_node[0]][next_node[1]]:
                findPath(N, K, map_height, max_path, next_node, new_path)
            elif K > 0 :
                new_map_height = copy.deepcopy(map_height)
                for _b in range(K):
                    new_map_height[next_node[0]][next_node[1]] -= 1
                    if new_map_height[node[0]][node[1]] > new_map_height[next_node[0]][next_node[1]]:
                        findPath(N, 0, new_map_height, max_path, next_node, new_path)

    return max_path


f = open('1949_sample_input.txt', 'r')

T = int(f.readline().strip())

for tc in range(1):
    N, K = map(int, f.readline().strip().split(' '))
    map_height = [0 for _ in range(N)]
    for inp in range(N):
        map_height[inp] = list(map(int, f.readline().strip().split(' ')))
    answer = getLongistPath(N, K, map_height)
    print('#%d' %tc)
