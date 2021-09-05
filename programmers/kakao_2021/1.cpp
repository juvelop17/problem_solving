//
// Created by Junho Kim on 2021/09/01.
//

#include <string>
#include <vector>

using namespace std;

string solution(string new_id) {
    string answer = "";

    string res;

    for (char &ch : new_id) {
        if (ch >= 'A' && ch <= 'Z') {
            ch = ch - 'A' + 'a';
        }
    }

    string exp = "-_.";
    for (char &ch : new_id) {
        if ((ch >= 'a' && ch <= 'z') || (ch >= '0' && ch <= '9')
        || exp.find(ch) != -1) {
            res += ch;
        }
    }
    new_id = res;
    res.clear();

    for (char &ch : new_id) {
        if (!res.empty() && res.back() == '.' && ch == '.') {
            continue;
        }
        res += ch;
    }
    new_id = res;
    res.clear();

    if (new_id.front() == '.') new_id.erase(new_id.begin());
    if (new_id.back() == '.') new_id.pop_back();

    if (new_id.empty()) new_id = 'a';

    if (new_id.length() > 15) new_id = new_id.substr(0, 15);
    if (new_id.back() == '.') new_id.pop_back();

    while (new_id.length() <= 2) new_id += new_id.back();

    return new_id;
}


#include <iostream>

int main() {
    freopen("input.txt", "r", stdin);

    string new_id = "...!@BaT#*..y.abcdefghijklm";
//    string new_id = "z-+.^.";
//    string new_id = "abcdefghijklmn.p";

    cout << solution(new_id) << "\n";

    return 0;
}