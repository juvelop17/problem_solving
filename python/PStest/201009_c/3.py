
def solution(k, score):
    answer = -1
    next_score = score[1:]

    diff_dict = {}
    set_dict = {}
    for i in range(len(score)-1):
        diff = score[i]-next_score[i]
        if diff not in diff_dict:
            diff_dict[diff] = 1
            set_dict[diff] = set()
            set_dict[diff].add(i)
            set_dict[diff].add(i+1)
        else:
            diff_dict[diff] += 1
            set_dict[diff].add(i)
            set_dict[diff].add(i+1)
    print(diff_dict)
    print(set_dict)

    total_set = set()
    for diff, cnt in diff_dict.items():
        if k <= cnt:
            total_set = total_set | set_dict[diff]

    print(total_set)
    print(len(score)-len(total_set))

    return answer



# k = 3
# score =[24,22,20,10,5,3,2,1]

k = 2
score = [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]



print(solution(k, score))

