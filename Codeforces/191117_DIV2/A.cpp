#include <iostream>
#include <cstdio>

using namespace std;


int t,n,a_arr[100001],b_arr[100001];

int solution(){
    bool isPush = true;
    int start = -1 , end = -1, add_num = -1;
    int cnt = 0;

    for(int i=1;i<=n;i++){
        if(a_arr[i] == b_arr[i]){
            if (start != -1){
                end = i;
            }
            continue;
        } else if(a_arr[i] > b_arr[i]){
            isPush = false;
            break;
        } else {
            if (end != -1 ) {
                isPush = false;
                break;
            } 
            if (add_num == -1) {
                add_num = b_arr[i] - a_arr[i];
            }
            if (start == -1) {
                start = i;
            }
            if (add_num != b_arr[i] - a_arr[i]){
                isPush = false;
                break;
            }
        }
    }

    if (isPush){
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;
}


int main(){
    // freopen("input.txt","r",stdin);

    cin >> t;
    for(int i=0;i<t;i++){
        cin >> n;
        for(int j=1;j<=n;j++){
            cin >> a_arr[j];
        }
        for(int j=1;j<=n;j++){
            cin >> b_arr[j];
        }
        solution();
    }
}


