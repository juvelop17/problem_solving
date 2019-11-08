#include <iostream>
#include <cstdio>


using namespace std;

int q,n,m,d;
int m_arr[1000];
int board_arr[1000];

int solution(){
    int curr_pos = 0;
    int board_i = 0;
    int board_len;
    while(curr_pos < n+1){
        curr_pos += d;
        board_len = m_arr[board_i];
        
        for(int i=0;i<board_len && curr_pos+i < n+1;i++){
            board_arr[curr_pos+i]=board_len;
        }
        
        curr_pos += board_len;

    }

    return 0;
}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    freopen("input.txt","r",stdin);

    cin >> n >> m >> d;
    for(int i=0;i<m;i++){
        cin >> m_arr[i];
    }

    solution();

    return 0;
}

