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
    if (n < 2){
        return -1;
    }

    int start = 0, end = 1;
    int max_num,max_cnt;

    map<int,int> m;
    m[num_arr[0]] = 1;
    max_num = num_arr[0];
    max_cnt = m[num_arr[0]];
    int min_len = 2*100000;

    while(end < n){
        int end_num = num_arr[end];
        if ((end - start < 2 || m[end_num] <= max_cnt)){
            m[end_num] += 1;
            if (m[end_num] > max_cnt) {
                max_num = end_num;
                max_cnt = m[end_num];
                
                while(num_arr[start] ){
                    int start_num = num_arr[start];
                    if (m[start_num] < m[max_num]) {
                        m[start_num] -= 1;
                        start++;
                        min_len = min(min_len,end-start);
                    } else {
                        min_len = min(min_len,end-start);
                        break;
                    }
                }

            }
            end++;
            


        }

        
    }

    return min_len;
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


