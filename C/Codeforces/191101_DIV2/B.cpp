#include <iostream>
#include <cstdio>
#include <string>

using namespace std;


int t,n,a,b,c;
int ba,bb,bc;
string bob_str;
string alice_str;


void bobCount(){
    ba=bb=bc=0;

    char ch;
    for (int i=0;i<bob_str.length();i++){
        ch = bob_str[i];
        if (ch == 'R'){
            ba += 1;
        } else if (ch=='P'){
            bb += 1;
        } else if (ch=='S'){
            bc += 1;
        }
    }
}



int solution(){
    int win_cnt,a_cnt,b_cnt,c_cnt;
    win_cnt=a_cnt=b_cnt=c_cnt=0;

    a_cnt += min(a,bc);
    b_cnt += min(b,ba);
    c_cnt += min(c,bb);
    win_cnt = a_cnt + b_cnt + c_cnt;

    if (win_cnt * 2 < n){
        return 0;   // NO
    }

    alice_str = "";
    for (int i=0;i<bob_str.length();i++){
        if (bob_str[i] == 'R'){
            if (b_cnt > 0){
                alice_str += 'P';
                b_cnt -= 1;
                b -= 1;
            } else {
                if (a-a_cnt > 0){
                    alice_str += 'R';
                    a -= 1;
                } else if (c-c_cnt > 0){
                    alice_str += 'S';
                    c -= 1;
                }
            }
        } else if (bob_str[i] == 'P'){
            if (c_cnt > 0){
                alice_str += 'S';
                c_cnt -= 1;
                c -= 1;
            } else {
                if (a-a_cnt > 0){
                    alice_str += 'R';
                    a -= 1;
                } else if (b-b_cnt > 0){
                    alice_str += 'P';
                    b -= 1;
                }
            }
        } else if (bob_str[i] == 'S'){
            if (a_cnt > 0){
                alice_str += 'R';
                a_cnt -= 1;
                a -= 1;
            } else {
                if (b-b_cnt > 0){
                    alice_str += 'P';
                    b -= 1;
                } else if (c-c_cnt > 0){
                    alice_str += 'S';
                    c -= 1;
                }
            }
        }
    }

    return 1;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    // freopen("input.txt","r",stdin);

    int res;
    cin >> t;

    for (int i=0;i<t;i++){
        cin >> n;
        cin >> a >> b >> c;
        cin >> bob_str;

        bobCount();

        res = solution();
        if (res == 0){
            cout << "NO" << endl;
        } else{
            cout << "YES" << endl;
            cout << alice_str << endl;
        }
        
    }
}




