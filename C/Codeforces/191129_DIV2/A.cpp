#include <iostream>
#include <algorithm>
using namespace std;


int t,r,g,b;

int solution(){
    int mx,mid,mn;
    int arr[3] = {r,g,b};
    sort(arr,arr+3);

    mn = arr[0];
    mid = arr[1];
    mx = arr[2];

    if (mx >= mid + mn) {
        return mid + mn;
    } 

    return mx + (mid + mn - mx) / 2;
}

int main() {
    freopen("input.txt","r",stdin);

    cin >> t;
    for(int i=0;i<t;i++){
        cin >> r >> g >> b;
        cout << solution() << endl;
    }
    
}
