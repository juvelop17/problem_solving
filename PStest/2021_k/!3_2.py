import time

prev_time = time.time_ns()


from itertools import combinations


def insert(res,num_list,index,cur_str):
    if index == 4:
        res.append(cur_str)
        return

    next_str = str(num_list[index])
    insert(res,num_list, index+1, cur_str+next_str)
    next_str = '-'
    insert(res,num_list, index+1, cur_str+next_str)

def solution(info, query):
    answer = []

    # DB 입력
    new_dict = {}

    lang_list = ['cpp', 'java', 'python']
    job_list = ['backend', 'frontend']
    period_list = ['junior', 'senior']
    food_list = ['chicken', 'pizza']


    for i in range(len(info)):
        lang, job, period, food, score = info[i].strip().split()
        score = int(score)
        # print(lang, job, period, food, score)

        lang_num = lang_list.index(lang)
        job_num = job_list.index(job)
        period_num = period_list.index(period)
        food_num = food_list.index(food)
        num_list = [lang_num,job_num,period_num,food_num]
        res = []
        insert(res,num_list,0,'')
        # print(res)

        for r in res:
            if r not in new_dict:
                new_dict[r] = []
            new_dict[r].append(score)
        # print(new_dict)

    # DB 쿼리 처리
    for que in query:
        qlang, qjob, qperiod, qfood, qscore = que.replace('and','').split()
        qscore = int(qscore)
        # print(qlang, qjob, qperiod, qfood, qscore)

        query_str = ''
        if qlang == '-':
            query_str += '-'
        else:
            query_str += str(lang_list.index(qlang))

        if qjob == '-':
            query_str += '-'
        else:
            query_str += str(job_list.index(qjob))

        if qperiod == '-':
            query_str += '-'
        else:
            query_str += str(period_list.index(qperiod))

        if qfood == '-':
            query_str += '-'
        else:
            query_str += str(food_list.index(qfood))

        # print('query_str',query_str)

        cnt = 0
        if query_str in new_dict:
            for sco in new_dict[query_str]:
                if sco >= qscore:
                    cnt += 1
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



