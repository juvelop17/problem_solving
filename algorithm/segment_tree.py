
# 참조할 숫자 배열 인덱스(0부터 시작) : start_num, end_num
def construct(node, start, end):
    if start == end:
        tree_list[node] = num_list[start]
        return tree_list[node]
    mid = int((start + end)/2)
    tree_list[node] = construct(node*2,start,mid) + construct(node*2+1,mid+1,end)
    return tree_list[node]

# 구할 범위 : l,r
# 트리 시작 인덱스 번호 : node
# 숫자 범위 : node_l, node_r
def sum(l, r, node, node_l, node_r):
    if r < node_l or l > node_r :
        return 0
    if l <= node_l and r >= node_r:
        return tree_list[node]
    mid = int((node_l+node_r)/2)
    return sum(l, r, node*2, node_l, mid) + sum(l, r, node*2+1, mid+1, node_r)

# 트리 시작 인덱스 번호 : node
# 숫자 범위 : node_l, node_r
# 변경할 인덱스와 값 : index, value
def update(node, node_l, node_r, index, value):
    if index < node_l or index > node_r:
        return tree_list[node]
    if node_l == node_r == index:
        tree_list[node] = value
        return tree_list[node]
    mid = int((node_l+node_r)/2)
    tree_list[node] = update(node*2,node_l,mid,index,value) + update(node*2+1,mid+1,node_r,index,value)
    return tree_list[node]


def solution():
    construct(1,0,len(num_list)-1)
    # print('tree_list',tree_list[:20])
    # print(num_list)
    # print('[0:2]',sum(0,2,1,0,len(num_list)-1))
    # print('[1:2]',sum(1,2,1,0,len(num_list)-1))
    # print('[1:3]',sum(1,3,1,0,len(num_list)-1))
    # print('[1:3]',sum(1,3,1,1,len(num_list)))

    print('3번째 항목 6으로 변경(0부터 시작)')
    update(1,0,len(num_list)-1,3,6)
    # print('tree_list',tree_list[:20])
    print('3번째 항목 6으로 변경(1부터 시작)')
    update(1,1,len(num_list),3,6)
    # print('tree_list',tree_list[:20])

N = 10**6
num_list = [i for i in range(N)]
tree_list = [0 for _ in range(10**7)]

solution()




