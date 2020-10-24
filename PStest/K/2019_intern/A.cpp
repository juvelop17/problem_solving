#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;


int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    
    vector<int> bucket;

    int i = 0;
    int curr_pos,curr_num;
    while(i<moves.size()){
        curr_pos = moves[i] - 1;
        for(int j=0;j<board.size();j++){
            if(board[j][curr_pos] != 0){
                curr_num = board[j][curr_pos];
                if (!bucket.empty() && bucket.back() == curr_num){
                    bucket.pop_back();
                    answer += 1;
                } else {
                    bucket.push_back(curr_num);
                }
                board[j][curr_pos] = 0;
                break;
            }
        }
        i++;
    }
    

    return answer * 2;
}


int main(){
    vector<vector<int>> board = {{0,0,0,0,0},{0,0,1,0,3},{0,2,5,0,1},{4,2,4,4,2},{3,5,1,3,1}};
    vector<int> moves = {1,5,3,5,1,2,1,4};    

    cout << solution(board, moves);

    return 0;
}




