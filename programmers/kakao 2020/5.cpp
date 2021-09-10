//
// Created by Junho Kim on 2021/09/10.
//
#include <iostream>

#include <string>
#include <vector>

using namespace std;

int board[101][101][2];
int n;

bool check() {
    for (int i = 0; i <= n; ++i) {
        for (int j = 0; j <= n; ++j) {
            for (int k = 0; k < 2; ++k) {
                if (board[i][j][k]) {
                    if (k == 0) {
                        if (j == 0) continue;
                        if (i > 0 && board[i-1][j][1]) continue;
                        if (board[i][j][1]) continue;
                        if (board[i][j-1][0]) continue;
                        return false;
                    } else {
                        if (j > 0 && board[i][j-1][0]) continue;
                        if (j > 0 && i < n && board[i+1][j-1][0]) continue;
                        if (i > 0 && i < n && board[i-1][j][1] && board[i+1][j][1]) continue;
                        return false;
                    }
                }
            }
        }
    }
    return true;
}

void build(vector<int> frame) {
    int x = frame[0];
    int y = frame[1];
    int a = frame[2];
    int b = frame[3];

    board[x][y][a] = b;
    if (check()) {
        return;
    }
    board[x][y][a] = !b;
}

vector<vector<int>> solution(int _n, vector<vector<int>> build_frame) {
    vector<vector<int>> answer;
    n = _n;

    for (int i = 0; i <= n; ++i) {
        for (int j = 0; j <= n; ++j) {
            for (int k = 0; k < 2; ++k) {
                board[i][j][k] = 0;
            }
        }
    }

    for (int i = 0; i < build_frame.size(); ++i) {
        build(build_frame[i]);
    }

    for (int i = 0; i <= n; ++i) {
        for (int j = 0; j <= n; ++j) {
            for (int k = 0; k < 2; k++) {
                if (board[i][j][k]) {
                    answer.push_back({i, j, k});
                }
            }
        }
    }

    return answer;
}



int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n = 5;
    vector<vector<int>> build_frame = {{1,0,0,1},{1,1,1,1},{2,1,0,1},{2,2,1,1},{5,0,0,1},{5,1,0,1},{4,2,1,1},{3,2,1,1}};

//    int n = 5;
//    vector<vector<int>> build_frame = {{0,0,0,1},{2,0,0,1},{4,0,0,1},{0,1,1,1},{1,1,1,1},{2,1,1,1},{3,1,1,1},{2,0,0,0},{1,1,1,0},{2,2,0,1}};

    solution(n, build_frame);

    return 0;
}





