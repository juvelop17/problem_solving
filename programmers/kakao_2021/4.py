
INF = 100000000



def solution(n, s, a, b, fares):
    cost = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for fare in fares:
        cost[fare[0]][fare[1]] = fare[2]
        cost[fare[1]][fare[0]] = fare[2]

    for i in range(1,n+1):
        cost[i][i] = 0

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if cost[i][j] > cost[i][k] + cost[k][j]:
                    cost[i][j] = cost[i][k] + cost[k][j]

    minFare = INF
    for i in range(1,n+1):
        minFare = min(minFare, cost[s][i] + cost[i][a] + cost[i][b])

    return minFare


if __name__ == '__main__':
    n, s, a, b, fares = 6, 4, 6, 2, \
                        [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66],[2, 3, 22], [1, 6, 25]]

    print(solution(n, s, a, b, fares))
