#include <iostream>
#include <cstdio>

using namespace std;
int A[50][50];
int mem_arr[50][50];
int N,L,R;
int con_cnt;

int explore(int i,int j){
    mem_arr[i][j] = 1;



    return 
}


int solution(){
    bool isChanged = true;
    int res;
    while(isChanged){
        isChanged = false;
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                res = explore(i,j);
                if (res == 1){
                    isChanged = true;
                }
            }
        }

    }


    return 0;
}

int main() {
    freopen("input.txt","r",stdin);

    cin >> N >> L >> R;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cin >> A[i][j];
        }
    }

    solution();

    return 0;
}









