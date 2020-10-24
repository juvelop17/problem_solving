#include <iostream>

using namespace std;

int n;
int comb_arr[32][32];
int one_arr[32];


int comb(int n, int r){
    if (n <= 0 || r <= 0) {
        return 0;
    }
    comb_arr[1][0] = 1;    
    comb_arr[1][1] = 1;
    for (int i = 2; i <= n; i++){
        comb_arr[i][0] = 1;
        for (int j = 1; j <= r; j++){
            comb_arr[i][j] = comb_arr[i - 1][j - 1] + comb_arr[i - 1][j];
         }
    }

    return comb_arr[n][r];
}

void display(int one_arr[],int cnt){
    for(int i=cnt;i>=1;i--){
        cout << one_arr[i] << " ";
    }
    cout << endl;
}

int solution(int n){
    int answer;

    int num = n; 
    int cnt = 0;
    while (num > 0) {
        cnt++;
        if (num % 2 == 1) {
            one_arr[cnt] = 1;
        } else {
            one_arr[cnt] = 0;
        }
        num /= 2;
    }

    // display(one_arr,cnt);

    int sum = 0;
    int one_cnt = 0;
    for(int i=1;i<=cnt;i++){
        if (one_arr[i] == 1) {
            one_cnt += 1;
            sum += comb(i-1,one_cnt);
            // cout << i-1 << " " << one_cnt << endl;
        }
    }

    // cout << sum << endl;

    answer = sum;

    return answer;
}

int main() {
    freopen("input.txt","r",stdin);

    cin >> n;
    cout << solution(n);

}





// void comb(int arr[], int idx, int n, int r, int target) {
//     if (r==0)
// }
