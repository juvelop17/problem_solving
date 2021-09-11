#include <iostream>
#include <iomanip>

using namespace std;

int tc;
int n, x, pos;

int dfs(int l, int r, int goal, int cnt){
    int mid = (l + r) / 2;
    if (l == r) {
        return cnt;
    }
    
    if (mid <= goal) {
        return dfs(mid + 1, r, goal, cnt + 1);
    } else {
        return dfs(l, mid, goal, cnt + 1);
    }
}

int solution(){
    long long sum = 1;

    int depth = dfs(1, n, pos, 0);
    for (int i = n - (depth-1) ; i > 0 ; i--) {
        sum *= i;
        if (sum > 1000000007) {
            sum = sum % (1000000007);
        }
    }
    cout << sum << endl;

    for (int test=0;test<n;test++){
        long long sum = 1;
        
        for (int i = n + 20 - test ; i > 0 ; i--) {
            sum *= i;
            if (sum > 1000000007) {
                sum = sum % (1000000007);
            }
        }
        cout << "exam " << test << " : " << sum << endl;
    }


    return 0;  
}


int main() {
    freopen("input.txt","r",stdin);

    tc = 1;
    for(int t=0;t<tc;t++){
        cin >> n >> x >> pos;
        solution();
    }

    return 0;
}









