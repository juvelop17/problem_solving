#include <iostream>
#include <cstdio>
#include <map>
#include <vector>

using namespace std;


int n;
int num_arr[100001];
int e_arr[1000001],l_arr[1000001];
map<int,int> m;
vector<int> vec;

int solution(){
    int start,end;

    for(int i=1;i<=n;i++){
        vec.clear();
        m.clear();
        start = -1;
        end = -1;
        for(int j=i;j<=n;j++){
            if (num_arr[j]>0){
                vec.push_back(num_arr[j]);
                if (m[num_arr[j]] == 0){
                    m[num_arr[j]] = 1;
                } else if (m[num_arr[j]] == 1){
                    i=j;
                    break;
                } else if (m[num_arr[j]] == 2){
                    i=j;
                    break;
                } 
            } else {
                if (m[-num_arr[j]] == 0){
                    i=j+1;
                    break;
                } else if (m[-num_arr[j]] == 1){
                    m[-num_arr[j]] = 2;
                } else if (m[-num_arr[j]] == 2){
                    i=j+1;
                    break;
                } 
            }
        }

        if(vec.size() > 0){
            bool isValid = true;
            for(int j=0;j<vec.size();j++){
                if(m[vec[j]] != 2){
                    isValid = false;
                }
            }
            
            if(isValid) {
                cout << 
            }
        }
    }

    return 0;
}


int main(){
    freopen("input.txt","r",stdin);

    cin >> n;
    for(int i=1;i<=n;i++){
        cin >> num_arr[i];
    }
    solution();
}


