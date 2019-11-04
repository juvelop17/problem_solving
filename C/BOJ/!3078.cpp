#include <iostream>
#include <cstdio>
#include <queue>

using namespace std;


int N,K;
vector<int> vec[21];

int solution(){
    int sum = 0;
    int cnt = 0;

    int l_index,r_index;

    l_index = 0;
    r_index = 1;
    for(int i=2;i<=20;i++){
        if (vec[i].empty()){
            continue;
        }
        
        while (l_index<N){
            if (vec[i][r_index] - vec[i][l_index] > K){
                sum += cnt;
                l_index++;
                cnt--; 
            } else {
                r_index++;
                cnt++;
            }
        }
    }

    return sum;
}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    freopen("input.txt","r",stdin);

    cin >> N >> K;

    string str;
    for(int i=0;i<N;i++){
        cin >> str;
        vec[str.size()].push_back(i);
    }
    cout << solution() << endl;

    return 0;
}

