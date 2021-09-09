//
// Created by Junho Kim on 2021/09/09.
//


#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

int n;
int rg[100000];
int rs[100000];

struct Truck {
    int i;
    int w;
    int t;

    Truck(int _i, int _w, int _t) : i(_i), w(_w), t(_t){}

    bool operator<(const Truck &b) const {
        return t > b.t;
    }
};

long long solution(int a, int b, vector<int> g, vector<int> s, vector<int> w, vector<int> t) {
    long long answer = -1;
    n = g.size();

    priority_queue<Truck> timestamp;
    priority_queue<Truck> backup;
    for (int i = 0; i < n; ++i) {
        Truck truck = {i, w[i], t[i]};
        timestamp.push(truck);
        backup.push(truck);
        rg[i] = g[i];
        rs[i] = s[i];
    }

    while (!timestamp.empty()) {
        Truck cur = timestamp.top();
        timestamp.pop();
        printf("%d %d %d\n", cur.t, a, b);

        int diffg = 0;
        int diffs = 0;
        diffg = cur.w;
        g[cur.i] -= cur.w;
        if (g[cur.i] < 0) {
            diffg += g[cur.i];
            g[cur.i] = 0;
        }
        diffs = cur.w - diffg;
        s[cur.i] -= diffs;
        if (s[cur.i] < 0) {
            diffs += s[cur.i];
            s[cur.i] = 0;
        }
        a -= diffg;
        b -= diffs;

        if (a < 0) {
            while (!backup.empty()) {
                Truck tr = backup.top();
                backup.pop();

                if (s[tr.i] > 0) {
                    int num = min(s[tr.i], tr.w);
                    if (num + a >= 0) {
                        num = -a;
                    }
                    if (rg[tr.i] <= g[tr.i] + num) {
                        num = rg[tr.i] - g[tr.i];
                    }
                    g[tr.i] += num;
                    s[tr.i] -= num;
                    a += num;
                    b -= num;
                }
            }
        }

        if (a <= 0 && b <= 0) {
            return cur.t;
        }

        if (g[cur.i] || s[cur.i]) {
            timestamp.push({cur.i, cur.w, cur.t + 2 * t[cur.i]});
            backup.push({cur.i, cur.w, cur.t + 2 * t[cur.i]});
        }
    }

    return answer;
}


int main() {
//    int a = 10;
//    int b = 10;
//    vector<int> g = {100};
//    vector<int> s = {100};
//    vector<int> w = {7};
//    vector<int> t = {10};

//    int a = 90;
//    int b = 500;
//    vector<int> g = {70,70,0};
//    vector<int> s = {0,0,500};
//    vector<int> w = {100,100,2};
//    vector<int> t = {4,8,1};

    int a = 90;
    int b = 500;
    vector<int> g = {100,0,0};
    vector<int> s = {10,0,500};
    vector<int> w = {100,100,2};
    vector<int> t = {4,8,1};


    cout << solution(a, b, g, s, w, t);

    return 0;
}