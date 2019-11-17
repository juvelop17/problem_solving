#include <iostream>
#include <cstdio>

using namespace std;


int t,n,x,a,b;

int solution() {
    int min_num = min(a,b);
    int max_num = max(a,b);

    if (min_num - 1 < x){
        x -= min_num - 1;
        min_num = 1;
    } else {
        min_num -= x;
        x = 0;
    }

    if (n - max_num < x){
        x -= n - max_num;
        max_num = n;
    } else {
        max_num += x; 
        x = 0;
    }

    return max_num - min_num;

}


int main() {
    // freopen("input.txt","r",stdin);


    cin >> t;
    for(int i=0;i<t;i++){
        cin >> n >> x >> a >> b;
        cout << solution() << endl;
    }

    return 0;
}


