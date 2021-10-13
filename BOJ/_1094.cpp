//
// Created by Junho Kim on 2021/10/13.
//




#include <iostream>
#include <vector>

#define INF 100000000


using namespace std;



int solution(int x) {
    vector<int> sticks = {64};
    int numSum = 64;
    while (numSum > x) {
        int minIdx = 0;
        int minStick = INF;
        for (int i = 0; i < sticks.size() ; i++) {
            if (sticks[i] < minStick) {
                minStick = sticks[i];
                minIdx = i;
            }
        }
        minStick /= 2;
        sticks.erase(sticks.begin() + minIdx);
        sticks.push_back(minStick);
        sticks.push_back(minStick);

        numSum = 0;
        for (int i = 0; i < sticks.size(); i++) {
            numSum += sticks[i];
        }
        if (numSum - minStick >= x) {
            numSum -= minStick;
            sticks.pop_back();
        }
    }

    return sticks.size();
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
//    freopen("input.txt", "r", stdin);

    int x;
    cin >> x;
    cout << solution(x);


    return 0;
}