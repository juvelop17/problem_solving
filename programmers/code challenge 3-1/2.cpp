//
// Created by Junho Kim on 2021/09/09.
//



#include <iostream>


#include <string>
#include <vector>
#include <algorithm>
using namespace std;


int di[4] = {-1, 0, 1, 0};
int dj[4] = {0, 1, 0, -1};
int visit[500][500][4];
vector<int> answer;
int n, m;

bool checkRange(int i, int j) {
    return i >= 0 && i < n && j >= 0 && j < m;
}


void find(vector<string> grid, int ci, int cj, int ck) {
    visit[ci][cj][ck] = 1;

    int ni = (ci + di[ck] + n) % n;
    int nj = (cj + dj[ck] + m) % m;
    int cnt = 1;
    int nk = ck;
    if (grid[ni][nj] == 'L') {
        nk = (nk - 1 + 4) % 4;
    } else if (grid[ni][nj] == 'R') {
        nk = (nk + 1) % 4;
    }
    visit[ni][nj][nk] = 1;
    while (ni != ci || nj != cj || nk != ck) {
        ni = (ni + di[nk] + n) % n;
        nj = (nj + dj[nk] + m) % m;
        if (grid[ni][nj] == 'L') {
            nk = (nk - 1 + 4) % 4;
        } else if (grid[ni][nj] == 'R') {
            nk = (nk + 1) % 4;
        }
        visit[ni][nj][nk] = 1;
        cnt++;
    }
    answer.push_back(cnt);
//    printf("%d %d %d %d\n", ci, cj, ck, cnt);
}

vector<int> solution(vector<string> grid) {
    n = grid.size();
    m = grid[0].size();
    answer.clear();
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            for (int k = 0; k < 4; k++) {
                visit[i][j][k] = 0;
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            for (int k = 0; k < 4; k++) {
                if (!visit[i][j][k]) {
                    find(grid, i, j, k);
                }
            }
        }
    }

    sort(answer.begin(), answer.end());

    return answer;
}




using namespace std;

int main() {
//    vector<string> grid = {"SL","LR"};
    vector<string> grid = {"S"};
//    vector<string> grid = {"R","R"};

//    vector<string> grid = {"S","S"};

    solution(grid);

    for (int i = 0; i < answer.size(); ++i) {
        printf("%d ", answer[i]);
    }

    return 0;
}