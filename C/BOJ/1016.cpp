#include <iostream>
#include <cmath>
#include <time.h>

using namespace std;

long long min_num, max_num;
bool num[1000001];

long long solution() {
    long long result = max_num - min_num + 1;
    
    for(long long i=2;i*i<=max_num;i++){
        long long j;
        j = min_num / (i*i);
        if (i*i*j != min_num) {
            j++;
        }

        while (j*i*i <= max_num) {
            if (num[j*i*i-min_num]) {
                j++;
                continue;
            }
            num[j*i*i-min_num] = true;
            j++;
            result--;
        }    
    }

    return result;
}

int main() {
    clock_t start_clock, end_clock;

    // freopen("input.txt","r",stdin);
    // start_clock = clock();
    
    cin >> min_num >> max_num;

    for(int i=0;i<1000001;i++){
        num[i] = false;
    }
    
    cout << solution() << endl;

    // end_clock = clock();
    // cout << "time : " << end_clock - start_clock << endl;

    return 0;
}



