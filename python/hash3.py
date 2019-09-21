def solution(clothes):
    answer = 1

    clothes_dict = dict()

    for cloth in clothes:
        if cloth[1] not in clothes_dict:
            clothes_dict[cloth[1]] = []
        clothes_dict[cloth[1]].append(cloth[0])

    # print(clothes_dict)

    for key in clothes_dict.keys():
        answer *= len(clothes_dict[key]) + 1

    answer -= 1

    return answer


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))






