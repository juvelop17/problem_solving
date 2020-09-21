
import sys
import time

sys.stdin = open('input1.txt','r')
read = sys.stdin.readline
prev_time = time.time_ns()

def solution(s):
    result = 10000
    cur_index = 0
    for tok_len in list(range(1,int(len(s)/2)+1)) + [len(s)]:
        cur_index = 0
        word_tok = list(s[i:i+tok_len] for i in range(0,len(s),tok_len))

        # print(word_tok,word_tok[1:] + [''])
        new_word = []
        cnt = 1
        for a,b in zip(word_tok,word_tok[1:] + ['']):
            # print(a,b)
            if a == b:
                cnt += 1
            else:
                new_word.append((a,cnt))
                cnt = 1
        # print(new_word)

        num = sum(len(word) + len(str(word_cnt)) if word_cnt > 1 else len(word) for word, word_cnt in new_word)
        if num < result:
            result = num

    return result


for _ in range(5):
    s = read().strip()
    print(s)
    print(solution(s))

print('time', time.time_ns()-prev_time)