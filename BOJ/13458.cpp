#include <iostream>


using namespace std;



int N, A[1000000];
int B, C;


long long  solution() {
    long long cnt = 0;

    for(int i=0;i<N;i++){
        int res = A[i];
        res -= B;
        cnt++;
        
        if (res > 0) {
            cnt += res % C == 0 ? res / C : res / C + 1;
        }
    }

    return cnt;
}


int main() {
    freopen("input.txt","r",stdin);

    cin >> N;
    for (int i=0;i<N;i++){
        cin >> A[i];
    }
    cin >> B >> C;

    cout << solution();

}


