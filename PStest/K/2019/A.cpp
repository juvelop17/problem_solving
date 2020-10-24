#include <iostream>
#include <cstdio>


using namespace std;


string s;


int solution(string s) {
    int answer = 0;
    string str;
    int min_len = s.length();

    string test = s.substr(0,6);

    for(int i=1;i<=s.length();i++){
        str = "";
        int j = i;
        int cnt = 1;

        string curr_str = s.substr(0,i);
        string next_str;
        while(j+i-1<s.length()){
            next_str = s.substr(j,i);
            if (curr_str.compare(next_str) != 0){
                str += (cnt>1?to_string(cnt):"") + curr_str;
                cnt = 0;
            }
            curr_str = next_str;
            j += i;
            cnt++;
        }
        str += (cnt>1?to_string(cnt):"") + curr_str + s.substr(j);
        
        if (str.length() < min_len){
            min_len = str.length();
        }
        // cout << i << " str : " << str << endl;
    }

    // cout << "min_len : " << min_len << endl;

    return min_len;
}


int main() {

    freopen("input.txt","r",stdin);

    cin >> s;
    solution(s);
}




