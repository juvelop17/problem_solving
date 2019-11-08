#include <iostream>
#include <cstdio>

using namespace std;

#define MAX_VAL 1000000


int T,K;
long long min_a, min_b;
long long gcd_arr[100] = {0};


void GCD(long long *n1, long long *n2){
    long long a, b, temp;

    if (gcd_arr[K] != 0){
        *n1 = gcd_arr[K];
        *n2 = gcd_arr[K-1];
    }

    gcd_arr[0] = 1;

    a = 2;
    b = 1;
    for (int i = 1;i<=K;i++){
        gcd_arr[i] = a;
        temp = a;
        a = a + b;
        b = temp;
    }

    *n1 = gcd_arr[K];
    *n2 = gcd_arr[K-1];
}


int solution(){
    min_a = MAX_VAL;
    min_b = MAX_VAL;

    GCD(&min_a,&min_b);
    
    return 1;
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    // freopen("input.txt","r",stdin);

    int res;

    cin >> T;
    for (int i=1;i<=T;i++){
        cin >> K;
        res = solution();
        cout << "#" << i << " " << min_a << " " << min_b << endl;
    }

    return 0;
}


