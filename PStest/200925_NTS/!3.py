




def solution(histogram):
    answer = 0


    left = 0
    right = 0
    max_square = 0

    while right < len(histogram):
        while histogram[right] <= histogram[left]:
            cal = min(histogram[left],histogram[right]) * (right - left - 1)
            if cal > max_square:
                max_square = cal
            print('left',left,'right',right,'max_square',max_square)
            right += 1
            if right == len(histogram):
                break

        left = right

    print('left',left,'right',right)



    return answer


# histogram = [2, 2, 2, 3]
histogram = [6, 5, 7, 3, 4, 2]

print(solution(histogram))








