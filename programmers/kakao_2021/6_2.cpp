//
// Created by Junho Kim on 2021/09/06.
//

int calCnt = 0;


#include <string>
#include <vector>

using namespace std;


#define INF 100000000

int di[4] = {-1, 0, 1, 0};
int dj[4] = {0, 1, 0, -1};
int mp[4][4];
int visit[4][4];
int minCnt;

bool isFinish() {
    bool isClear = true;
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            if (mp[i][j] != 0) {
                isClear = false;
                break;
            }
        }
    }
    return isClear;
}

bool checkRange(int i, int j) {
    return i >= 0 && i < 4 && j >= 0 && j < 4;
}

void printMap(int m[][4]) {
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            printf("%d ", m[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

void find(int ci, int cj, int si, int sj, int selCnt, int cnt) {
    if (cnt >= minCnt) {
        return;
    }

    calCnt++;
//    printf("%d %d %d %d %d %d %d\n", ci, cj, si, sj, selCnt, cnt, calCnt);
//    printMap(mp);
//    printMap(visit);

    int cardNum = -1;
    int ti = si; int tj = sj;

    if (si != -1 && sj != -1) {
        if (mp[si][sj] == mp[ci][cj]) {
            cardNum = mp[si][sj];
            mp[si][sj] = mp[ci][cj] = 0;
            cnt++;
            selCnt++;
            si = sj = -1;

            if (isFinish()) {
                mp[ti][tj] = mp[ci][cj] = cardNum;
                if (minCnt > cnt) {
                    minCnt = cnt;
                }
                return;
            }
        }
    } else {
        if (mp[ci][cj] != 0) {
            si = ci; sj = cj;
            cnt++;
        }
    }

    for (int d = 0; d < 4; ++d) {
        int ni = ci + di[d % 4];
        int nj = cj + dj[d % 4];

        if (d >= 4) {
            while (checkRange(ni, nj) && mp[ni][nj] == 0) {
                ni += di[d % 4];
                nj += dj[d % 4];
            }
            if (!checkRange(ni, nj)) {
                ni -= di[d % 4];
                nj -= dj[d % 4];
            }
            if (ci == ni && cj == nj) {
                continue;
            }
        }
        if (checkRange(ni, nj) && visit[ni][nj] != selCnt) {
            int tmp = visit[ni][nj];
            visit[ni][nj] = selCnt;
            find(ni, nj, si, sj, selCnt, cnt + 1);
            visit[ni][nj] = tmp;
        }
    }

    if (cardNum != -1) {
        mp[ti][tj] = mp[ci][cj] = cardNum;
    }
}


int solution(vector<vector<int>> board, int r, int c) {
    memset(visit, -1, sizeof(visit));
    minCnt = INF;

    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            mp[i][j] = board[i][j];
        }
    }

    find(r,c,-1,-1,0,0);

    return minCnt;
}


#include <iostream>

using namespace std;

int main() {
    vector<vector<int>> board = {{1,0,0,3},{2,0,0,0},{0,0,0,2},{3,0,1,0}};
    int r = 1;
    int c = 0;

    cout << solution(board, r, c);

    return 0;
}




