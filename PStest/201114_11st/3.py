# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    alpha_dict = {}
    for s in S:
        if s not in alpha_dict:
            alpha_dict[s] = 0
        alpha_dict[s] += 1

    cnt = 0
    for k, v in alpha_dict.items():

        while alpha_dict[k] != 0:
            sw = True
            for fk, fv in alpha_dict.items():
                if k == fk:
                    continue
                if v == fv:
                    sw = False
            if sw == False:
                cnt += 1
                alpha_dict[k] -= 1
                v -= 1
            else:
                break
    return cnt

# S = "aaaabbbb"
# S = "ccaaffddecee"
# S = "eeee"
S = "example"
# S = ""

print(solution(S))
