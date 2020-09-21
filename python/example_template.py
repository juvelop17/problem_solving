import sys
import time

# text file input
sys.stdin = open('example_template.txt', 'r')  # console input
# sys.stdout = open('output.txt', 'w')  # console output

read = sys.stdin.readline # input 보다 빠름

# strip(), split() 이용하여 parsing
N, M, H = map(int, read().strip().split())

# for문으로 list parsing
M_list = [list(map(int, read().strip().split())) for _ in range(M)]

print(N, M, H)
print(M_list)

# 시간 측정
prev_time = time.time_ns()
print('time',time.time_ns()-prev_time)

