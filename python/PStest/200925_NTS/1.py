

def solution(flowers):
    answer = 0

    cnt = 0
    time_list = []
    for flower in flowers:
        time_list.append([flower[0],1]) # 피는
        time_list.append([flower[1],0]) # 지는
    time_list.sort()
    # print(time_list)

    start_time = -1
    end_time = -1
    period = 0
    for time in time_list:
        if time[1]:
            if cnt == 0:
                start_time = time[0]
            cnt += 1
        else:
            cnt -= 1
            if cnt == 0:
                end_time = time[0]
                period += end_time - start_time
                # print("start_time, end_time, period : ",start_time, end_time, period)

    answer = period

    return answer




# flowers = [[2, 5], [3, 7], [10, 11]]
flowers =[[3, 4],[4, 5], [6, 7], [8, 10]]

print(solution(flowers))


