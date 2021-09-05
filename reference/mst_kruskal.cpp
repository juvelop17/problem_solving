//
// Created by Junho Kim on 2021/08/19.
//

#define MAX_N 100

struct Edge {
    int u;
    int v;
    int cost;
};

Edge edgeArr[MAX_N * (MAX_N - 1) / 2];
int edgeCnt;
int Parent[MAX_N];
int kruskal() {
    quickSort(edgeArr, 0, edgeCnt - 1);

    for (int i = 0; i < N; i++) {
        Parent[i] = i;
    }

    int sumCost = 0;
    int selectCnt = 0;
    for (int i = 0; i < EdgeCnt; i++) {
        int u = edgeArr[i].u;
        int v = edgeArr[i].v;
        if (findSet(u) == findSet(v)) continue; // Cycle

        Parent[findSet(u)] = findSet(v); // Union

        sumCost += EdgeArr[i].cost;
        if (++selectCnt >= N - 1) break;
    }

    return sumCost;
}



