#include <iostream>

using namespace std;

long long t, a, b;

int solution() {
    long long mx, mn;
    mx = max(a,b);
    mn = min(a,b);

    if (mn == mx) {
        if (mn % 3 == 0){
            return 1;
        } else {
            return 0;
        }
    } 

    if (mn == 0) {
        return 0;
    }

    if (mn * 2 < mx) {
        return 0;
    } 
    else if (mn * 2 == mx) {
        return 1;
    }

    int diff = mx - mn;
    // cout << "num " << num << endl;
    if ((mn - diff) % 3 == 0) {
        return 1;
    } 
    return 0;
}

int main() {
    cin >> t;
    for (int test_case=1;test_case<=t;test_case++){
        cin >> a >> b;

        cout << (solution() ? "YES" : "NO") << endl;
    }

    return 0;
}
