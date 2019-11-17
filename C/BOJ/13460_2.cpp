#include <iostream>
#include <cstdio>

using namespace std;

int N,M,red_ball[2],blue_ball[2];
char map_arr[10][10];
int mem_arr[10][10][10][10] = {0};
int ans = 11;

int di[4]={-1,1,0,0};
int dj[4]={0,0,-1,1};


void printMap(int ri,int rj,int bi,int bj){
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            if (i==ri && j==rj){
                cout << "R" << "\t";
            } else if (i==bi && j==bj){
                cout << "B" << "\t";
            } else {
                cout << map_arr[i][j] << "\t";
            }
        }
        cout << endl;
    }
    cout << endl;
}


int move(int ri,int rj,int bi,int bj,int cnt){
    printMap(ri,rj,bi,bj);

    if (cnt == 11){
        return -1;
    }

    if (cnt >= ans){
        return -1;
    }

    
    for(int k=0;k<4;k++){
        int mr=0,mb=0;
        int new_ri=ri, new_rj=rj, new_bi=bi, new_bj=bj;

        while(map_arr[new_bi+di[k]][new_bj+dj[k]] != '#'){
            if (map_arr[new_bi+di[k]][new_bj+dj[k]] == 'O'){
                return -1; // 실패
            }
            
            new_bi+=di[k], new_bj+=dj[k];
            mb++;
        }

        while(map_arr[new_ri+di[k]][new_rj+dj[k]] != '#'){
            if (map_arr[new_ri+di[k]][new_rj+dj[k]] == 'O'){
                ans = ans > cnt ? cnt : ans;
                return 1;
            }
            
            new_ri+=di[k], new_rj+=dj[k];
            mr++;
        }

        if(new_ri==new_bi && new_rj==new_bj){
            if(mr > mb){
                new_ri -= di[k];
                new_rj -= dj[k];
            } else {
                new_bi -= di[k];
                new_bj -= dj[k];
            }
        }

        if(mem_arr[new_ri][new_rj][new_bi][new_bj] == 0 || 
                mem_arr[new_ri][new_rj][new_bi][new_bj] > cnt){
            mem_arr[new_ri][new_rj][new_bi][new_bj] = cnt;
            move(new_ri,new_rj,new_bi,new_bj,cnt+1);
        }
    }

    return -1;
}


int main() {
    freopen("input.txt","r",stdin);

    cin >> N >> M;
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            cin >> map_arr[i][j];
            if (map_arr[i][j] == 'R') {red_ball[0]=i; red_ball[1]=j; map_arr[i][j] = '.';}
            if (map_arr[i][j] == 'B') {blue_ball[0]=i; blue_ball[1]=j; map_arr[i][j] = '.';}
        }
    }

    printMap(red_ball[0],red_ball[1],blue_ball[0],blue_ball[1]);
    move(red_ball[0],red_ball[1],blue_ball[0],blue_ball[1],1);
    cout << (ans != 11 ? ans : -1);

    return 0;
}


