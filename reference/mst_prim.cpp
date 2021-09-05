//
// Created by Junho Kim on 2021/08/19.
//

#define MAX_N 100
#define INF 100000000

int N;
int Graph[MAX_N][MAX_N];
int Parent[MAX_N];
int Weight[MAX_N];

int prim() {
    for (int i = 0; i < N; i++) {
        Weight[i] = -1;
    }
    Weight[0] = 0;

    for (int k = 1; k < N; k++) {
        int minWeight = INF;
        int minVertex;
        int minParent;

        for (int i = 0; i < N; i++) {
            if (Weight[i] < 0) {
                continue;
            }
            for (int j = 0; j < N; j++) {
                if (Weight[j] >= 0) {
                    continue;
                }
                if (Graph[i][j] < minWeight) {
                    minVertex = j;
                    minParent = i;
                    minWeight = Graph[i][j];
                }
            }
        }
        Parent[minVertex] = minParent;
        Weight[minVertex] = minWeight;
    }

    int sumCost = 0;
    for (int i = 0; i < N; i++) {
        sumCost += Weight[i];
    }
    return sumCost;
}


//////////////////////////////////////////////

// priority_queue 활용

#include <queue>
#include <vector>

#define MAX_N 100
#define INF 100000000

int N;
int Graph[MAX_N][MAX_N];

int prim() {
    priority_queue < pair<int,int>, vector<pair<int,int> >, greater<pair<int,int> > > pq;

    bool visited[MAX_N] = {false};
    visited[0] = true;
    for (int next = 0; next < N; next++) {
        pq.push(make_pair(Graph[0][next], next));
    }

    int sumCost = 0;
    while (!pq.empty()) {
        int curr = pq.top().second;
        int weight = pq.top().first;
        pq.pop();

        if (visited[curr]) continue;
        visited[curr] = true;
        sumCost += weight;

        for (int next = 0; next < N; next++) {
            pq.push(make_pair(Graph[curr][next], next));
        }
    }

    return sumCost;
}






