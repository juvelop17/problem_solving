//
// Created by Junho Kim on 2021/09/11.
//



#include <string>
#include <vector>
#include <queue>

using namespace std;

queue<vector<int>> work[101];
int priSum[101];

int nextWork() {
    int priMax = 0;
    int curWork = -1;
    for (int i = 1; i <= 100; ++i) {
        if (priSum[i] > priMax) {
            priMax = priSum[i];
            curWork = i;
        }
    }
    return curWork;
}


vector<int> solution(vector<vector<int>> jobs) {
    vector<int> answer;

    for (int i = 1; i < 101; ++i) {
        priSum[i] = 0;
    }

    int jobIdx = 0;
    int currentTime = 1;

    int curWork = -1;
    while (!(jobIdx == jobs.size() && nextWork() == -1)) {
        while (jobIdx < jobs.size() && currentTime >= jobs[jobIdx][0]) {
            vector<int> cur = jobs[jobIdx++];
            work[cur[2]].push(cur);
            priSum[cur[2]] += cur[3];
        }

        if (curWork != -1 && !work[curWork].empty()) {
            while (!work[curWork].empty()) {
                vector<int> cur = work[curWork].front();
                work[curWork].pop();

                currentTime += cur[1];
                priSum[cur[2]] -= cur[3];
            }
            continue;
        }

        curWork = nextWork();
        if (jobIdx < jobs.size() && curWork == -1) {
            currentTime = jobs[jobIdx][0];
            continue;
        }
        while (!work[curWork].empty()) {
            vector<int> cur = work[curWork].front();
            work[curWork].pop();

            currentTime += cur[1];
            priSum[cur[2]] -= cur[3];
        }

        if (answer.size() == 0 || answer.back() != curWork) {
            answer.push_back(curWork);
        }
    }

    return answer;
}


#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
//    vector<vector<int>> jobs = {{1, 5, 2, 3}, {2, 2, 3, 2}, {3, 1, 3, 3}, {5, 2, 1, 5}, {7, 1, 1, 1}, {9, 1, 1, 1}, {10, 2, 2, 9}};

    vector<vector<int>> jobs = {{0, 2, 3, 1}, {5, 3, 3, 1}, {10, 2, 4, 1}}	;

    vector<int> v = solution(jobs);
    for (int i = 0; i < v.size(); ++i) {
        cout << v[i] << " ";
    }



    return 0;
}

