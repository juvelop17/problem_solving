# 9:00 부터 n회 t분 간격으로 역에 도착, 최대 m명 탑승
# 그시간에 도착한 사람도 태움


class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute


def solution(n, t, m, timetable):
    answer = ''

    ppl_timetable = []
    for time in timetable:
        p_hour, p_minute = time.split(':')
        ppl_timetable.append(Time(int(p_hour), int(p_minute)))

    bus_timetable = []
    departure_time = Time(9, 0)
    for i in range(n):
        interval = i * t
        bus_time = Time(departure_time.hour + interval // 60, departure_time.minute + interval % 60)
        # print(bus_time.hour, bus_time.minute)
        bus_timetable.append(bus_time)

    time_sort(ppl_timetable)

    # print('bus_timetable')
    # print_time_list(bus_timetable)
    # print('ppl_timetable')
    # print_time_list(ppl_timetable)

    index_ppl = 0           # 승객 인덱스
    count_bus = 0           # 버스 카운트
    late_time = None        # 탑승가능한 마지막 시간
    last_person = False
    pass_list = []

    while count_bus < n:
        count_ppl = 0  # 탑승 승객 카운트
        while count_ppl < m and index_ppl < len(ppl_timetable):
            count_ppl += 1
            if (ppl_timetable[index_ppl].hour < bus_timetable[count_bus].hour or
                    (ppl_timetable[index_ppl].hour == bus_timetable[count_bus].hour and
                     ppl_timetable[index_ppl].minute <= bus_timetable[count_bus].minute)):
                pass_list.append(ppl_timetable[index_ppl])
                if count_ppl == m and count_bus == n - 1:
                    last_person = True
                index_ppl+=1

        count_bus += 1

    # print('count_pass')
    # print_time_list(pass_list)

    if last_person:
        if pass_list[-1].minute == 0:
            last_time = Time(pass_list[-1].hour-1, 59)
        else:
            last_time = Time(pass_list[-1].hour, pass_list[-1].minute - 1)
    else:
        last_time = bus_timetable[-1]

    return '{}:{}'.format(str(last_time.hour).zfill(2), str(last_time.minute).zfill(2))


def time_sort(time_list):
    for i in range(len(time_list)):
        min_index = len(time_list) - 1
        for j in range(i, len(time_list)):
            if ((time_list[j].hour < time_list[min_index].hour) or
                    (time_list[j].hour == time_list[min_index].hour and
                     time_list[j].minute < time_list[min_index].minute)):
                min_index = j
        swap(time_list, i, min_index)
        # waiting_queue.put(time_list[min_index])


def swap(time_list, i, j):
    time_list[i], time_list[j] = time_list[j], time_list[i]


def print_time(_time):
    print(_time.hour, _time.minute)

def print_time_list(_time_list):
    for i in range(len(_time_list)):
        print_time(_time_list[i])


# print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03", "08:03", "08:03", "02:03"]))

print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(solution(10, 60, 45,
               ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                "23:59", "23:59", "23:59", "23:59", "23:59"]))
