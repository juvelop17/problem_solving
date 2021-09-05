//
// Created by Junho Kim on 2021/09/04.
//

#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

int N;
unordered_map<string, int> cmap;


void select(int depth, string order, string sel) {
    if (depth == sel.length()) {
        cmap[sel] += 1;
        return;
    }

    for (int i = 0; i < order.length(); ++i) {
        select(depth, order.substr(i+1), sel + order[i]);
    }
}


vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;
    cmap.clear();

    for (string &order : orders) {
        sort(order.begin(), order.end());
    }

    for (int crs : course) {
        for (string &order : orders) {
            select(crs, order, "");
        }

        int maxn = 0;
        for (auto it : cmap) {
            maxn = max(maxn, it.second);
        }

        for (auto it : cmap) {
            if (maxn >= 2 && it.second == maxn) {
                answer.push_back(it.first);
            }
        }
        cmap.clear();
    }

    sort(answer.begin(), answer.end());

    return answer;
}


#include <iostream>
using namespace std;

int main() {
//    vector<string> orders = {"ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"};
//    vector<int> course = {2,3,4};

    vector<string> orders = {"ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"};
    vector<int> course = {2,3,5};
//
//    vector<string> orders = {"XYZ", "XWY", "WXA"};
//    vector<int> course = {2,3,4};

    solution(orders, course);


    return 0;
}