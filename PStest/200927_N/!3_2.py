




def getExpect(con,exp,index):
    exp[index] = 1
    if len(con[index]) == 0:
        return 1

    for child in con[index]:
        exp[index] += getExpect(con,exp,child)

    return exp[index]

# def find(n,inf,protec,exp):
#     max_val = -1
#     max_node = -1
#     for i in range(n):
#         if inf[i] or protec[i]:
#             continue
#         if max_val < exp[i]:
#             max_val = exp[i]
#             max_node = i
#
#     return max_node

def find(con,inf,protec,exp,index):
    if len(con[index]) == 0:
        return exp[index], index

    max_val = -1
    max_node = -1

    for child in con[index]:
        if not inf[child] and not protec[child]:
            if exp[child] > max_val:
                max_val = exp[child]
                max_node = child

        if inf[child]:
            new_val, new_node = find(con,inf,protec,exp,child)
            if inf[index] == False and new_val > max_val:
                max_val = new_val
                max_node = new_node

    return max_val, max_node

def infect(n,con,inf,protec):
    new_inf = inf[:]
    for i in range(n):
        if inf[i]:
            for child in con[i]:
                if not protec[child]:
                    new_inf[child] = True
    inf[:] = new_inf[:]

    return





def solution(n, edges):
    answer = 0

    con = [[] for _ in range(50)]
    for edge in edges:
        con[edge[0]].append(edge[1])
    print('con',con)

    exp = [-1 for _ in range(50)]
    inf = [False for _ in range(50)]
    protec = [False for _ in range(50)]

    inf[0] = True

    getExpect(con,exp,0)
    print('exp',exp)

    ischanged = True
    while ischanged:
        max_val, max_node = find(con,inf,protec,exp,0)
        print('max_node',max_node)
        if max_node == -1:
            ischanged = False
        protec[max_node] = True

        infect(n,con,inf,protec)


        print('protec : ', end='')
        for i in range(n):
            print(i,protec[i],end='  ')
        print()
        print('inf : ', end='')
        for i in range(n):
            print(i,inf[i],end='  ')
        print()


    for i in range(n):
        if inf[i]:
            answer += 1



    return answer



n = 19
edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6,14], [6, 15], [6, 16], [8, 17], [8, 18]]

# n = 14
# edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [2, 7], [3, 8], [3, 9], [3, 10], [4, 11], [4, 12], [4, 13]]
#
# n = 10
# edges = [[0, 1], [0, 2], [1, 3], [2, 4], [2, 5], [2, 6], [3, 7], [3, 8], [3, 9]]


print(solution(n,edges))


