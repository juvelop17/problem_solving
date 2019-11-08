#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int k,n;
string s,t;

int solution(){
    int cnt=0;
    char ch_s, ch_t;

    bool isTrue = true;

    for(int i=0;i<n;i++){
        if (s[i]!=t[i]){
            cnt++;
            if(cnt == 1){
                ch_s = s[i];
                ch_t = t[i];
                isTrue = false;
            } else if (cnt == 2){
                if (ch_s == s[i] && ch_t == t[i]){
                    isTrue = true;
                } else {
                    isTrue = false;
                }   
            } else {
                isTrue = false;
                break;
            }
        }
    }

    if (isTrue){
        cout << "Yes" << endl;
        return 0;
    }
    
    cout << "No" << endl;
    return 0;
}


int main(){
    // freopen("input.txt","r",stdin);

    cin >> k;
    for(int i=0;i<k;i++){
        cin >> n;
        cin >> s;
        cin >> t;
        solution();
    }

    return 0;
}


