#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>

using namespace std;

struct Tree{
    int x;
    int y;
    int age;
};

struct cmp{
    bool operator() (Tree a, Tree b){
        return a.age < b.age;
    }
};

int N,M,K;
int map_arr[11][11] = {0};    // 맵
int A[11][11] = {0};    // 양분
int tree_arr[11][11] = {0}; // 나무 나이
int dx[8] = {-1,-1,-1,0,0,1,1,1};
int dy[8] = {-1,0,1,-1,1,-1,0,1};

priority_queue<Tree,vector<Tree>,cmp> tree_pque;
priority_queue<Tree,vector<Tree>,cmp> alive_pque;
priority_queue<Tree,vector<Tree>,cmp> dead_pque;




bool checkRange(int i, int j) {
    return i >= 1 && i <= N && j >= 1 && j <= N;
}

int solution(){
    int y = 0;

    for(int i=1;i<=N;i++){
        for(int j=1;j<=N;j++){
            map_arr[i][j] = 5;
        }
    }

    while(y < K){
        // 봄
        while(!tree_pque.empty()){
            Tree tr = tree_pque.top(); tree_pque.pop();
            if(map_arr[tr.x][tr.y] >= tr.age){
                map_arr[tr.x][tr.y] -= tr.age;
                tr.age += 1;
                alive_pque.push(tr);
            } else {
                dead_pque.push(tr);
            }
        }

        // 여름
        while(!dead_pque.empty()){
            Tree tr = dead_pque.top(); dead_pque.pop();
            map_arr[tr.x][tr.y] += tr.age/2;
        }

        // 가을
        while(!alive_pque.empty()){
            Tree tr = alive_pque.top(); alive_pque.pop();
            if (tr.age % 5 == 0){
                for(int i=0;i<8;i++){
                    int new_x = tr.x + dx[i];
                    int new_y = tr.y + dy[i];
                    if (checkRange(new_x,new_y)){
                        Tree t = {new_x,new_y,1};
                        tree_pque.push(t);
                    }
                }
            }
            tree_pque.push(tr);
        }

        // 겨울
        for(int i=1;i<=N;i++){
            for(int j=1;j<=N;j++){
                map_arr[i][j] += A[i][j];
            }
        }
       
        y++;
    }

    return tree_pque.size();
}


int main(){
    freopen("input.txt","r",stdin);

    cin >> N >> M >> K;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cin >> A[i][j];
        }
    }

    
    int x,y,z;
    for(int i=0;i<M;i++){
        Tree tr;
        cin >> tr.x >> tr.y >> tr.age;
        tree_pque.push(tr);
    }

    cout << solution();

    return 0;
}



