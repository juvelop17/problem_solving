#include <stdio.h>
#include <queue>


using namespace std;


int T,K;
int MAX_VAL = 100000;
int min_a = MAX_VAL;
int min_b = MAX_VAL;

int map_arr[100][100];
int memory_arr[100][100];
int goal[2] = {0};


void printMap(int map_arr[][100]){
    for (int i=0;i<100;i++){
        for (int j=0;j<100;j++){
            printf("%d",map_arr[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}


int explore(int i,int j){
    int res = -1;

    memory_arr[i][j] = 1;

    if (i == 0){
        return j;
    }

    if (map_arr[i][j+1] == 1 && memory_arr[i][j+1] == 0){
        res = explore(i,j+1);
    } else if (map_arr[i][j-1] == 1 && memory_arr[i][j-1] == 0){
        res = explore(i,j-1);
    } else if (map_arr[i-1][j] == 1 && memory_arr[i-1][j] == 0){
        res = explore(i-1,j);
    }


    return res;
}


// int explore(int i,int j){
    // int res = -1;

    // memory_arr[i][j] = 1;

    // if (i == 0){
    //     return j;
    // }

    // queue<int,int> que; 
    // q.

    // if (map_arr[i][j+1] == 1 && memory_arr[i][j+1] == 0){
    //     res = explore(i,j+1);
    // } else if (map_arr[i][j-1] == 1 && memory_arr[i][j-1] == 0){
    //     res = explore(i,j-1);
    // } else if (map_arr[i-1][j] == 1 && memory_arr[i-1][j] == 0){
    //     res = explore(i-1,j);
    // }


    // return res;
// }



int solution(){
    int x;
    for (int i=0;i<100;i++){
        for (int j=0;j<100;j++){
            memory_arr[i][j] = 0;
        }
    }

    x = explore(goal[0],goal[1]);

    return x;
}


int main(){
    freopen("input.txt","r",stdin);
    int num;

    int T = 10;
    for (int t=1;t<=T;t++){
        scanf("%d",&num);

        for (int i=0;i<100;i++){
            for (int j=0;j<100;j++){
                scanf("%d",&map_arr[i][j]);
                if (map_arr[i][j] == 2){
                    goal[0] = i;
                    goal[1] = j;
                }
            }
        }
        // printMap(map_arr);
        printf("#%d %d\n",t,solution());
        // printMap(memory_arr);

    }

    return 0;
}


