#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;


vector<int> solution(string s) {
    vector<int> answer;
    vector<vector<int>> vec;

    int i=0;
    char curr_ch;
    while (i<s.length()){
        curr_ch = s[i];
        if (curr_ch == '{'){
            
        }
        if (curr_ch-'0' <= 9 && curr_ch-'0' > 0){

        }
        i++;
    }


    return answer;
}


int main(){
    string s = "{{2},{2,1},{2,1,3},{2,1,3,4}}";
    // string s = "{{1,2,3},{2,1},{1,2,4,3},{2}}";
    // string s = "{{20,111},{111}}";
    // string s = "{{123}}";
    // string s = "{{4,2,3},{3},{2,3,4,1},{2,3}}";
    

    vector<int> answer;
    answer = solution(s);
    for (int i=0;i<answer.size();i++){
        cout << answer[i] << " ";
    }
    cout << endl;

    return 0;
}




