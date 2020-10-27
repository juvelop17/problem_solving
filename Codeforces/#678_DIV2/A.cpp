#include <iostream>

using namespace std;


int tc;
int n,m;
int a[100];


int solution(){
    int sum = 0;
    for (int i =0;i<n;i++){
        sum += a[i];
    }
    if (sum == m){
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;  
}


int main() {
    freopen("input.txt","r",stdin);

    cin >> tc;
    for(int t=0;t<tc;t++){
        cin >> n >> m;
        for (int tt=0;tt<n;tt++){
            cin >> a[tt];
        }
        solution();
    }


    return 0;
}









