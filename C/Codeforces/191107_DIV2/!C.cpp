#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

long long n;
int mem[1000000] = {0};

long long solution(){
    long long max_num = 0;
    long long tmp;
    long long cnt = 1;
    for(long long i=2;i*i<=n;i++){
        if (n % i == 0 && mem[i] == 0){
            cnt++;
            for (long long j=1;j<=n/i;j++){
                mem[i*j] = cnt;
            }
        }        
    }

    if (cnt == 0){
        cnt = n;
    }
    
    return cnt;
}


int main(){
    freopen("input.txt","r",stdin);

    cin >> n;
    cout << solution();

    return 0;
}


