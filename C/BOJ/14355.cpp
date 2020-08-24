#include <iostream>
#include <math.h>
#include <algorithm>
using namespace std;

int T;
int TC[25][4];
char result[8];
char ch_list[3] = {'P','R','S'};
int ch_remain[3];



void print_arr(char arr[], int depth){
    for(int i=0;i<depth;i++){
        cout << arr[i];
    }
    cout << endl;
}

char get_winner(char a, char b){
    if (a > b) swap(a, b);
    if (a == 'P' && b == 'R') return 'P';
    if (a == 'P' && b == 'S') return 'S';
    return 'R';
}

bool check_tournament(int r) {
    char round[8];
    int num = r;

    for(int i=0;i<r;i++){
        round[i] = result[i];
    }

    while (num > 1){
        for(int i=0;i<num;i=i+2){
            if (round[i] == round[i+1]) return false; // IMPOSSIBLE
            round[i/2] = get_winner(round[i],round[i+1]);
        }
        num /= 2;
    }

    return true;
}


// 중복순열
bool rpt_perm(int n, int r, int depth){
    if (depth == r) {
        // print_arr(result, depth);
        return check_tournament(depth);
    }

    for(int i=0;i<n;i++){
        if (ch_remain[i] == 0) continue;
        ch_remain[i]--;
        result[depth] = ch_list[i];
        if (rpt_perm(n,r,depth+1)) return true; // true인 경우 탈출
        ch_remain[i]++;
    }

    return false;
}

int solution(){
    
    for(int i=0;i<T;i++){
        int N = TC[i][0];
        int R = TC[i][1];
        int P = TC[i][2];
        int S = TC[i][3];

        ch_remain[0] = P;
        ch_remain[1] = R;
        ch_remain[2] = S;

        cout << "Case #" << i+1 << ": ";
        if (rpt_perm(3,pow(2,N),0)) print_arr(result, pow(2,N));
        else cout << "IMPOSSIBLE" << endl;
    }

    return 0;
}

int main() {
    freopen("input.txt", "r", stdin);

    cin >> T;
    //N, R, P, S
    for(int i=0;i<T;i++){
        cin >> TC[i][0] >> TC[i][1] >> TC[i][2] >> TC[i][3];
    }

    solution();

    return 0;
}

