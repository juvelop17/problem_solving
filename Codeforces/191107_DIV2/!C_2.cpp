#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

long long n;
int num_arr[1000000];
int mem_arr[1000000]={0};

long long solution(){
    long long res;
    long long cnt = 0;
    for(long long i=2;i*i<=n;i++){
        if (n % i == 0 && mem_arr[i] == 0){
            for (int j=1;j<=n/i;j++){
                mem_arr[i*j] = 1;
            }
            num_arr[cnt] = i;
            cnt++;

            int k = n/i;
            if (i!=k){
                for (int j=1;j<=n/k;j++){
                    mem_arr[k*j] = 1;
                }
                num_arr[cnt] = k;
                cnt++;
            }
        }        
    }

    bool isTrue = false; // 최대공약수 1
    for(int i=0;i<cnt;i++){
        for (int j=i+1;j<cnt;j++){
            if (num_arr[j] % num_arr[i] == 0){
                mem_arr[j] = 0;
            }

            if(num_arr[j] % num_arr[i] != 0 && mem_arr[j] == 0) {
                isTrue = true;
                break;
            }
        }
    }

    if (cnt == 0){
        return n;
    }
    
    if (isTrue){
        res = 1;
    } else {
        res = num_arr[0];
    }
    
    return res;
}


int main(){
    // freopen("input.txt","r",stdin);

    cin >> n;
    cout << solution();

    return 0;
}


