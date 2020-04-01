#include <iostream>

using namespace std;


int N, M, x, y, K;
int mp[20][20];
int mem[20][20];
int comm[1000];

int cur_i,cur_j;

// 동 서 북 남
// 1 2 3 4
int di[5] = {0,0,0,-1,1};
int dj[5] = {0,1,-1,0,0};

int move(int comm){
    // if (comm == 1) {
        
    // } else if (comm == 2) {

    // } else if (comm == 3) {
        
    // } else if (comm == 4) {
        
    // }

    
}


int solution() {
    int cnt = 0;
    while (cnt < K){
        
        cnt++;
    }
    

    return 0;
}

int main() {
    freopen("input.txt","r",stdin);

    cin >> N >> M >> x >> y >> K;
    
    for (int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            cin >> mp[i][j];
        }
    }

    for (int i=0;i<K;i++) {
        cin >> comm[i];
    }

    solution();
    
    return 0;
}




