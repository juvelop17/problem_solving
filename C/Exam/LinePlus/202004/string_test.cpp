#include <iostream>

using namespace std;

int main() {
    // 문자열 토크나이징
    char str_res[1000];
    int str_cnt;

    string a = "My,name is kukaro";
    char str_buff[1000];
    strcpy(str_buff, a.c_str());

    cout << str_buff << endl;
    cout << a.c_str() << endl;

    char *tok = strtok(str_buff, ",");
    cout << tok << endl;
    cout << sizeof(tok) << endl;

    while (tok != nullptr) {
        cout << tok << endl;
        tok = strtok(nullptr, " ");
    }

    // 문자열 숫자형으로 변환
    char num_test[10] = "2020";
    int num = atoi(num_test);
    cout << num << endl;
}


