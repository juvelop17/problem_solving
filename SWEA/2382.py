
class Node:
    def __init__(self, i, j, num, di):
        self.i = i
        self.j = j
        self.num = num
        self.di = di


# 상1 하2 좌3 우4

def getNodeNumAfter(N, M, K, node_list):
    # print('------------------------------------------------')
    # print(N,M,K)
    cnt = 0
    while cnt < M :
        cnt += 1
        node_map_list = [[[] for _ in range(N)] for _ in range(N)]

        for node in node_list:
            if node.di == 1:
                node.i, node.j = node.i-1, node.j
                node_map_list[node.i][node.j].append(node)
            elif node.di == 2:
                node.i, node.j = node.i+1, node.j
                node_map_list[node.i][node.j].append(node)
            elif node.di == 3:
                node.i, node.j = node.i, node.j-1
                node_map_list[node.i][node.j].append(node)
            elif node.di == 4:
                node.i, node.j = node.i, node.j+1
                node_map_list[node.i][node.j].append(node)

            if node.i == 0 or node.i == N-1 or node.j == 0 or node.j == N-1:
                node.num //= 2
                if node.di == 1:
                    node.di = 2
                elif node.di == 2:
                    node.di = 1
                elif node.di == 3:
                    node.di = 4
                elif node.di == 4:
                    node.di = 3

        for _i in range(N):
            for _j in range(N):
                if len(node_map_list[_i][_j]) > 1:
                    max_num = 0
                    di = 0
                    sum = 0
                    for node in node_map_list[_i][_j]:
                        sum += node.num
                        if node.num > max_num:
                            max_num = node.num
                            di = node.di
                        node_list.remove(node)
                    new_node = Node(_i,_j,sum,di)
                    node_list.append(new_node)
        # printMap(N, node_list)

    node_sum = 0
    for node in node_list:
        node_sum += node.num

    return node_sum


def printMap(N, node_list):
    print('printMap')
    node_map = [[0 for _ in range(N)] for _ in range(N)]

    for node in node_list:
        node_map[node.i][node.j] = node.di
        print(node.i,node.j,node.num,node.di)

    _str = ''
    for i in range(N):
        for j in range(N):
            _str += str(node_map[i][j]) + ' '
        _str += '\n'
    print(_str)
    print('')




f = open('2382_sample_input.txt', 'r')
T = int(f.readline().strip())

tc_result = []
for tc in range(T):
    N, M, K = map(int, f.readline().strip().split(' '))
    node_map = [[0 for _ in range(N)] for _ in range(N)]
    node_list = []
    for k in range(K):
        i, j, num, di = map(int, f.readline().strip().split(' '))
        new_node = Node(i,j,num,di)
        node_list.append(new_node)

    tc_result.append(getNodeNumAfter(N, M, K, node_list))

for _i in range(len(tc_result)):
    print('#' + str(_i+1) + ' ' + str(tc_result[_i]))
