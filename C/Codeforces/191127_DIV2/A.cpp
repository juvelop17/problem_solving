#include <iostream>
#include <cmath>

using namespace std;


int t,n,c,sum;


int solution() {
    if (sum % c == 0){
        return pow(sum / c, 2) * c;
    }
    if (c >= sum) {
        return sum;
    }
    
    int num = sum / c;
    int num_1_cnt = sum - num * c;
    int num_cnt = c - num_1_cnt;

    return pow(num, 2) * num_cnt + pow(num + 1, 2) * num_1_cnt;
}


int main() {
    freopen("input.txt","r",stdin);

    cin >> t;
    for(int test_case=1;test_case<=t;test_case++){
        cin >> c >> sum;
        cout << solution() << endl;
    }

    return 0;
}



