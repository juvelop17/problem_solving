//
// Created by Junho Kim on 2021/09/10.
//
typedef long long int ll;
#include <iostream>

using namespace std;

int n, m;
int tree[1000000];

int solution() {
    ll l = 0, r = 2000000000;
    ll maxh = -1;
    while (l <= r) {
        ll h = (l + r) / 2;
        ll total = 0;
        for (int i = 0; i < n; ++i) {
            if (tree[i] - h > 0) {
                total += tree[i] - h;
            }
        }
        if (total >= m) {
            maxh = h;
            l = h + 1;
        } else {
            r = h - 1;
        }
    }
    return maxh;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
//    freopen("input.txt", "r", stdin);

    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
        cin >> tree[i];
    }

    cout << solution();
    return 0;
}