#include <iostream>
#include <vector>
#include <string>

using namespace std;

int U,N;
vector<vector<string> > auc_vec;
vector<int> mon_vec;

int solution(){
    int min_cnt, min_mo;
    min_cnt = N+1;
    min_mo = U+1;
    for(int i=1;i<=U;i++){
        if (auc_vec[i].size() != 0 && auc_vec[i].size() < min_cnt) {
            min_mo = i;
            min_cnt = auc_vec[i].size();
        }
    }
    cout << auc_vec[min_mo][0] << " " << min_mo;

    return 0;
}

int main() {
    freopen("input.txt","r",stdin);

    cin >> U >> N;
    string na;
    int mo;
    auc_vec.resize(U+1);

    for(int i=0;i<=U;i++){
        vector<string> vec;
        auc_vec[i] = vec;
    }

    for(int i=0;i<N;i++){
        cin >> na >> mo;
        auc_vec[mo].push_back(na);
    }

    solution();

    return 0;
}

