//
// Created by Junho Kim on 2021/08/19.
//

void makeSet(int v) {
    Parent[v] = v;
}

int findSet(int v) {
    if (v == Parent[v]) return v;
    return findSet(Parent[v]);
}

void unionSet(int u, int v) {
    Parent[findSet(u)] = findSet(v);
}




///////////////////////////

// 서로소 집합

#define MAX_N 100

int Parent[MAX_N];
for (int i=0;i<MAX_N;i++){
    Parent[i] = -1;
}

int findSet(int v) {
    if (Parent[v] < 0) return v;

    return findSet(Parent[v]);
}

int getSetSize(int v) {
    return -Parent[findSet(v)];
}

void unionSet(int u, int v) {
    int root1 = findSet(u);
    int root2 = findSet(v);
    if (root1 == root2) return;

    Parent[root1] += Parent[root2];
    Parent[root2] = root1;
}









