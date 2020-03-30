#include <iostream>
#include <vector>

using namespace std;

vector<int> invec;
vector<int> outvec;


int solution(){
    outvec.resize(invec.size(),0);
    
    for(int i=0;i<invec.size();i++){
        int curr = i;
        int init = i;
        int cnt = 0;
        while (outvec[curr] == 0) {
            curr = invec[curr];
            cnt++;
            if (curr == init){
                for(int j=0;j<cnt;j++){
                    outvec[curr] = cnt;
                    curr = invec[curr];
                }
            }
        }
    }

    for (int i=0;i<outvec.size();i++) {
        cout << outvec[i] << " ";
    }
    cout << endl;

    return 0;
}


int main() {
    freopen("input.txt","r",stdin);

    int q,n,a;
    cin >> q;
    for (int tc=0;tc<q;tc++){
        cin >> n;
        for(int i=0;i<n;i++) {
            cin >> a;
            invec.push_back(a);
        }
        solution();

        invec.clear();
        outvec.clear();
    }

    return 0;
}
