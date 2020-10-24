#include <iostream>
#include <cstdio>

using namespace std;
int A[50][50];
int mem_arr[50][50] = {0};
int val_arr[50][50] = {0};
int N,L,R;
int num_cnt;


int di[4] = {-1,1,0,0};
int dj[4] = {0,0,-1,1};


void printMap(int arr[][50]) {
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cout << arr[i][j] << "\t";
        }
        cout << endl;
    }
    cout << endl;
}


bool checkRange(int i,int j){
    return i >= 0 && i < N && j >= 0 && j < N;
}


int explore(int i,int j,int cont_num){
    mem_arr[i][j] = cont_num;
    num_cnt += 1;
    int curr_size = A[i][j];
    int isChanged = 0;
    int sum = curr_size;
    
    int new_i,new_j;
    for(int k=0;k<4;k++){
        new_i = i + di[k], new_j = j + dj[k]; 
        if (checkRange(new_i,new_j) 
        && mem_arr[new_i][new_j] == 0
        && abs(curr_size - A[new_i][new_j]) >= L
        && abs(curr_size - A[new_i][new_j]) <= R){
            sum += explore(new_i,new_j,cont_num);
            isChanged = 1;
        }
    }

    return sum;
}


int calCountry(int i,int j,int num,int val){
    val_arr[i][j] = val;
    A[i][j] = val;
    
    int new_i,new_j;
    for(int k=0;k<4;k++){
        new_i = i + di[k], new_j = j + dj[k]; 
        if (checkRange(new_i,new_j) 
        && mem_arr[new_i][new_j] == num
        && val_arr[new_i][new_j] == 0){
            calCountry(new_i,new_j,num,val);
        }
    }

    return 0;
}


int solution(){
    bool isChanged = true;
    int res;
    int cont_num = 0;
    int sum = 0;
    int total_cnt = -1;

    while(isChanged){
        isChanged = false;
        total_cnt += 1;

        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                mem_arr[i][j] = 0;
                val_arr[i][j] = 0;
            }
        }

        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if (mem_arr[i][j] == 0){
                    cont_num += 1;
                    num_cnt = 0;
                    sum = explore(i,j,cont_num);
                    val_arr[i][j] = sum/num_cnt;
                    if (num_cnt > 1){
                        isChanged = true;
                    }
                }
            }
        }

        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if (val_arr[i][j] != 0){
                    calCountry(i,j,mem_arr[i][j],val_arr[i][j]);
                }
            }
        }

        // printMap(mem_arr);
        // printMap(val_arr);
    }

    return total_cnt;
}

int main() {
    // freopen("input.txt","r",stdin);

    cin >> N >> L >> R;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            cin >> A[i][j];
        }
    }

    cout << solution();

    return 0;
}









