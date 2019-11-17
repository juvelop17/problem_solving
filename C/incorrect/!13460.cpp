#include <iostream>
#include <cstdio>
#include <queue>
#include <vector>

using namespace std;


int N,M;
char map_arr[10][10];
int mem_arr[10][10][10][10] = {0}; // red_i,red_j,blue_i,blue_j

int di[4] = {-1,1,0,0};
int dj[4] = {0,0,-1,1};
int ball_pos[2][2]; // RED : 0 BLUE : 1


void printMap(char map_arr[][10]){
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            if (i == ball_pos[0][0] && j == ball_pos[0][1]) {
                cout << "R" << "\t";
            } else if (i == ball_pos[1][0] && j == ball_pos[1][1]) {
                cout << "B" << "\t";
            } else {
                cout << map_arr[i][j] << "\t";
            }
        }
        cout << endl;
    }
    cout << endl;
}


bool checkRange(int i, int j){
    return i >= 0 && i < N && j >= 0 && j < M;
}


int moveBall(int dir, char color) {
    bool isUpdate = true;
    int i,j,res,new_i,new_j;
    res = 0;

    if (color == 'R') {
        i = ball_pos[0][0];
        j = ball_pos[0][1];
    } else if (color == 'B') {
        i = ball_pos[1][0];
        j = ball_pos[1][1];
    }

    while(isUpdate){
        isUpdate = false;

        new_i = i + di[dir];
        new_j = j + dj[dir];
        if (checkRange(new_i,new_j)){
            if (color == 'R' && ball_pos[1][0] == new_i && ball_pos[1][1] == new_j) {
                break;
            } else if (color == 'B' && ball_pos[0][0] == new_i && ball_pos[0][1] == new_j) {
                break;
            }

            if (map_arr[new_i][new_j] == '.'){
                i = new_i;
                j = new_j;
                isUpdate = true;
            } else if (map_arr[new_i][new_j] == 'O'){
                i = new_i;
                j = new_j;
                res = 1;
            }
        }
    }

    if (color == 'R') {
        ball_pos[0][0] = i;
        ball_pos[0][1] = j;
    } else if (color == 'B') {
        ball_pos[1][0] = i;
        ball_pos[1][1] = j;
    }

    return res;   // 이동
}


int move(int dir){
    int is_red_end = 0;
    int is_blue_end = 0;

    if (dir == 0) { // 상
        if (ball_pos[0][1] == ball_pos[1][1]){
            if (ball_pos[0][0] > ball_pos[1][0]){
                is_blue_end = moveBall(dir,'B');
                is_red_end = moveBall(dir,'R');
            } else {
                is_red_end = moveBall(dir,'R');
                is_blue_end = moveBall(dir,'B');
            }
        } else {
            is_red_end = moveBall(dir,'R');
            is_blue_end = moveBall(dir,'B');
        }
    } else if (dir == 1){ // 하
        if (ball_pos[0][1] == ball_pos[1][1]){
            if (ball_pos[0][0] < ball_pos[1][0]){
                is_blue_end = moveBall(dir,'B');
                is_red_end = moveBall(dir,'R');
            } else {
                is_red_end = moveBall(dir,'R');
                is_blue_end = moveBall(dir,'B');
            }
        } else {
            is_red_end = moveBall(dir,'R');
            is_blue_end = moveBall(dir,'B');
        }
    } else if (dir == 2){ // 좌
        if (ball_pos[0][0] == ball_pos[1][0]){
            if (ball_pos[0][1] > ball_pos[1][1]){
                is_blue_end = moveBall(dir,'B');
                is_red_end = moveBall(dir,'R');
            } else {
                is_red_end = moveBall(dir,'R');
                is_blue_end = moveBall(dir,'B');
            }
        } else {
            is_red_end = moveBall(dir,'R');
            is_blue_end = moveBall(dir,'B');
        }
    } else if (dir == 3){ // 우
        if (ball_pos[0][0] == ball_pos[1][0]){
            if (ball_pos[0][1] < ball_pos[1][1]){
                is_blue_end = moveBall(dir,'B');
                is_red_end = moveBall(dir,'R');
            } else {
                is_red_end = moveBall(dir,'R');
                is_blue_end = moveBall(dir,'B');
            }
        } else {
            is_red_end = moveBall(dir,'R');
            is_blue_end = moveBall(dir,'B');
        }
    }

    if (is_red_end == 1 && is_blue_end == 0) {
        return 1; // 성공
    } else if (is_blue_end == 1) {
        return -1; // 실패
    }

    return 0; // 진행
}


int solution(){
    
    queue<vector<int>> que;
    vector<int> node;
    node = {ball_pos[0][0],ball_pos[0][1],ball_pos[1][0],ball_pos[1][1],0};
    que.push(node);

    int node_red_i,node_red_j,node_blue_i,node_blue_j,node_cnt;
    while(!que.empty()){
        node = que.front();
        que.pop();

        node_red_i = node[0];
        node_red_j = node[1];
        node_blue_i = node[2];
        node_blue_j = node[3];
        node_cnt = node[4];

        if (node_cnt > 10) {
            return -1;
        }

        printMap(map_arr);

        for(int k=0;k<4;k++){
            int move_res = move(k);
            if (move_res == 0 && 
            mem_arr[ball_pos[0][0]][ball_pos[0][1]][ball_pos[1][0]][ball_pos[1][1]] == 0) { // 진행
                node = {ball_pos[0][0],ball_pos[0][1],ball_pos[1][0],ball_pos[1][1],node_cnt+1};
                que.push(node);
                mem_arr[ball_pos[0][0]][ball_pos[0][1]][ball_pos[1][0]][ball_pos[1][1]] = node_cnt+1;
            } else if (move_res == 1) { // 성공
                return node_cnt+1;
            }
        }
    }
    

    return -1;
}

int main(){
    freopen("input.txt","r",stdin);

    cin >> N >> M;

    char ch;
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            cin >> map_arr[i][j];
            if (map_arr[i][j] == 'R') {ball_pos[0][0] = i; ball_pos[0][1] = j; map_arr[i][j]='.';}
            if (map_arr[i][j] == 'B') {ball_pos[1][0] = i; ball_pos[1][1] = j; map_arr[i][j]='.';}
        }
    }

    printMap(map_arr);
    cout << solution();
}













