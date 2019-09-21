
import os
import sys



def search():
    word_dict = {}
    query_list = []

    n = int(f.readline().strip())
    for _ in range(n):
        word_dict[f.readline().strip()] = []

    q = int(f.readline().strip())
    for _ in range(q):
        query_list.append(f.readline().strip())

    for query in query_list:
        query_split = query.split(' ')

        if query_split[0] == '1':
            search_word = query_split[1]
            k = int(query_split[2])

            result1 = [] # 추천된
            result2 = [] # 처음

            words_keys = list(word_dict.keys())
            for word in words_keys:
                if search_word == word[:len(search_word)]:
                    # if search_word in word_dict[word]:
                    if len(word_dict[word]) != 0:
                        result1.append(word)
                    else:
                        result2.append(word)

            result1.sort()
            result2.sort()
            # print('result1',result1)
            # print('result2',result2)

            total_result = (result1 + result2)[:k]
            # print('total_result',total_result)

            for r in total_result:
                print(r.strip())
                if search_word not in word_dict[r]:
                    word_dict[r].append(search_word)

            # if len(total_result) == 0:
            #     print('')

        elif query_split[0] == '2':
            add_word = query_split[1]
            word_dict[add_word] = []



if __name__ == '__main__':

    file_path = os.getcwd() + '\\test_cases_1\\input002.txt'
    f = open(file_path, 'r')

    search()

    f.close()


