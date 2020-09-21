import time

prev_time = time.time_ns()


def getTime(time_str):
    time_str_list = time_str.split(":")
    seconds = 0
    seconds += int(time_str_list[0]) * 3600 + int(time_str_list[1]) * 60 + int(time_str_list[2])
    return seconds

def getLogTime(log):
    start_str, end_str = log.split('-')
    start_time = getTime(start_str)
    end_time = getTime(end_str)
    return start_time, end_time

def solution(play_time, adv_time, logs):
    answer = ''

    play_seconds = getTime(play_time)
    adv_seconds = getTime(adv_time)
    print(play_seconds)
    print(adv_seconds)

    log_time_list = []
    for log in logs:
        start_time, end_time = getLogTime(log)
        log_time_list.append([start_time, 0])
        log_time_list.append([end_time, 1])
    log_time_list.sort()
    print(log_time_list)

    adv_start_time = 0
    max_cnt = 0

    cur_start_time = log_time_list[0]
    cur_end_time = cur_start_time + adv_seconds
    cur_cnt = 0

    node_que = []
    for log_time in log_time_list: # log_time : [시간, start or end]
        print(log_time)
        node_que.append(log_time)
        if log_time[1] == 0: # 정시간에 카운트 할지 말지 debug 필요
            if
            cur_cnt += 1

    return answer


play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

# play_time = "99:59:59"
# adv_time = "25:00:00"
# logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
#
# play_time = "50:00:00"
# adv_time = "50:00:00"
# logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]

print(solution(play_time,adv_time,logs))

print('time', time.time_ns()-prev_time)
