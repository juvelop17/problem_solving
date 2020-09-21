import sys
import time

sys.stdin = open('input1.txt','r')
read = sys.stdin.readline
prev_time = time.time_ns()

def solution(s):
    answer = 10000

    if len(s) == 1:
        return 1

    for i in range(1,int(len(s)/2)+1):
        new_str = ''
        cur_index = 0
        cur_str = s[cur_index:cur_index+i]
        next_index = cur_index + i
        cnt = 1

        while next_index <= len(s):
            next_str = s[next_index:next_index+i]
            if cur_str == next_str:
                cnt += 1
            else:
                if cnt > 1:
                    new_str += str(cnt) + cur_str
                else:
                    new_str += cur_str
                cur_str = next_str
                cnt = 1

            cur_index = next_index
            next_index = cur_index + i
            # print(cur_index,' new_str',new_str)

        if cnt > 2:
            new_str += str(cnt) + cur_str + s[next_index:]
        else:
            new_str += s[cur_index:]

        if len(new_str) < answer:
            answer = len(new_str)

        # print('i', i, ' new_str',new_str)

    return answer

for _ in range(5):
    s = read().strip()
    print(s)
    print(solution(s))

print('time', time.time_ns()-prev_time)