//
// Created by Junho Kim on 2021/09/10.
//
#include <iostream>



#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> weak;
vector<int> dist;
int mincnt;
int n;

void swap(int &a, int &b) {
    int tmp = b;
    b = a;
    a = tmp;
}

void find(int depth) {
    if (depth == dist.size()) {
        int wi = 0;
        int di = 0;
        while (wi < weak.size() && di < dist.size()) {
            int s = weak[wi];
            int e = s + dist[di++];
            while (wi < weak.size()) {
                if (!(weak[wi] >= s && weak[wi] <= e)) {
                    break;
                }
                wi++;
            }
        }
        if (wi == weak.size()) {
            mincnt = min(mincnt, di);
        }
        return;
    }

    for (int i = depth; i < dist.size(); ++i) {
        swap(dist[depth], dist[i]);
        find(depth + 1);
        swap(dist[depth], dist[i]);
    }
}


int solution(int _n, vector<int> _weak, vector<int> _dist) {
    weak.assign(_weak.begin(), _weak.end());
    dist.assign(_dist.begin(), _dist.end());
    n = _n;
    mincnt = 1000;

    for (int j = 0; j < weak.size(); ++j) {
        for (int i = 0; i < dist.size(); ++i) {
            swap(dist[0], dist[i]);
            find(0);
            swap(dist[0], dist[i]);
        }
        weak.push_back(weak.front() + n);
        weak.erase(weak.begin());
    }

    if (mincnt == 1000) {
        return -1;
    }
    return mincnt;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n = 12;
    vector<int> weak = {1, 5, 6, 10};
    vector<int> dist = {1, 2, 3, 4};

//    int n = 12;
//    vector<int> weak = {1, 3, 4, 9, 10};
//    vector<int> dist = {3, 5, 7};

    cout << solution(n, weak, dist);

    return 0;
}