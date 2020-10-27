#include <iostream>
#include <iomanip>

using namespace std;

int tc;
int n;
int square[100][100] = {0};
bool che[100001] = {false};

void print_square(){
    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            cout << square[i][j] << " ";
        }
        cout << endl;
    }
}

int cal_row(int i) {
    int sum = 0;
    for (int j=0;j<n;j++){
        sum += square[i][j];
    }
    return sum;
}

int cal_col(int i) {
    int sum = 0;
    for (int j=0;j<n;j++){
        sum += square[j][i];
    }
    return sum;
}

int solution(){
    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++){
            square[i][j] = 1;
        }
    }
    while (!(che[cal_row(0)] && che[cal_col(0)])) { // not prime
        square[0][0]++;
        while (che[square[0][0]]) { // prime
            square[0][0]++;
        }
    }

    for (int i=1;i<n;i++){
        square[i][i] = square[0][0];
    }
    print_square();

    return 0;  
}


int main() {
    // freopen("input.txt","r",stdin);

    for (int i = 2; i < 100001;i++){
        che[i] = true;
    }

    int num = 1000;
    for (int i = 2; i <= num; i++) { 
        if (che[i] == false) // 이미 체크된 수의 배수는 확인하지 않는다
            continue;
        for (int j = i + i; j <= num; j += i) { // i를 제외한 i의 배수들은 0으로 체크
            che[j] = false;
        }
    }

    cin >> tc;
    for(int t=0;t<tc;t++){
        cin >> n;
        solution();
    }

    return 0;
}









