#include <iostream>
#include <cstdio>

using namespace std;


int T,K;
int MAX_VAL = 100000;
int min_a = MAX_VAL;
int min_b = MAX_VAL;

int map_arr[100000][100000] = {0};
// int prime_num[10000] = {0};



int GCD(int n, int a,int b){
    int res;
    if (map_arr[a][b] == -1) {
        return -1;
    } else if (map_arr[a][b] != 0) {
        return map_arr[a][b];
    }

    if (b == 0){
        return 0;
    }

    if (n == K){
        if (a%b == 0){
            return 0;
        } else {
            return -1;
        }
    }

    res = GCD(n+1,b,a%b);
    if (res == -1){
        return -1;
    }

    return res + 1;
}


int solution(){
    int res;
    min_a = MAX_VAL;
    min_b = MAX_VAL;

    for (int i=2;i<=min_a;i++){
        cout << i;
        for (int j=1;j<i;j++){
            res = GCD(1,i,j);
            cout << res;
            if (res != -1){
                min_a = i;
                min_b = j;
            }
        }
    }
    
    return 0;
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("input.txt","r",stdin);

    cin >> T;
    for (int i=1;i<=T;i++){
        cin >> K;
        cout << K;
        solution();
        cout << i << min_a << min_b;
    }

    return 0;
}


