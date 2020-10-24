#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string inputString) {
    int answer = -1;

    int total_cnt = 0;
    int cnt1 = 0; // ()
    int cnt2 = 0; // {}
    int cnt3 = 0; // []
    int cnt4 = 0; // <

    int index = 0;

    for(int i=0;i<inputString.size();i++){
        cout << inputString[i] << " " << cnt1 << cnt2 << cnt3 << cnt4 << endl;
        if(inputString[i] == '(') {
            total_cnt += 1;
            cnt1 += 1;
        } else if(inputString[i] == ')' && cnt1 > 0) {
            cnt1 -= 1;
        } else if(inputString[i] == '{') {
            total_cnt += 1;
            cnt2 += 1;
        } else if(inputString[i] == '}' && cnt2 > 0) {
            cnt2 -= 1;
        } else if(inputString[i] == '[') {
            total_cnt += 1;
            cnt3 += 1;
        } else if(inputString[i] == ']' && cnt3 > 0) {
            cnt3 -= 1;
        } else if(inputString[i] == '<') {
            total_cnt += 1;
            cnt4 += 1;
        } else if(inputString[i] == '>' && cnt4 > 0) {
            cnt4 -= 1;
        }
    }

    if (cnt1 == 0 && cnt2 == 0 && cnt3 == 0 && cnt4 == 0) {
        answer = total_cnt;
    }

    return answer;
}

int main() {
    string str = "{[}]";
    cout << solution(str) << endl;

    return 0;
}