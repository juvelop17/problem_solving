#include <iostream>

using namespace std;


int N, M;
char mp[10][10];
int mem[10][10][10][10];
int goal[2];
int red[2];
int blue[2];

int di[4] = {-1,1,0,0};
int dj[4] = {0,0,-1,1};

void displayMap(int dir, int ri,int rj,int bi,int bj){
    cout << dir << endl;
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            if(i == ri && j == rj) {
                cout << 'R';
            } else if(i == bi && j == bj){
                cout << 'B';
            } else if(i == goal[0] && j == goal[1]){
                cout << 'O';
            } else {
                cout << mp[i][j];
            }
        }
        cout << endl;
    }
    cout << endl;
}


int move(int cnt, char dir, int ri, int rj, int bi, int bj) {
    int res;

    if (cnt > 10 || (mem[ri][rj][bi][bj] != 0 && mem[ri][rj][bi][bj] < cnt)){
        return -1;
    }
    mem[ri][rj][bi][bj] = cnt;

    int rm = 0, bm = 0;

    bm = 0;
    while (mp[bi][bj] != '#') {
        bm += 1;
        bi += di[dir]; bj += dj[dir];
        if (bi == goal[0] && bj == goal[1]) {
            return -1;
        }
    }
    bi -= di[dir]; bj -= dj[dir];

    rm = 0;
    while (mp[ri][rj] != '#') {
        rm += 1;
        ri += di[dir]; rj += dj[dir];
        if (ri == goal[0] && rj == goal[1]) {
            return cnt;
        }
    }
    ri -= di[dir]; rj -= dj[dir];

    if (ri == bi && rj == bj){
        if (rm >= bm) {
            ri -= di[dir]; rj -= dj[dir];
        } else {
            bi -= di[dir]; bj -= dj[dir];
        }
    }

    // displayMap(dir,ri,rj,bi,bj);

    res = 11;
    int tmp;
    tmp = move(cnt+1,0,ri,rj,bi,bj); res = tmp != -1 && tmp < res ? tmp : res;
    tmp = move(cnt+1,1,ri,rj,bi,bj); res = tmp != -1 && tmp < res ? tmp : res;
    tmp = move(cnt+1,2,ri,rj,bi,bj); res = tmp != -1 && tmp < res ? tmp : res;
    tmp = move(cnt+1,3,ri,rj,bi,bj); res = tmp != -1 && tmp < res ? tmp : res;

    return res;
}

int solution() {
    int res = 11, cnt = 0;

    int tmp;
    tmp = move(1,0,red[0],red[1],blue[0],blue[1]); res = tmp != -1 && tmp < res ? tmp : res;
    tmp = move(1,1,red[0],red[1],blue[0],blue[1]); res = tmp != -1 && tmp < res ? tmp : res;
    tmp = move(1,2,red[0],red[1],blue[0],blue[1]); res = tmp != -1 && tmp < res ? tmp : res;
    tmp = move(1,3,red[0],red[1],blue[0],blue[1]); res = tmp != -1 && tmp < res ? tmp : res;

    if (res == 11) {
        res = -1;
    }

    return res;
}

int main() {
    freopen("input.txt", "r", stdin);

    cin >> N >> M;
    for (int i=0;i<N;i++) {
        for (int j=0;j<M;j++){
            cin >> mp[i][j];
            if (mp[i][j] == 'O') {
                goal[0] = i;
                goal[1] = j;
                mp[i][j] = '.';
            } else if (mp[i][j] == 'R') {
                red[0] = i;
                red[1] = j;
                mp[i][j] = '.';
            } else if (mp[i][j] == 'B') {
                blue[0] = i;
                blue[1] = j;
                mp[i][j] = '.';
            }
        }
    }

    for(int a1=0;a1<N;a1++){
        for(int a2=0;a2<N;a2++){
            for(int a3=0;a3<N;a3++){
                for(int a4=0;a4<N;a4++){
                    mem[a1][a2][a3][a4] = 0;
                }
            }
        }
    }

    cout << solution();

    return 0;
}




