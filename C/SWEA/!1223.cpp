#include <iostream>
#include <cstdio>
#include <string>
#include <stack>

using namespace std;


int len;
string input_str;
string output_str;
char ch,st;
stack<char> s;
stack<int> num_stack;


int postOrder(){
    for(int i=0;i<len;i++){
        ch = input_str[i];
        if (ch >= '1' && ch <= '9'){
            output_str.push_back(ch);
        } else {
            if (s.empty()){
                s.push(ch);
            } else {
                st = s.top();
                if((ch == '*' || ch == '/') && (st == '+' || st == '-')) {
                    s.push(ch);                    
                } else {
                    output_str.push_back(st);
                    s.pop();
                    s.push(ch);
                }
            }
        }
    }

    while (!s.empty()){
        ch = s.top();
        s.pop();
        output_str.push_back(ch);
    }

    cout << output_str << endl;

    return 0;
}

int calculate(){
    int sum = 0;
    int num,a,b;

    for (int i=0;i<len;i++){
        ch = output_str[i];
        if (ch >= '1' && ch <= '9'){
            num_stack.push(ch - '0');
        } else {
            a = s.top() - '0';
            s.pop();
            b = s.top() - '0';
            s.pop();
            if (ch == '+'){
                num_stack.push(a+b);
            } else if (ch == '-'){
                num_stack.push(a-b);
            } else if (ch == '*'){
                num_stack.push(a*b);
            } else if (ch == '/'){
                num_stack.push(a/b);
            }
        }    
    }

    return num_stack.top();
}

int solution() {
    postOrder();
    return calculate();
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    freopen("input.txt","r",stdin);

    for (int i=1;i<=10;i++){
        cin >> len;
        cin >> input_str;
        cout << len << endl;
        cout << input_str << endl;
        cout << "#" << i << " " << solution() << endl;
    }

    return 0;
}





