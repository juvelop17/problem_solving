//
// Created by Junho Kim on 2021/09/11.
//

#include <iostream>



#include <string>
#include <vector>
#include <queue>

using namespace std;


int board[101][101];
int visit[101][101][101][101];
int n;

int di[4] = {-1, 0, 1, 0};
int dj[4] = {0, 1, 0, -1};

struct Robot {
    int pos[4];
    int cnt;

    Robot(int _pos[], int _cnt) {
        for (int i = 0; i < 4; ++i) {
            pos[i] = _pos[i];
        }
        cnt = _cnt;
    }
};

bool checkRange(int i, int j) {
    return i > 0 && i <= n && j > 0 && j <= n;
}

bool checkRange(int pos[]) {
    return pos[0] > 0 && pos[0] <= n &&
            pos[1] > 0 && pos[1] <= n &&
            pos[2] > 0 && pos[2] <= n &&
            pos[3] > 0 && pos[3] <= n;
}

void rotate(int pos[], int clock) { // 0 : 반시계, 1: 시계
    if (pos[0] == pos[2]) { // 가로
        if (clock == 0) { // 반시계
            int ni = pos[1] > pos[3] ? pos[0] + 1 : pos[0] - 1;
            int nj = pos[1];
            if (checkRange(ni, nj) && !board[ni][nj] && !board[ni][pos[3]]) {
                pos[2] = ni;
                pos[3] = nj;
            }
        } else { // 시계
            int ni = pos[1] < pos[3] ? pos[0] + 1 : pos[0] - 1;
            int nj = pos[1];
            if (checkRange(ni, nj) && !board[ni][nj] && !board[ni][pos[3]]) {
                pos[2] = ni;
                pos[3] = nj;
            }
        }
    } else { // 세로
        if (clock == 0) { // 반시계
            int ni = pos[0];
            int nj = pos[0] > pos[2] ? pos[1] - 1 : pos[1] + 1;
            if (checkRange(ni, nj) && !board[ni][nj] && !board[pos[2]][nj]) {
                pos[2] = ni;
                pos[3] = nj;
            }
        } else { // 시계
            int ni = pos[0];
            int nj = pos[0] < pos[2] ? pos[1] - 1 : pos[1] + 1;
            if (checkRange(ni, nj) && !board[ni][nj] && !board[pos[2]][nj]) {
                pos[2] = ni;
                pos[3] = nj;
            }
        }
    }
}

bool finish(int pos[]) {
    return (pos[0] == n && pos[1] == n) || (pos[2] == n && pos[3] == n);
}

int solution(vector<vector<int>> b) {
    n = b.size();

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            board[i][j] = b[i-1][j-1];
            for (int k = 1; k <= n; k++) {
                for (int l = 1; l <= n; l++) {
                    visit[i][j][k][l] = 0;
                }
            }
        }
    }

    queue<Robot*> que;
    int pos[4] = {1, 1, 1, 2};
    que.push(new Robot(pos, 0));
    visit[1][1][1][2] = 1;
    visit[1][2][1][1] = 1;
    while (!que.empty()) {
        Robot *cur = que.front();
        que.pop();

        if (finish(cur->pos)) {
            return cur->cnt;
        }

        for (int d = 0; d < 8; d++) {
            int npos[4];
            for (int i = 0; i < 4; ++i) {
                npos[i] = cur->pos[i];
            }
            if (d < 4) {
                for (int i = 0; i < 4; ++i) {
                    if (i == 0 || i == 2) {
                        npos[i] += di[d];
                    } else {
                        npos[i] += dj[d];
                    }
                }
            } else if (d < 6) {
                rotate(npos, d - 4);
            } else {
                int t[4] = {npos[2],npos[3],npos[0],npos[1]};
                for (int i = 0; i < 4; ++i) {
                    npos[i] = t[i];
                }
                rotate(npos, d - 6);
            }

            if (checkRange(npos) && !board[npos[0]][npos[1]] && !board[npos[2]][npos[3]] &&
            !visit[npos[0]][npos[1]][npos[2]][npos[3]] && !visit[npos[2]][npos[3]][npos[0]][npos[1]] ) {
                visit[npos[0]][npos[1]][npos[2]][npos[3]] = 1;
                visit[npos[2]][npos[3]][npos[0]][npos[1]] = 1;
                que.push(new Robot(npos, cur->cnt + 1));
            }
        }
    }

    return -1;
}





int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);


    vector<vector<int>> b = {{0, 0, 0, 1, 1},{0, 0, 0, 1, 0},{0, 1, 0, 1, 1},{1, 1, 0, 0, 1},{0, 0, 0, 0, 0}}	;

    cout << solution(b);

    return 0;
}