#include <iostream>
#include <cstdio>
#include <iomanip>

using namespace std;


int T, N, A, B;
long long fac_arr[100] = {0};


long long factorial(int num){
    if (fac_arr[num] != 0){
        return fac_arr[num];
    }

    for (int i=2;i<=num;i++){
        if (fac_arr[num] != 0){
            continue;
        }
        fac_arr[i] = fac_arr[i-1] * i;
    }
    return fac_arr[num];
}


int solution(){
    if (A > B){
        return 0;
    } else if (A == B) {
        return 1;
    }

    if (N < 2){
        return 0; 
    } else if (N == 2){
        return 1;
    }
    
    int n1 = B-A+1; // 수 범위 개수
    int n2 = N-2; // 뽑을 개수
    cout << "n1 n2 : " << n1 << " " << n2 << endl;

    fac_arr[1] = 1;
    int left = n1+n2-1;
    int right_min = min(n2,n1-1);
    
    long long res = 1;
    for (int i=0;i<right_min;i++){
        res = res * (left-i) / (i+1);
    } 
    // 틀린 계산식 
    // 1 + 3 과 2 + 2를 구분함

    return res;
}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    freopen("input.txt","r",stdin);

    cin >> T;
    for (int i=1;i<=T;i++){
        cin >> N >> A >> B;
        cout << "#" << i << " " << solution() << endl;
    }
}






