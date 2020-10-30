#include <iostream>
#include <iomanip>

using namespace std;
int t,l,r;

int solution(long long l, long long r){
    bool is_success = false;
    long long int a;

    a = l * 2 / 3;
    if (a * 2 > r) {
        is_success = true;
    }
    // cout << a << endl;

    a = l * 2;
    if (a > r) {
        is_success = true;
    }
    // cout << a << endl;

    if (is_success){
        cout << "YES" << endl;
    } else {   
        cout << "NO" << endl;
    }

    return 0;  
}


int main() {
    // freopen("input.txt","r",stdin);
    int ptime = clock();

    cin >> t;
    for (int i=0;i<t;i++){
        cin >> l >> r;
        solution(l,r);
    }
    
    // cout << "time : " << clock() - ptime << endl;

    return 0;
}









