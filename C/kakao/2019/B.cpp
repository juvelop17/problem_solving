#include <iostream>
#include <cstdio>

using namespace std;


string input_str;


void strSplit(string *u, string *v){
    int cnt = 0;
    int i=0;
    string s=*u;

    while(i<s.length()){
        if(s[i] == '('){
            cnt++;
        } else {
            cnt--;
        }

        i += 1;
        if (cnt == 0){
            *u = s.substr(0,i);
            *v = s.substr(i);
            break;
        }
    }
}


bool strCheck(string u){
    int cnt = 0;
    bool isTrue = true; // 올바른 괄호 문자열
    for(int i=0;i<u.length();i++){
        if(u[i] == '('){
            cnt++;
        } else {
            cnt--;
        }
        if (cnt < 0){
            isTrue = false;
        }
    }
    return isTrue;
}


string strConvert(string u){
    string s="";
    for(int i=1;i<u.length()-1;i++){
        if(u[i] == '('){
            s+=')';
        } else {
            s+='(';
        }
    }
    return s;
}


string solution(string p) {
    string answer = "";
    string u,v;

    if (p.compare("") == 0){
        return "";
    }
    u = p;
    strSplit(&u,&v);
    if (strCheck(u)){
        return u+solution(v);
    } else {
        answer += "(" + solution(v) + ")" + strConvert(u);
    }
    
    // cout << "u v : " << u << " " << v << endl;

    return answer;
}


int main(){
    freopen("input.txt","r",stdin);

    cin >> input_str;
    cout << solution(input_str);

    return 0;
}

