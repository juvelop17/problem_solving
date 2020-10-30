#include <iostream>
#include <iomanip>
#include <string>

using namespace std;
int t;

int solution(int n, string s) {
    cout << s << endl;
    int cnt1, cnt2; // 홀수가 1, 짝수가 1
    cnt1 = cnt2 = 0;
    for (int i=0;i<n;i++){
        cout << "i : " << i << " " << s[i] << endl;
        if(i % 2 == 0){ // even
            if(s[i] == '1'){
                cnt1++;
            } else {
                cnt2++;
            }
        } else { // odd
            if(s[i] == '1'){
                cnt2++;
            } else {
                cnt1++;
            }
        }
        cout << "cnt1, cnt2 " << cnt1 << " " << cnt2 << endl;
    }

    if (cnt1 < cnt2) {
        cout << cnt1 << endl;
    } else {
        cout << cnt2 << endl;
    }

    return 0;  
}


int main() {
    freopen("input.txt","r",stdin);
    int ptime = clock();

    cin >> t;
    for (int i=0;i<t;i++){
        int n;
        string s;
        cin >> n >> s;
        solution(n,s);
    }
    
    cout << "time : " << clock() - ptime << endl;

    return 0;
}









