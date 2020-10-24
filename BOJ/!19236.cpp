#include <iostream>
#include <cmath>
#include <iomanip>

// #define DEBUG

#ifdef DEBUG

#endif

using namespace std;

typedef struct {
    int i,j,dir;
} Shark;

typedef struct {
    int i,j,dir;
} Fish;

int max_sum = -1;

int di[8] = {-1,-1,0,1,1,1,0,-1};
int dj[8] = {0,-1,-1,-1,0,1,1,1};

int eat(int mp[4][4], Fish fish[16], Shark shark, int i, int j, int sum);
int move(int mp[4][4], Fish fish[16]);

bool checkRange(int i, int j) {
    return i >= 0 && i < 4 && j >= 0 && j < 4;
}

void printMap(int mp[][4]){
    for (int i = 0;i < 4;i++){
        for (int j = 0;j < 4;j++){
            cout << setw(10) << mp[i][j];
        }
        cout << endl;
    }
    cout << endl;
}


int eat(int mp[4][4], Fish fish[16], Shark shark, int i, int j, int sum){
    int new_mp[4][4];
    Fish new_fish[16];
    Shark new_shark;
    for (int a=0;a < 4;a++){
        for (int b=0;b < 4;b++){
            new_mp[a][b] = mp[a][b];        
        }
    }
    for (int a=0;a < 16;a++){
        new_fish[a] = fish[a];
    }
    int fish_num = new_mp[i][j];
    new_mp[shark.i][shark.j] = 0;
    new_mp[i][j] = -1;
    sum += fish_num;
    new_shark = {i,j,new_fish[fish_num - 1].dir};
    new_fish[fish_num - 1] = {-1,-1,-1};
    if (sum > max_sum) {
        max_sum = sum;
    }
    // cout << "i, j, sum, max_sum : " << i << " " << j << " " << sum << " " << max_sum << endl;
    // printMap(new_mp);
    move(new_mp, new_fish);
    // printMap(new_mp);

    for (int d = 1;d < 4;d++){
        int ni = i + di[new_shark.dir] * d;
        int nj = j + dj[new_shark.dir] * d;

        if (checkRange(ni,nj) && new_mp[ni][nj] > 0){
            eat(new_mp, new_fish, new_shark, ni, nj, sum);
        }
    }

    return 0;
}

int move(int mp[4][4], Fish fish[16]) {
    for (int idx = 0;idx < 16; idx++){
        // cout << setw(10) << "idx " << idx + 1 << endl;
        // printMap(mp);
        if (fish[idx].dir == -1){
            continue;
        }

        int ci = fish[idx].i;
        int cj = fish[idx].j;
        for (int d=0;d < 8;d++){
            int ndir = (fish[idx].dir + d) % 8;
            int ni = ci + di[ndir];
            int nj = cj + dj[ndir];

            if (checkRange(ni,nj) && mp[ni][nj] >= 0){
                mp[ci][cj] = mp[ni][nj];
                mp[ni][nj] = idx + 1;
                fish[idx] = {ni, nj, ndir};

                if (mp[ci][cj] > 0) {
                    fish[mp[ci][cj] - 1].i = ci;
                    fish[mp[ci][cj] - 1].j = cj;
                }
                break;
            }
        
        }
    }

    return 0;
}




int solution(int mp[4][4], Fish fish[16], Shark shark){
    eat(mp, fish, shark, 0, 0, 0);

    return max_sum;
}





int main() {
    #ifdef DEBUG
        clock_t start_clock, end_clock;
        start_clock = clock();

        freopen("input.txt","r",stdin);
    #endif

    ////////////////////////////////////////////////
    int mp[4][4];
    Shark shark;
    Fish fish[16];

    int a, b;
    for (int i=0;i < 16;i++){
        cin >> a >> b;
        a--; b--;
        mp[i/4][i%4] = a + 1;
        fish[a] = {i/4, i%4, b};
    }
    shark = {0, 0, -1};

    cout << solution(mp,fish,shark) << endl;



    ////////////////////////////////////////////////

    #ifdef DEBUG
        end_clock = clock();
        cout << "time : " << end_clock - start_clock << endl;
    #endif

    return 0;
}



