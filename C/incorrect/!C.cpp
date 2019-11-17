// https://codeforces.com/contest/1257/problem/C
// C. Dominated Subarray

#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int mem_arr[5];
int t,n;
vector<int> num_arr;


int solution() {
    int min_next = n + 1;
    int best = n + 1;

    vector<int> next(n,-1);
    vector<int> last(n+1,-1);
    for(int i=n-1;i>=0;i++){
        next[i] = last[num_arr[i]];
        last[num_arr[i]] = i;
    }

    for(int i=n-1;i>=0;i++){
        if (next[i] < min_next){
            if(){
                
            }

            min_next = min(min_next,next[i]);
        }
    }

    return best;
}


int main(){
    int num;

    freopen("input.txt","r",stdin);

    cin >> t;
    for(int i=0;i<t;i++){
        num_arr.clear();

        cin >> n;
        for (int j=0;j<n;j++){
            cin >> num;
            num_arr.push_back(num);
        }
        cout << solution() << endl;
    }

    return 0;
}


