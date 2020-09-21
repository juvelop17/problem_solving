import time

prev_time = time.time_ns()

def solutioin(info, query):
    db =





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



