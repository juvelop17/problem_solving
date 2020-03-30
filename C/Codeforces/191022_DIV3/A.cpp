#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> vec;
int q, n, a;


int solution() {
    int num = 1;
    sort(vec.begin(),vec.end());
    for(int i=1;i<vec.size();i++){
        if (vec[i] - vec[i-1] == 1) {
            num = 2;
            break;
        }
    }

    return num;
}


int main() {
    freopen("input.txt","r",stdin);

    cin >> q;
    for(int tc=0;tc<q;tc++){
        cin >> n;
        for(int num=0;num<n;num++){
            cin >> a;
            vec.push_back(a);
        }
        cout << solution() << endl;
        vec.clear();
    }

    return 0;
}



