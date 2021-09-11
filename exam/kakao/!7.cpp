#include <iostream>


#include <string>
#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

#define INF 100000000

unordered_set<int> endCnt[2];
int N, M;

int di[4] = {-1, 0, 1, 0};
int dj[4] = {0, 1, 0, -1};

bool checkRange(vector<int> loc) {
    return loc[0] >= 0 && loc[0] < N && loc[1] >= 0 && loc[1] < M;
}

bool dfs(int mode, int sel, vector<vector<int>> board, vector<int> aloc, vector<int> bloc, int cnt) {
    vector<int> loc;
    if (sel == 0) {
        loc = aloc;
    } else {
        loc = bloc;
    }
    if (board[loc[0]][loc[1]] == 0) {
        if (sel == 1 && sel == mode) {
            endCnt[mode].insert(cnt);
            return true;
        }
        return false;
    }

    bool move = false;
    vector<int> che(4, -1);
    for (int d = 0; d < 4; d++) {
        vector<int> nextLoc = loc;
        nextLoc[0] += di[d];
        nextLoc[1] += dj[d];

        if (checkRange(nextLoc) && board[nextLoc[0]][nextLoc[1]]) {
            move = true;
            board[loc[0]][loc[1]] = 0;
            if (sel == 0) {
                che[d] = dfs(mode, 1, board, nextLoc, bloc, cnt + 1);
            } else {
                che[d] = dfs(mode, 0, board, aloc, nextLoc, cnt + 1);
            }
            board[loc[0]][loc[1]] = 1;
        }
    }
    if (!move) {
        if (sel == 0 && sel == mode) {
            endCnt[mode].insert(cnt);
            return true;
        }
        return false;
    }
}

int solution(vector<vector<int>> board, vector<int> aloc, vector<int> bloc) {
    endCnt[0].clear();
    endCnt[1].clear();

    N = board.size();
    M = board[0].size();
    dfs(0,0, board, aloc, bloc, 0);
    dfs(1,0, board, aloc, bloc, 0);

    vector<int> res[2];
    for (int i = 0; i < 2; ++i) {
        res[i].assign(endCnt[i].begin(), endCnt[i].end());
        sort(res->begin(), res->end());
    }

    if (res[0].size() < res[1].size()) {
        return res[1].front();
    } else if (res[0].size() > res[1].size()) {
        return res[0].back();
    } else {
        return res[0].back();
    }
}




int main() {
//    ios::sync_with_stdio(false);
//    cin.tie(NULL);
//    cout.tie(NULL);

//    vector<vector<int>> board = {{1, 1, 1}, {1, 1, 1}, {1, 1, 1}}	;
//    vector<int> aloc = {1, 0}	;
//    vector<int> bloc = {1, 2}	;

//    vector<vector<int>> board = {{1, 1, 1}, {1, 0, 1}, {1, 1, 1}}	;
//    vector<int> aloc = {1, 0}	;
//    vector<int> bloc = {1, 2}	;

//    vector<vector<int>> board = {{1, 1, 1, 1, 1}}	;
//    vector<int> aloc = {0, 0}	;
//    vector<int> bloc = {0, 4}	;

    vector<vector<int>> board = {{1}}	;
    vector<int> aloc = {0, 0}	;
    vector<int> bloc = {0, 0}	;
//
    cout << solution(board, aloc, bloc);


    return 0;
}

