// 벽 부수고 이동하기
#include <iostream>
#include <cstdio>
#include <queue>

using namespace std;

int N,M;
int map_arr[1000][1000]={0};
int mem_arr[2][1000][1000]={0};

int di[4] = {0,0,-1,1};
int dj[4] = {-1,1,0,0};


bool check_range(int i,int j){
    return i < N && j < M && i >= 0 && j >= 0;
}


void printMap(int arr[][1000]){
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            cout << arr[i][j] << "\t";
        }
        cout << endl;
    }
    cout << endl;
}



int solution(){
    queue<vector<int>> que;

    vector<int> start (4,0);  // i, j, cnt, chance
    start[2] = 1;   
    start[3] = 1;   
    que.push(start);

    vector<int> node;
    int node_i,node_j,node_cnt,node_chance;
    int new_i,new_j;
    while(!que.empty()){
        node = que.front();
        que.pop();

        node_i=node[0];
        node_j=node[1];
        node_cnt=node[2];
        node_chance=node[3];

        cout << 0 << endl;
        printMap(mem_arr[0]);
        cout << 1 << endl;
        printMap(mem_arr[1]);

        for (int d=0;d<4;d++){
            new_i = node_i + di[d];
            new_j = node_j + dj[d];
            if (check_range(new_i,new_j)) {
                if (map_arr[new_i][new_j] == 0) {
                    if (mem_arr[node_chance][new_i][new_j] == 0 || mem_arr[node_chance][new_i][new_j] > node_cnt){
                        vector<int> vec{new_i,new_j,node_cnt+1,node_chance};
                        mem_arr[node_chance][new_i][new_j] = node_cnt+1;
                        que.push(vec);
                    }
                } else {
                    if (node_chance == 1 && 
                    (mem_arr[node_chance-1][new_i][new_j] == 0 || mem_arr[node_chance-1][new_i][new_j] > node_cnt)) {
                        vector<int> vec{new_i,new_j,node_cnt+1,node_chance-1};
                        mem_arr[node_chance-1][new_i][new_j] = node_cnt+1;
                        que.push(vec);
                    }
                }
            }
        }


        
    }


    return 0;
}

int main(){
    freopen("input.txt","r",stdin);

    char ch;
    cin >> N >> M;
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            cin >> ch;
            cout << "map_arr[i][j] " << ch << endl;
            map_arr[i][j] = ch;
        }
    }

    printMap(map_arr);


    // solution();

    return 0;
}

