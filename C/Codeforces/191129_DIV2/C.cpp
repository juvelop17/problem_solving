#include <iostream>
#include <set>

using namespace std;

int n, k, t; 

int solution() {
    set<int> res;

    res.insert(0);
    for (int i=1;i*i<=n;i++){
        int q = n / i;
        res.insert(n / i);
        res.insert(n / q);
    }

    cout << res.size() << endl;
    for (auto i = res.begin();i != res.end();i++) {
        cout << *i << " ";
    }
    cout << endl;
}

int main() {
    // freopen("input.txt","r",stdin);

    cin >> t;
    for (int tc=1;tc<=t;tc++) {
        cin >> n;
        solution();
    }
}
