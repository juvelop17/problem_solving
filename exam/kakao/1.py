



def solution(id_list, report, k):
    answer = []

    ban = {}
    mail = {}
    for id in id_list:
        ban[id] = set()
        mail[id] = 0

    for repo in report:
        user_id, ban_id = repo.split()
        ban[ban_id].add(user_id)

    for ban_id, user_set in ban.items():
        if (len(user_set) >= k):
            for user_id in user_set:
                mail[user_id] += 1

    # print(ban)
    # print(mail)

    for id in id_list:
        answer.append(mail[id])

    return answer


if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2

    print(solution(id_list, report, k))



