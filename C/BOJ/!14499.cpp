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

int dice[6] = {4,3,2,1,5,6}; // 좌 우 위에서 아래로

bool checkRange(int i, int j){
    return i >= 0 && i < N && j >= 0 && j < M;
}

int move(int comm){
    int new_dice[6];
    
    int new_cur_i = cur_i + di[comm];
    int new_cur_j = cur_j + dj[comm];
    if (checkRange(new_cur_i, new_cur_j)) {
        cur_i = new_cur_i;
        cur_j = new_cur_j;
    }

    for (int i=0;i<6;i++){
        new_dice[i] = dice[i];
    }

    if (comm == 1) {
        new_dice[0] = dice[5];
        new_dice[3] = dice[0];
        new_dice[1] = dice[3];
        new_dice[5] = dice[1];
    } else if (comm == 2) {
        new_dice[0] = dice[3];
        new_dice[3] = dice[1];
        new_dice[1] = dice[5];
        new_dice[5] = dice[0];
    } else if (comm == 3) {
        new_dice[2] = dice[3];
        new_dice[3] = dice[4];
        new_dice[4] = dice[5];
        new_dice[5] = dice[2];
    } else if (comm == 4) {
        new_dice[2] = dice[5];
        new_dice[3] = dice[2];
        new_dice[4] = dice[3];
        new_dice[5] = dice[4];
    }
    
    for (int i=0;i<6;i++){
        dice[i] = new_dice[i];
    }

    if (mp[cur_i][cur_j] == 0) {
        mp[cur_i][cur_j] = dice[5];
    } else {
        mp[cur_i][cur_j] = dice[5];
        dice[5] = 0;
    }

    cout << dice[3] << endl;

    return 0;
}

int solution() {
    int cnt = 0;
    while (cnt < K){
        move(comm[cnt]);
        cnt++;
    }

    return 0;
}

int main() {
    freopen("input.txt","r",stdin);

    cin >> N >> M >> x >> y >> K;
    
    cur_i = x;
    cur_j = y;
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




