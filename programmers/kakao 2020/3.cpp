//
// Created by Junho Kim on 2021/09/09.
//


#include <iostream>



#include <string>
#include <vector>

using namespace std;

#define MAX_N 20
#define MAX_M 20

int k[MAX_M][MAX_M];
int l[MAX_N][MAX_N];
int board[MAX_N+(MAX_M-1)*2][MAX_N+(MAX_M-1)*2];
int M, N;


bool correct(int ci, int cj) {
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            board[i + M - 1][j + M - 1] = l[i][j];
        }
    }

    for (int i = 0; i < M; ++i) {
        for (int j = 0; j < M; ++j) {
            board[ci + i][cj + j] += k[i][j];
        }
    }

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (board[i + M - 1][j + M - 1] != 1) {
                return false;
            }
        }
    }
    return true;
}

void rotate() {
    int nk[MAX_M][MAX_M];
    for (int i = 0; i < M; ++i) {
        for (int j = 0; j < M; ++j) {
            nk[i][j] = k[i][j];
        }
    }
    for (int i = 0; i < M; ++i) {
        for (int j = 0; j < M; ++j) {
            k[j][M-1-i] = nk[i][j];
        }
    }
}

bool solution(vector<vector<int>> key, vector<vector<int>> lock) {
    M = key.size();
    N = lock.size();

    for (int i = 0; i < M; ++i) {
        for (int j = 0; j < M; ++j) {
            k[i][j] = key[i][j];
        }
    }
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            l[i][j] = lock[i][j];
        }
    }

    for (int d = 0; d < 4; d++) {
        rotate();
        for (int i = 0; i < N + M - 1; ++i) {
            for (int j = 0; j < N + M - 1; ++j) {
                if (correct(i, j)) {
                    return true;
                }
            }
        }
    }

    return false;
}




int main() {
    vector<vector<int>> key = {{0, 0, 0}, {1, 0, 0}, {0, 1, 1}};
    vector<vector<int>> lock = {{1, 1, 1}, {1, 1, 0}, {1, 0, 1}};

    printf("%d\n", solution(key, lock));

    return 0;
}



