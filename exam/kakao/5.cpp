#include <string>
#include <vector>
#include <unordered_set>

using namespace std;
vector<int> info;
vector<int> conn[20];
int N;
int maxSheep;

int find(int curNode, int sheep, int wolf, unordered_set<int> candi) {
//    printf("%d %d %d\n", curNode, sheep, wolf);
//    for (auto c : candi) {
//        printf("%d ", c);
//    }
//    printf("\n");

    if (info[curNode] == 0) {
        sheep +=1;
    }
    else {
        wolf += 1;
    }

    if (maxSheep < sheep) {
        maxSheep = sheep;
    }

    for (int i = 0; i < conn[curNode].size(); ++i) {
        int nextNode = conn[curNode][i];
        candi.insert(nextNode);
    }

    vector<int> candiList(candi.begin(), candi.end());
    int maxCnt = 0;
    for (int i = 0; i < candiList.size(); ++i) {
        int nextNode = candiList[i];
        if (info[nextNode] >= sheep - wolf) { // 현재 카운트와 앞으로 늑대일 경우 계산 검증 필요
            continue;
        }
        candi.erase(nextNode);
        int curCnt = find(nextNode, sheep, wolf, candi);
        candi.insert(nextNode);
        if (maxCnt < curCnt) {
            maxCnt = curCnt;
        }
    }

    return maxCnt;
}



int solution(vector<int> _info, vector<vector<int>> edges) {
    info = _info;
    N = info.size();

    for (int i = 0; i < N; ++i) {
        conn->clear();
    }

    for (int i = 0; i < edges.size(); ++i) {
        conn[edges[i][0]].push_back(edges[i][1]);
    }

    unordered_set<int> candi;
    find(0, 0, 0, candi);

    return maxSheep;
}


#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

//    vector<int> info = {0,0,1,1,1,0,1,0,1,0,1,1};
//    vector<vector<int>> edges = {{0,1},{1,2},{1,4},{0,8},{8,7},{9,10},{9,11},{4,3},{6,5},{4,6},{8,9}};

    vector<int> info = {0,1,0,1,1,0,1,0,0,1,0};
    vector<vector<int>> edges = {{0,1},{0,2},{1,3},{1,4},{2,5},{2,6},{3,7},{4,8},{6,9},{9,10}};

    cout << solution(info, edges);


    return 0;
}




