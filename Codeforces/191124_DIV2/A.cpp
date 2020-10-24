#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int t, n, a, b;
vector<int> lvec,rvec;

int solution() {
    int mn, mx;

    sort(lvec.begin(),lvec.end());
    sort(rvec.begin(),rvec.end());

    mn = rvec.front();
    mx = lvec.back();

    if (mx - mn < 0) {
        return 0;
    }

    return mx - mn;
}


int main() {
    freopen("input.txt","r",stdin);

    cin >> t;
    for (int tc=1;tc<=t;tc++){
        lvec.clear();
        rvec.clear();

        cin >> n;
        int l, r;
        for(int i=0;i<n;i++){
            cin >> l >> r;
            lvec.push_back(l);
            rvec.push_back(r);
        }

        cout << solution() << endl;
    }

}






