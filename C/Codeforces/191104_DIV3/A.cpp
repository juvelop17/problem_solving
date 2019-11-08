#include <iostream>
#include <cstdio>


using namespace std;

long long q,a,b,n,S;

long long solution(){
    long long sum = 0;
    if (a*n >= S){
        sum += ((long long) S/n) * n;
    } else {
        sum += a*n;
    }

    if (sum + b >= S){
        cout << "YES" << endl;
        return 0;
    }
    cout << "NO" << endl;
    return 0;
}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    // freopen("input.txt","r",stdin);

    cin >> q;
    for (int i=0;i<q;i++){
        cin >> a >> b >> n >> S;
        solution();
    }

    return 0;
}

