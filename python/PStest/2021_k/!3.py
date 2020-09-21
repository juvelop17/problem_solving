import time

prev_time = time.time_ns()

def solution(info, query):
    answer = []

    # DB 입력
    id_dict = {}
    lang_dict = {}
    job_dict = {}
    period_dict = {}
    food_dict = {}

    lang_list = ['cpp', 'java', 'python']
    for l in lang_list:
        lang_dict[l] = []

    job_list = ['backend', 'frontend']
    for j in job_list:
        job_dict[j] = []

    period_list = ['junior', 'senior']
    for p in period_list:
        period_dict[p] = []

    food_list = ['chicken', 'pizza']
    for f in food_list:
        food_dict[f] = []

    for i in range(len(info)):
        lang, job, period, food, score = info[i].strip().split()
        score = int(score)
        # print(lang, job, period, food, score)
        id_dict[str(i)] = score

        lang_dict[lang].append(str(i))
        job_dict[job].append(str(i))
        period_dict[period].append(str(i))
        food_dict[food].append(str(i))

    # print(id_dict)
    # print(lang_dict)
    # print(job_dict)
    # print(period_dict)
    # print(food_dict)

    # DB 쿼리 처리
    for que in query:
        cnt = 0
        qlang, qjob, qperiod, qfood, qscore = que.replace('and','').split()
        qscore = int(qscore)
        # print(qlang, qjob, qperiod, qfood, qscore)

        pick_id = set(id_dict.keys())
        # print('pick_id', pick_id)

        if qlang != '-':
            if len(pick_id) > 0:
                pick_id = pick_id.intersection(set(lang_dict[qlang]))
            else:
                pick_id = set(lang_dict[qlang])
        # print(pick_id)

        if qjob != '-':
            if len(pick_id) > 0:
                pick_id = pick_id.intersection(set(job_dict[qjob]))
            else:
                pick_id = set(job_dict[qjob])
        # print(pick_id)

        if qperiod != '-':
            if len(pick_id) > 0:
                pick_id = pick_id.intersection(set(period_dict[qperiod]))
            else:
                pick_id = set(period_dict[qperiod])
        # print(pick_id)

        if qfood != '-':
            if len(pick_id) > 0:
                pick_id = pick_id.intersection(set(food_dict[qfood]))
            else:
                pick_id = set(food_dict[qfood])
        # print(pick_id)
        # print(id_dict)

        for id in pick_id:
            if id_dict[id] >= qscore:
                cnt += 1
        # print(cnt)
        answer.append(cnt)
    return answer



#  개발언어 직군 경력 소울푸드 점수
info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]

# '-' 표시는 해당 조건을 고려하지 않겠다는 의미입니다.
query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]

# #  개발언어 직군 경력 소울푸드 점수
# info = ["java backend junior pizza 150",
#         "java backend junior chicken 80",
#         "python backend senior chicken 50"]
#
# # '-' 표시는 해당 조건을 고려하지 않겠다는 의미입니다.
# query = ["java and backend and junior and pizza 100",
#          "python and frontend and senior and chicken 200",
#          "cpp and - and senior and pizza 250",
#          "- and backend and senior and - 150",
#          "- and - and - and chicken 100",
#          "python and - and - and - 50"]


print(solution(info, query))


print('time', time.time_ns()-prev_time)



