#include <iostream>
#include <cstdio>

using namespace std;

int N, K, W[101], V[101];
int mem_w[100001] = {0};

void printArray(){
    int num;
    for (int j=0;j<=K;j++){
        cout << j << " : " << mem_w[j] << endl;
    }
    cout << endl;
}


int solution(){
    int max_num = 0;
    for(int i=1;i<=N;i++){
        for (int j=K;j>=0;j--){
            if(j-W[i]>=0){
                mem_w[j] = max(mem_w[j], mem_w[j-W[i]] + V[i]);
            }
            if (mem_w[j] > max_num){
                max_num = mem_w[j];
            }
            cout << j << " : " << mem_w[j] << endl;
        }
    }

    // printArray();

    return max_num;
}


int main(){
    freopen("input.txt","r",stdin);

    cin >> N >> K;
    for(int i=1;i<=N;i++){
        cin >> W[i] >> V[i];
    }
    cout << solution();

    return 0;
}




