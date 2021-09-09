//
// Created by Junho Kim on 2021/09/06.
//


#include <string>
#include <vector>
#include <queue>

using namespace std;

#define INF 100000000

int di[4] = {-1, 0, 1, 0};
int dj[4] = {0, 1, 0, -1};
int cardPos[7][2][2];
int minCnt;

bool isFinish(int cmap[][4]) {
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            if (cmap[i][j] != 0) {
                return false;
            }
        }
    }
    return true;
}

bool checkRange(int i, int j) {
    return i >= 0 && i < 4 && j >= 0 && j < 4;
}

struct Node {
    int i;
    int j;
    int move;

    Node(int _i, int _j, int _move) : i(_i), j(_j), move(_move) {}
};


int getDist(int cmap[][4], int ci, int cj, int ti, int tj) {
    int visit[4][4];

    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            visit[i][j] = 0;
        }
    }

    queue<Node*> que;
    que.push(new Node(ci, cj, 0));
    visit[ci][cj] = 1;
    while (!que.empty()){
        Node *cur = que.front();
        que.pop();

        if (cur->i == ti && cur->j == tj) {
            return cur->move;
        }

        for (int d = 0; d < 8; d++) {
            int ni = cur->i + di[d % 4];
            int nj = cur->j + dj[d % 4];
            if (d >= 4) {
                int move = 0;
                while(checkRange(ni, nj) && cmap[ni][nj] == 0) {
                    ni += di[d % 4];
                    nj += dj[d % 4];
                    move++;
                }
                if (!checkRange(ni,nj) && move) {
                    ni -= di[d % 4];
                    nj -= dj[d % 4];
                }
            }
            if (checkRange(ni, nj) && !visit[ni][nj]) {
                visit[ni][nj] = 1;
                que.push(new Node(ni, nj, cur->move + 1));
            }
        }
    }
    return -1;
}


void find(int cmap[][4], int target, int ci, int cj, int cnt) {
    int nmap[4][4];
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            nmap[i][j] = cmap[i][j];
        }
    }

    for (int i = 0; i < 2; ++i) {
        int a = cardPos[target][i][0];
        int b = cardPos[target][i][1];
        int ncnt = cnt;
        ncnt += getDist(cmap, ci, cj, a, b) + 1;

        int c = cardPos[target][(i+1)%2][0];
        int d = cardPos[target][(i+1)%2][1];
        ncnt += getDist(cmap, a, b, c, d) + 1;

        nmap[a][b] = nmap[c][d] = 0;
        if (isFinish(nmap)) {
            if (minCnt > ncnt) {
                minCnt = ncnt;
            }
        }
        for (int nt = 1; nt <= 6; nt++) {
            if (cardPos[nt][0][0] == -1 || nmap[cardPos[nt][0][0]][cardPos[nt][0][1]] == 0) {
                continue;
            }
            find(nmap, nt, c, d, ncnt);
        }
    }
}

int solution(vector<vector<int>> board, int r, int c) {
    int cmap[4][4];
    minCnt = INF;

    for (int i = 0; i < 7; ++i) {
        for (int j = 0; j < 2; ++j) {
            for (int k = 0; k < 2; ++k) {
                cardPos[i][j][k] = -1;
            }
        }
    }

    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            cmap[i][j] = board[i][j];
            if (board[i][j] != 0) {
                if (cardPos[board[i][j]][0][0] == -1) {
                    cardPos[board[i][j]][0][0] = i;
                    cardPos[board[i][j]][0][1] = j;
                } else {
                    cardPos[board[i][j]][1][0] = i;
                    cardPos[board[i][j]][1][1] = j;
                }
            }
        }
    }

    for (int target = 1; target <= 6; target++) {
        if (cardPos[target][0][0] == -1 || cmap[cardPos[target][0][0]][cardPos[target][0][1]] == 0) {
            continue;
        }
        find(cmap, target, r, c, 0);
    }

    return minCnt;
}


#include <iostream>

using namespace std;

int main() {
//    vector<vector<int>> board = {{1,0,0,3},{2,0,0,0},{0,0,0,2},{3,0,1,0}};
//    int r = 1;
//    int c = 0;

    vector<vector<int>> board = {{3,0,0,2},{0,0,1,0},{0,1,0,0},{2,0,0,3}};
    int r = 1;
    int c = 0;

    cout << solution(board, r, c);

    return 0;
}




