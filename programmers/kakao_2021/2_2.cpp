//
// Created by Junho Kim on 2021/09/04.
//

#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

int N;
unordered_map<string, int> courseMap;


int contain(string a, string b) {
    int i = 0, j = 0;
    while(i < a.length()) {
        while (j < b.length()) {
            if (a[i] == b[j]) {
                i++; j++;
            } else {
                j++;
            }
        }
        if (i < a.length() && j == b.length()) {
            return -1; // 미포함
        }
    }

    if (a.length() == b.length()) {
        return 0; // 동일
    }
    return 1; // 포함
}


void select(int num, string order, int idx, string sel, int cnt) {
    if (num == cnt) {
        courseMap[sel] += 1;
        return;
    }

    for (int i = idx + 1; i < order.length(); ++i) {
        select(num, order, i, sel + order[i], cnt + 1);
    }
}


vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;
    courseMap.clear();

    for (int i = 0; i < orders.size(); ++i) {
        for (int j = 0; j < course.size(); ++j) {
            sort(orders[i].begin(), orders[i].end());
            select(course[j], orders[i], -1, "", 0);
        }
    }

    vector<pair<string, int>> v;
    vector<string> candi[21];
    v.assign(courseMap.begin(), courseMap.end());
    for (int i = 0; i < v.size(); ++i) {
        candi[v[i].second].push_back(v[i].first);
    }


    for (int c = 0; c < course.size(); c++) {
        for (int i = 20; i >= 2; i--) {
            bool isFind = false;
            for (int j = 0; j < candi[i].size(); ++j) {
                string cur = candi[i][j];
                if (course[c] != cur.length()) {
                    continue;
                }
                answer.push_back(cur);
                isFind = true;
            }
            if (isFind) {
                break;
            }
        }
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