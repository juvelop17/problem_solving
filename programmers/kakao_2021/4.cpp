//
// Created by Junho Kim on 2021/09/05.
//


#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define INF 100000000
#define MAX_N 201

int cost[MAX_N][MAX_N];

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    for (int i = 0; i < MAX_N; ++i) {
        for (int j = 0; j < MAX_N; ++j) {
            cost[i][j] = INF;
        }
        cost[i][i] = 0;
    }

    for (auto fare : fares) {
        cost[fare[0]][fare[1]] = fare[2];
        cost[fare[1]][fare[0]] = fare[2];
    }

    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j]);
            }
        }
    }

    int minFare = INF;
    for (int i = 1; i <= n; ++i) {
        minFare = min(minFare, cost[s][i] + cost[i][a] + cost[i][b]);
    }

    return minFare;
}






#include <iostream>

using namespace std;

int main() {

    int n, s, a, b;
    vector<vector<int>> fares = {{4, 1, 10}, {3, 5, 24}, {5, 6, 2}, {3, 1, 41}, {5, 1, 24}, {4, 6, 50}, {2, 4, 66}, {2, 3, 22}, {1, 6, 25}};
    n = 6;
    s = 4;
    a = 6;
    b = 2;

    solution(n, s, a, b, fares);
    return 0;
}