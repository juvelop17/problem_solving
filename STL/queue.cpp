//
// Created by Junho Kim on 2021/08/20.
//


#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<int> qu;
    qu.push(1);
    qu.push(9);
    qu.push(5);
    int sz = qu.size();
    for(int i=0;i<sz;i++){
        cout << qu.front() << ',';
        qu.pop();
    }cout << '\n';

    return 0;
}