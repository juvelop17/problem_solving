
def solution(cacheSize, cities):
    answer = -1
    time_value = 0

    cache_list = [-1 for _ in range(cacheSize)]
    cache_list_age = [0 for _ in range(cacheSize)]

    cache_index = 0
    for i in range(len(cities)):
        for j in range(cacheSize):
            cache_list_age[j] += 1

        # 존재 탐색 : hash 이용
        # 존재할 경우
        find_value = False
        for j in range(cacheSize):
            if(hash(cities[i].lower()) == cache_list[j]):
                time_value += 1
                cache_list_age[j] = 0
                find_value = True
                break

        # 존재하지 않을 경우
        if find_value == False:
            time_value += 5
            if cacheSize > 0:
                max = -1
                index = -1
                for j in range(cacheSize):
                    if cache_list_age[j] > max:
                        max = cache_list_age[j]
                        index = j

                cache_list[index] = hash(cities[i].lower())
                cache_list_age[index] = 0

        # if find_value : print('hit')
        # else: print('miss')
        # print(cache_list)
        # print(cache_list_age)
    # print('time_value',time_value)

    answer = time_value

    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))






