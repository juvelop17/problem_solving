#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int N, K, L;
int mp[100][100];

int dir; // u,r,d,l
int head[2], tail[2];
int len, cnt;

int di[4] = {-1,0,1,0};
int dj[4] = {0,1,0,-1};


queue<vector<int> > time_comm;
queue<int> tail_comm;


void displayMap() {
    cout << cnt << " " << dir << endl;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cout << mp[i][j];
        }
        cout << endl;
    }
    cout << endl;
}

bool checkRange(int i, int j) {
    return i >= 0 && i < N && j >= 0 && j < N;
}

int move() {
    int tail_dir;
    head[0] += di[dir]; head[1] += dj[dir];
    if (!checkRange(head[0],head[1])) {
        return -1;
    }
    
    tail_comm.push(dir);
    if (mp[head[0]][head[1]] == 2) {
        mp[head[0]][head[1]] = 1;
    } else if (mp[head[0]][head[1]] == 0){
        mp[head[0]][head[1]] = 1;
        if (!tail_comm.empty()) {
            mp[tail[0]][tail[1]] = 0;
            tail_dir = tail_comm.front();
            tail_comm.pop();
            tail[0] += di[tail_dir]; tail[1] += dj[tail_dir];
        }
    } else if (mp[head[0]][head[1]] == 1){
        return -1;
    }

    return 0;
}

int solution(){
    int res;

    mp[head[0]][head[1]] = 1;

    dir = 1;
    len = 1;
    cnt = 0;
    for(int i=0;i<2;i++){
        head[i]=tail[i]=0;
    }

    while(1) {
        if(!time_comm.empty() && time_comm.front()[0] == cnt){
            dir += time_comm.front()[1];
            time_comm.pop();

            if (dir < 0) {
                dir = 3;
            } else if (dir > 3) {
                dir = 0;
            }
        }
        displayMap();

        cnt++;
        res = move();
        if (res == -1){
            return cnt;
        }
    }

    return 0;
}


int main() {
    freopen("input.txt","r",stdin);

    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            mp[i][j] = 0;
        }
    }

    for (int i=0;i<K;i++){
    }
    
    cin >> N >> K;
    int apple[2];
    for (int i=0;i < K;i++){
        cin >> apple[0] >> apple[1];
        mp[apple[0]-1][apple[1]-1] = 2;
    }

    cin >> L;

    int X;
    char C;
    for (int i=0;i<L;i++){
        cin >> X >> C;
        int ch_dir = C == 'L' ? -1 : 1;
        vector<int> tc;
        tc.push_back(X);
        tc.push_back(ch_dir);
        time_comm.push(tc);
    }

    solution();
    cout << cnt;

    return 0;
}

