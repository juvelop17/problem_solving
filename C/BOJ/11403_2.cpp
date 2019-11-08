// 11403 경로찾기
// 가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, 
// i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성하시오.

#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int N,mat[100][100];
int mem_mat[100][100] = {0};
int point_arr[100*100][2];
int cnt=0;


void dfs(int i, int j){
    if (mem_mat[i][j]){
        return;
    }
    mem_mat[i][j] = 1;
    
    for(int k=0;k<N;k++){
        if (mat[j][k]){
            dfs(j,k);
        }
    }
}


void printMat(int mat[][100]){
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cout << mat[i][j] << " ";
        }
        cout << endl;
    }
}


int solution(){
    int pi,pj;
    for(int i=0;i<cnt;i++){
        pi = point_arr[i][0];
        pj = point_arr[i][1];
        dfs(pi,pj);
    }

    printMat(mem_mat);
    
    return 0;
}

int main(){
    // freopen("input.txt","r",stdin);

    cin >> N;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cin >> mat[i][j];
            if (mat[i][j] == 1){
                point_arr[cnt][0]=i;
                point_arr[cnt][1]=j;
                cnt++;
            }
        }
    }

    solution();

    return 0;
}







