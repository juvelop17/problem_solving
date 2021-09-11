

#include <iostream>


#include <string>
#include <vector>

using namespace std;

int dest[1000][1000];
int N, M;

void destroy(int r1, int c1, int r2, int c2) {

}

int solution(vector<vector<int>> board, vector<vector<int>> skill) {
    N = board.size();
    M = board[0].size();
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            dest[i][j] = 0;
        }
    }

    for (int i = 0; i < skill.size(); ++i) {
        vector<int> cur = skill[i];
        if (cur[0] == 1) {
            for (int x = cur[1]; x <= cur[3]; x++) {
                for (int y = cur[2]; y <= cur[4]; y++) {
                    board[x][y] -= cur[5];
                }
            }
        } else {
            for (int x = cur[1]; x <= cur[3]; x++) {
                for (int y = cur[2]; y <= cur[4]; y++) {
                    board[x][y] += cur[5];
                }
            }
        }
    }

    int cnt = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (board[i][j] >= 1) {
                cnt++;
            }
        }
    }

    return cnt;
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    vector<vector<int>> board = {{5,5,5,5,5},{5,5,5,5,5},{5,5,5,5,5},{5,5,5,5,5}};
    vector<vector<int>> skill = {{1,0,0,3,4,4},{1,2,0,2,3,2},{2,1,0,3,1,2},{1,0,1,3,3,1}};

    
//    vector<vector<int>> board = {{1,2,3},{4,5,6},{7,8,9}};
//    vector<vector<int>> skill = {{1,1,1,2,2,4},{1,0,0,1,1,2},{2,2,0,2,0,100}};


    cout << solution(board, skill);

    return 0;
}