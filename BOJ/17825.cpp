#include <iostream>
#include <cmath>
#include <iomanip>

// #define DEBUG

#ifdef DEBUG

#endif

using namespace std;


int board[33][6] = {  // score, 1, 2, 3, 4, 5
    {0, 1, 2, 3, 4, 5},
    {2, 2, 3, 4, 5, 6},
    {4, 3, 4, 5, 6, 7},
    {6, 4, 5, 6, 7, 8},
    {8, 5, 6, 7, 8, 9},
    {10, 20, 21, 22, 28, 29},
    {12, 7, 8, 9, 10, 11},
    {14, 8, 9, 10, 11, 12},
    {16, 9, 10, 11, 12, 13},
    {18, 10, 11, 12, 13, 14},
    {20, 23, 24, 28, 29, 30},
    {22, 12, 13, 14, 15, 16},
    {24, 13, 14, 15, 16, 17},
    {26, 14, 15, 16, 17, 18},
    {28, 15, 16, 17, 18, 19},
    {30, 25, 26, 27, 28, 29},
    {32, 17, 18, 19, 31, 32},
    {34, 18, 19, 31, 32, 32},
    {36, 19, 31, 32, 32, 32},
    {38, 31, 32, 32, 32, 32},
    {13, 21, 22, 28, 29, 30},
    {16, 22, 28, 29, 30, 31},
    {19, 28, 29, 30, 31, 32},
    {22, 24, 28, 29, 30, 31},
    {24, 28, 29, 30, 31, 32},
    {28, 26, 27, 28, 29, 30},
    {27, 27, 28, 29, 30, 31},
    {26, 28, 29, 30, 31, 32},
    {25, 29, 30, 31, 32, 32},
    {30, 30, 31, 32, 32, 32},
    {35, 31, 32, 32, 32, 32},
    {40, 32, 32, 32, 32, 32},
    {0, 32, 32, 32, 32, 32}
};
int mal[4] = {0, };
int dice[10];
int max_sum = -1;
int trace[10] = {-1, };

int dfs(int turn, int mal_num, int sum) {
    // cout << setw(10) << "turn, mal_num, sum "<< turn << " " << mal_num << " " << sum << endl;
    // trace[turn] = mal_num;

    if (turn == 10){
        if (sum > max_sum) {
            // cout << "sum max_sum " << sum << " " << max_sum << endl;
            // cout << "trace ";
            // for (int i = 0;i < 10;i++) cout << trace[i] << " ";
            // cout << endl;
            max_sum = sum;
        }
        return 0;
    }

    int cpos = mal[mal_num];
    int npos = board[cpos][dice[turn]];
    for(int i = 0;i < 4;i++){
        if (mal[i] == npos && npos != 32){
            return -1;
        }
    }

    mal[mal_num] = npos;
    sum += board[npos][0];

    dfs(turn+1,0,sum);
    dfs(turn+1,1,sum);
    dfs(turn+1,2,sum);
    dfs(turn+1,3,sum);

    mal[mal_num] = cpos;

    return 0;
}

int solution(){
    dfs(0, 0, 0);

    return max_sum;
}





int main() {
    #ifdef DEBUG
        clock_t start_clock, end_clock;
        start_clock = clock();

        freopen("input.txt","r",stdin);
    #endif

    for (int i = 0;i < 10;i++){
        cin >> dice[i];
    }
    
    cout << solution() << endl;




    #ifdef DEBUG
        end_clock = clock();
        cout << "time : " << end_clock - start_clock << endl;
    #endif

    return 0;
}



