#include <iostream>

using namespace std;

int R, C, K;
char mp[5][5];
bool visited[5][5];
int start[2], goal[2];
int cnt;
int di[4] = {0,0,-1,1};
int dj[4] = {-1,1,0,0};


void printMap() {
    cout << endl;
    for (int i=0;i<R;i++){
        for (int j=0;j<C;j++){
            cout << visited[i][j];
        }
        cout << endl;
    }
}

bool checkRange(int i, int j){
    return i >= 0 && i < R && j >= 0 && j < C;
}

int move(int cur_i, int cur_j, int len){
    // printMap();
    if (len > K || mp[cur_i][cur_j] == 'T') {
        return 0;
    }

    if (cur_i == goal[0] && cur_j == goal[1] && len == K){
        cnt++;
        return 0;
    }

    int next_i,next_j;
    for(int x=0;x<4;x++){
        next_i = cur_i+di[x];
        next_j = cur_j+dj[x];

        if (!checkRange(next_i,next_j) || 
            visited[next_i][next_j]){
            continue;
        }

        visited[next_i][next_j] = true;
        move(next_i,next_j,len+1);
        visited[next_i][next_j] = false;
    }
    
    return 0;
}

int solution(){
    int cur[2];

    start[0] = R-1;
    start[1] = 0;
    goal[0] = 0;
    goal[1] = C-1;

    visited[start[0]][start[1]] = true;
    move(start[0],start[1],1);

    return 0;
}

int main(){
    freopen("input.txt","r",stdin);

    cin >> R >> C >> K;

    for(int i=0;i<R;i++) {
        for(int j=0;j<C;j++){
            cin >> mp[i][j];
            visited[i][j] = false;
        }
    }

    cnt = 0;
    solution();
    cout << cnt;
    return 0;
}
