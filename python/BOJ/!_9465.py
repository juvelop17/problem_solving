import sys


sys.stdin = open('input.txt','r')


def solution(n,score_board):
    print(score_board)


T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    l1 = list(map(int,sys.stdin.readline().strip().split()))
    l2 = list(map(int,sys.stdin.readline().strip().split()))
    solution(n,[l1]+[l2])




