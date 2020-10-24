#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string road, int n) {
    int answer = -1;

    char str_buff[1000];
    strcpy(str_buff, road.c_str());

    char *tok = strtok(str_buff, "0");
    while (tok != nullptr) {
        cout << tok << endl;
        tok = strtok(nullptr, "0");
    }

    return answer;
}

int main() {
    string road = "111011110011111011111100011111";
    int n = 3;

    cout << solution(road,n) << endl;
    
    return 0;
}