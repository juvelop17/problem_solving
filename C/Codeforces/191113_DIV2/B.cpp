#include <iostream>
#include <cstdio>

using namespace std;


int mem_arr[5];
int t,x,y;

int solution() {

    int num;
    num = x;
    if (x >= y){
        return 1;
    }

    // if (x <= 3){
    //     if(x < y){
    //         return 0;
    //     }
    // }

    if (x < 2 && y >= 2){
        return 0;
    }

    if (x <= 3 && y > 3) {
        return 0;
    }

    return 1;
}


int main() {
    // freopen("input.txt","r",stdin);

    cin >> t;
    for(int i=0;i<t;i++){
        cin >> x >> y;
        cout << (solution() ? "YES" : "NO") << endl;
    }

    return 0;
}


