//
// Created by Junho Kim on 2021/09/08.
//
#include <iostream>




#include <string>
#include <vector>
using namespace std;

#define INF ((1<<31)-1)

vector<int> child[300001];
int memo[300001][2];
int snum[300001];

void find(int parent) {
    if (child[parent].empty()) {
        memo[parent][0] = 0;
        memo[parent][1] = snum[parent];
        return;
    }

    for (int i = 0; i < child[parent].size(); ++i) {
        find(child[parent][i]);
    }

    bool isSelected = false;
    int minDiff = INF;
    for (int i = 0; i < child[parent].size(); ++i) {
        int cur = child[parent][i];
        if (memo[cur][0] < memo[cur][1]) {
            memo[parent][0] += memo[cur][0];
        } else {
            isSelected = true;
            memo[parent][0] += memo[cur][1];
        }
        minDiff = min(minDiff, memo[cur][1] - memo[cur][0]);
    }
    memo[parent][1] = memo[parent][0] + snum[parent];
    if (!isSelected) {
        memo[parent][0] += minDiff;
    }
}


int solution(vector<int> sales, vector<vector<int>> links) {
    for (int i = 1; i < 300001; ++i) {
        child[i].clear();
        memo[i][0] = 0;
        memo[i][1] = 0;
    }
    for (int i = 0; i < sales.size(); ++i) {
        snum[i+1] = sales[i];
    }
    for (int i = 0; i < links.size(); ++i) {
        child[links[i][0]].push_back(links[i][1]);
    }
    find(1);

    return min(memo[1][0], memo[1][1]);
}



using namespace std;

int main() {
//    vector<int> sales = {14, 17, 15, 18, 19, 14, 13, 16, 28, 17};
//    vector<vector<int>> links = {{10, 8}, {1, 9}, {9, 7}, {5, 4}, {1, 5}, {5, 10}, {10, 6}, {1, 3}, {10, 2}};

//    vector<int> sales = {5, 6, 5, 3, 4};
//    vector<vector<int>> links = {{2,3}, {1,4}, {2,5}, {1,2}};

    vector<int> sales = {5, 6, 5, 1, 4}	;
    vector<vector<int>> links = {{2,3}, {1,4}, {2,5}, {1,2}};

    cout << solution(sales, links);

    return 0;
}


