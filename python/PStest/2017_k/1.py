def find_way(n, arr1, arr2):
    secret_map_value = [0 for _ in range(n)]
    for i in range(n):
        secret_map_value[i] = arr1[i] | arr2[i]

    secret_map = ['' for _ in range(n)]
    for i in range(n):
        val = secret_map_value[i]
        for j in range(n):
            print(val)

            if val % 2 == 0:
                secret_map[i] = ' ' + secret_map[i]
            else:
                secret_map[i] = '#' + secret_map[i]
            val = int(val / 2)

    # print(secret_map)

    answer = secret_map
    return answer


find_way(5,	[9, 20, 28, 18, 11],[30, 1, 21, 17, 28])