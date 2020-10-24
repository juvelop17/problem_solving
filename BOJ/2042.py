
import time

ptime = time.time_ns()





import sys
sys.stdin = open('input.txt','r')
read = sys.stdin.readline

# 참조할 숫자 배열 인덱스(0부터 시작) : start_num, end_num
def construct(node_num, start_num, end_num):
    if start_num == end_num:
        tree_list[node_num] = num_list[start_num]
        return tree_list[node_num]
    mid_num = int((start_num + end_num)/2)
    tree_list[node_num] = construct(node_num*2,start_num,mid_num) + construct(node_num*2+1,mid_num+1,end_num)
    return tree_list[node_num]

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


def solution(num_list, commands):
    construct(1,0,len(num_list)-1)
    # print('tree_list',tree_list[:20])

    # print(num_list)
    # print('[0:2]',sum(0,2,1,0,len(num_list)-1))
    # print('[1:2]',sum(1,2,1,0,len(num_list)-1))
    # print('[1:3]',sum(1,3,1,0,len(num_list)-1))
    # print('[1:3]',sum(1,3,1,1,len(num_list)))

    # update(1,1,len(num_list),3,5)
    # print('tree_list',tree_list[:20])

    for command in commands:
        if command[0] == 1: # 값 변경
            update(1,1,len(num_list),command[1],command[2])
            # print('tree_list', tree_list[:20])
        elif command[0] == 2: # 합 출력
            print(sum(command[1],command[2],1,1,len(num_list)))


N, M, K = map(int, read().split())
num_list = []
for _ in range(N):
    num_list.append(int(read()))
commands = []
for _ in range(M+K):
    commands.append(list(map(int,read().split())))

tree_list = [0 for _ in range(10**7)]

solution(num_list,commands)




print('time',time.time_ns()-ptime)


