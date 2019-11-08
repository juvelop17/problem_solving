#include <iostream>
#include <cstdio>
#include <queue>

using namespace std;

int N,M;
int map_arr[1000][1000]={0};

int solution(){
    queue< vector<int> > que;

    vector<int> start (4,0);
    que.push(start);
    while(que.empty()){

    }


    return 0;
}

int main(){
    freopen("input.txt","r",stdin);

    cin >> N >> M;
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            cin >> map_arr[i][j];
        }
    }

    solution();

    return 0;
}

