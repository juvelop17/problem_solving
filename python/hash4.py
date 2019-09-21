# class Music:
#     def __init__(self, id, g, p):
#         self.id = id
#         self.g = g
#         self.p = p


def solution(genres, plays):
    answer = []

    sum_dict = {}
    song_dict = {}

    for i in range(len(genres)):
        if genres[i] not in sum_dict or genres[i] not in song_dict:
            sum_dict[genres[i]] = 0
            song_dict[genres[i]] = []
        sum_dict[genres[i]] += plays[i]
        song_dict[genres[i]].append([i, plays[i]])

    genres_list = dict_sort(sum_dict)
    for genre_set in genres_list:
        sorted_song = list_sort(song_dict[genre_set[0]])
        if len(sorted_song) > 0:
            answer.append(sorted_song[0][0])
            if len(sorted_song) > 1:
                answer.append(sorted_song[1][0])

    return answer

def dict_sort(dict):
    _list = []
    for _key in dict:
        _list.append([_key,dict[_key]])

    for i in range(len(_list)):
        _max = _list[i][1]
        for j in range(i + 1, len(_list)):
            if _list[j][1] > _max:
                _max = _list[j][1]
                temp = _list[j]
                _list[j] = _list[i]
                _list[i] = temp
    return _list

def list_sort(li):
    for i in range(len(li)):
        _max = li[i][1]
        for j in range(i + 1, len(li)):
            if li[j][1] > _max:
                _max = li[j][1]
                temp = li[j]
                li[j] = li[i]
                li[i] = temp
    return li

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])