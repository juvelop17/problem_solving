#include <iostream>
#include <cstdio>

using namespace std;


int t,a,b;
int prime_num[10000] = {0};


void getPrimeNum(){
    for (int i=2;i<1000;i++){
        for (int j=2;j<10000;j++){
            prime_num[i*j] = 1; // not prime number
        }
    }
}


int solution(){
    if (a == 1 || b == 1){
        return 1; // finite
    }

    if (a == b){
        return 0; // infinite
    }

    for (int i=2;i<=min(a,b);i++){
        if (a % i == 0 && b % i == 0){
            return 0; // infinite
        }
    }

    return 1; // finite
}



int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    // freopen("input.txt","r",stdin);

    // getPrimeNum();

    int res;
    cin >> t;
    // cout << t << endl;

    for (int i=0;i<t;i++){
        cin >> a >> b;
        res = solution();
        if (res == 0){
            cout << "Infinite" << endl;
        } else {
            cout << "Finite" << endl;
        }
    }
}




