#include <iostream>

using namespace std;


int N1, N2, T;
char R1[1000], R2[1000];
char row[1000];
int dir[1000];

void printRow(){
    cout << row << endl;
}


int solution(){
    for(int i=0;i<N1;i++){
        row[i] = R1[i];
        dir[i] = 1;
    }
    for(int i=0;i<N2;i++){
        row[N1+i] = R2[i];
        dir[N1+i] = -1;
    }

    int cnt = 0;
    int curr;
    int cur_dir = 0;
    while (cnt<T) {
        curr = 0;
        while(curr <N1+N2-1){
            if (dir[curr] == 1 && dir[curr+1] == -1){
                char tmp = row[curr];
                row[curr] = row[curr+1];
                row[curr+1] = tmp;
                
                dir[curr] = -1; dir[curr+1] = 1;
                curr++;
            }
            curr++;
        }
        // printRow();

        cnt++;
    }
    printRow();

    return 0;
}

int main(){
    char ch;

    freopen("input.txt","r",stdin);
    
    cin >> N1 >> N2;
    for(int i=N1-1;i>=0;i--){
        cin >> R1[i];
    }
    for(int i=0;i<N2;i++){
        cin >> R2[i];
    }
    cin >> T;
    
    solution();

    return 0;
}


